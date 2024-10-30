import os
import pytest
from fpdf import FPDF
from docx import Document
from pptx import Presentation
from pptx.util import Inches  # Ensure Pt is imported
from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader
from loaders.ppt_loader import PPTLoader

class TestImageOnlyDocumentLoader:
    image_paths = ['tests/test_files/img.png']

    @staticmethod
    def create_image_only_pdf_file(folder_path, filename="image_only_file.pdf"):
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        for image_path in TestImageOnlyDocumentLoader.image_paths:
            pdf.image(image_path, x=10, w=190)  # Adjust width (w) as needed
            pdf.ln(10)  # Add space after each image

        pdf.output(file_path)
        return file_path  # Return the file path

    @staticmethod
    def create_image_only_docx_file(folder_path, filename="image_only_file.docx"):
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        doc = Document()

        for image_path in TestImageOnlyDocumentLoader.image_paths:
            doc.add_picture(image_path, width=Inches(4))  # Adjust the width as needed
            doc.add_paragraph()  # Add a paragraph to provide spacing between images

        doc.save(file_path)
        return file_path  # Return the file path

    @staticmethod
    def create_image_only_pptx_file(folder_path, filename="image_only_file.pptx"):
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        prs = Presentation()

        for image_path in TestImageOnlyDocumentLoader.image_paths:
            slide_layout = prs.slide_layouts[5]  # Using a blank layout
            slide = prs.slides.add_slide(slide_layout)
            left = Inches(1)
            top = Inches(1)
            width = Inches(8)
            height = Inches(5)
            slide.shapes.add_picture(image_path, left, top, width, height)

        prs.save(file_path)
        return file_path  # Return the file path

    @pytest.fixture(autouse=True)
    def setup(self):
        self.folder_path = "tests/test_files"
        self.pdf_file_path = self.create_image_only_pdf_file(self.folder_path, "image_only_file.pdf")
        self.docx_file_path = self.create_image_only_docx_file(self.folder_path, "image_only_file.docx")
        self.pptx_file_path = self.create_image_only_pptx_file(self.folder_path, "image_only_file.pptx")

    def test_text_only_pdf_file_loading(self):
        pdf_loader = PDFLoader(self.pdf_file_path)
        pdf_loader.validate_file()
        pdf_document = pdf_loader.load_file()
        assert pdf_document is not None, "Failed to load the text only PDF document."

    def test_text_only_docx_file_loading(self):
        docx_loader = DOCXLoader(self.docx_file_path)
        docx_loader.validate_file()
        docx_document = docx_loader.load_file()
        assert docx_document is not None, "Failed to load the text only DOCX document"

    def test_text_only_pptx_file_loading(self):
        pptx_loader = PPTLoader(self.pptx_file_path)
        pptx_loader.validate_file()
        pptx_document = pptx_loader.load_file()
        assert pptx_document is not None, "Failed to load the text only PPTX document."
