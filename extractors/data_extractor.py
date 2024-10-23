import fitz  # PyMuPDF for PDF handling
import camelot  # For PDF table extraction
import docx  # For DOCX handling
import pptx  # For PPTX handling
from PIL import Image as PILImage
import os
from io import BytesIO
import pandas as pd

class DataExtractor:
    def __init__(self, loader):
        self.loader = loader
        self.file_path = loader.file_path

    def extract_text(self): #working fine
        if self.file_path.endswith('.pdf'):
            # Extract text from PDF
            reader = self.loader.load_file()
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text

        elif self.file_path.endswith('.docx'):
            # Extract text from DOCX
            doc = self.loader.load_file()
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text

        elif self.file_path.endswith('.pptx'):
            # Extract text from PPTX
            ppt = self.loader.load_file()
            text = ""
            for slide in ppt.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        text += shape.text + "\n"
            return text

        else:
            raise ValueError("Unsupported file format for text extraction.")

    def extract_images(self): #working in sql, defaulted to png in file.
        images = []

        if self.file_path.endswith('.pdf'):
            # PDF image extraction
            pdf_document = fitz.open(self.file_path)
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                image_list = page.get_images(full=True)
                for img in image_list:
                    xref = img[0]
                    base_image = pdf_document.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    width, height = base_image["width"], base_image["height"]
                    images.append({
                        "image_data": image_bytes,
                        "ext": image_ext,
                        "page": page_num + 1,
                        "dimensions": (width, height)
                    })
            pdf_document.close()

        elif self.file_path.endswith('.docx'):
            # DOCX image extraction
            doc = self.loader.load_file()
            
            for rel in doc.part.rels:
                if doc.part.rels[rel].is_external == False:
                    if "image" in doc.part.rels[rel].target_ref:
                        image_binary = doc.part.rels[rel].target_part.blob
                        image_data = ''
                        try:
                            image_data = PILImage.open(BytesIO(image_binary))
                        except Exception as e:
                            print("error")
                        image = {
                            "image_data": image_binary,
                            "image": image_data
                        }
                        images.append(image)

        elif self.file_path.endswith('.pptx'):
            # PPTX image extraction
            ppt = self.loader.load_file()

            for slide_number, slide in enumerate(ppt.slides):
                for shape_number, shape in enumerate(slide.shapes):
                    if shape.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.PICTURE:
                        image_stream = shape.image.blob
                        image_ext = shape.image.ext

                        # Load the image using PIL
                        try:
                            image = PILImage.open(BytesIO(image_stream))
                        except Exception as e:
                            print(f"Failed to load image from slide {slide_number+1}, shape {shape_number+1}: {e}")

                        # Create a dictionary to store image data
                        image_data = {
                            'image': image,
                            'image_data': image_stream,
                            'ext': image_ext,
                            'slide_number': slide_number + 1,
                            'shape_number': shape_number + 1
                        }

                        images.append(image_data)  # Add image data to the list

        return images

    def extract_urls(self):
        urls = []

        if self.file_path.endswith('.pdf'):
            # PDF URL extraction
            pdf_document = fitz.open(self.file_path)
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)

                links = page.get_links()

                for link in links:
                    if "uri" in link:
                        url = link["uri"]
                        rect = link["from"]
                        urls.append({
                            "url": url,
                            "page": page_num + 1,
                            "position": {
                                "x0": rect.x0,
                                "y0": rect.y0,
                                "x1": rect.x1,
                                "y1": rect.y1
                            }
                        })
            pdf_document.close()

        elif self.file_path.endswith('.docx'):
            # DOCX URL extraction
            doc = self.loader.load_file()

            for rel in doc.part.rels.values():
                # if "hyperlink" in rel.target_ref:
                urls.append({"url": rel.reltype})

        elif self.file_path.endswith('.pptx'):
            # PPTX URL extraction
            presentation = pptx.Presentation(self.file_path)

            for slide_num, slide in enumerate(presentation.slides, start=1):
                for shape in slide.shapes:
                    # Check if the shape has a hyperlink
                    if shape.has_text_frame and shape.text_frame:
                        for paragraph in shape.text_frame.paragraphs:
                            for run in paragraph.runs:
                                if run.hyperlink.address:
                                    urls.append({
                                    "url": run.hyperlink.address,
                                    "slide": slide_num,
                                    "text": run.text
                                    })

                    # Shapes like images or other elements may have hyperlinks as well
                    if shape.has_text_frame is False and hasattr(shape, 'hyperlink') and shape.hyperlink and shape.hyperlink.target:
                        urls.append({
                        "url": shape.hyperlink.target,
                        "slide": slide_num,
                        "shape_type": shape.shape_type
                        })

        return urls

    def extract_tables(self):
        tables = []

        if self.file_path.endswith('.pdf'):
            # Extract tables from PDF using Camelot
            tables = camelot.read_pdf(self.file_path, pages="all")
            table_data = [table.df for table in tables]  # List of DataFrames
            return table_data

        elif self.file_path.endswith('.docx'):
            # Extract tables from DOCX
            doc = self.loader.load_file()
            table_data = []
            for table in doc.tables:
                table_content = [[cell.text for cell in row.cells] for row in table.rows]
                df = pd.DataFrame(table_content)
                table_data.append(table_content)
            return table_data

        elif self.file_path.endswith('.pptx'):
            # Extract tables from PPTX (typically tables are part of shapes)
            ppt = self.loader.load_file()
            table_data = []
            for slide in ppt.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "table"):
                        table = shape.table
                        table_content = [[cell.text for cell in row.cells] for row in table.rows]
                        table_data.append(table_content)
            return table_data

        return tables