"""
import os
import json
import pandas as pd  # For saving tables as CSV
from io import BytesIO
from PIL import Image as PILImage  # For handling PPTX images

class FileStorage:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def save(self, data, filename: str, data_type: str):
        Save data based on type: 'text', 'image', 'url', or 'table'.
        if data_type == 'text':
            self.save_text(data, filename)
        elif data_type == 'image':
            self.save_images(data, filename)
        elif data_type == 'url':
            self.save_urls(data, filename)
        elif data_type == 'table':
            self.save_tables(data, filename)
        else:
            raise ValueError("Unsupported data type. Use 'text', 'image', 'url', or 'table'.")

    def save_text(self, data, filename: str):
        Save text data as a .txt file.
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(self.output_dir, txt_filename)
        with open(output_path, 'w') as f:
            f.write(data)

    def save_images(self, images, filename: str):
        Save image data to image files and metadata.
        images_dir = os.path.join(self.output_dir, "images")
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        metadata = []
        for idx, image in enumerate(images):
            # Check if the image is a PIL Image object (PPTX case)
            if isinstance(image, PILImage.Image):  
                # Convert the image to bytes (PNG format)
                image_bytes = BytesIO()
                image.save(image_bytes, format='PNG')  # Save as PNG
                image_bytes = image_bytes.getvalue()
                image_filename = f"image_{idx + 1}.png"
                image_ext = 'png'
            # Otherwise, assume it's a dictionary (PDF/DOCX case)
            elif isinstance(image, dict):
                # Check if it's a dictionary and has the necessary keys
                image_filename = f"image_{idx + 1}.{image.get('ext', 'jpg')}"
                image_bytes = image.get('image_data', b"")
                image_ext = image.get('ext', 'jpg')
            else:
                # If the image is neither a PIL Image nor a dictionary, skip it
                continue

            # Save the image data to file
            image_path = os.path.join(images_dir, image_filename)
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)

            metadata.append({
                "file_name": image_filename,
                "page_number": image.get("page", "N/A"),
                "dimensions": image.get("dimensions", "N/A")
            })

        metadata_file = os.path.join(images_dir, 'metadata.json')
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=4)

    def save_urls(self, urls, filename: str):
        Save URLs to a .txt file and metadata to a .json file.
        urls_dir = os.path.join(self.output_dir, "urls")
        if not os.path.exists(urls_dir):
            os.makedirs(urls_dir)

        url_filename = os.path.join(urls_dir, "urls.txt")
        metadata = []

        with open(url_filename, "w") as url_file:
            for url_info in urls:
                url_file.write(f"{url_info['url']}\n")
                metadata.append({
                    "url": url_info["url"],
                    "page_number": url_info["page"],
                    "position": url_info["position"]
                })

        metadata_file = os.path.join(urls_dir, "metadata.json")
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=4)

    def save_tables(self, tables, filename: str):
        Save extracted tables as CSV files.
        tables_dir = os.path.join(self.output_dir, "tables")
        if not os.path.exists(tables_dir):
            os.makedirs(tables_dir)

        for idx, table in enumerate(tables):
            csv_filename = f"table_{idx + 1}.csv"
            csv_path = os.path.join(tables_dir, csv_filename)
            
            # Check if the table is a DataFrame (from PDF extraction)
            if isinstance(table, pd.DataFrame):
                table.to_csv(csv_path, index=False)
            # Otherwise, treat it as a list (from DOCX or PPTX extraction)
            elif isinstance(table, list):
                with open(csv_path, 'w', newline='') as f:
                    for row in table:
                        f.write(",".join(row) + "\n")
"""

import os
import json
from PIL import Image as PILImage  # For handling image data
from io import BytesIO
import pandas as pd  # For saving tables as CSV (if needed)

class FileStorage:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def save(self, data, filename: str, data_type: str):
        """Save data based on type: 'text', 'image', 'url', or 'table'."""
        if data_type == 'text':
            self.save_text(data, filename)
        elif data_type == 'image':
            self.save_images(data, filename)
        elif data_type == 'url':
            self.save_urls(data, filename)
        elif data_type == 'table':
            self.save_tables(data, filename)
        else:
            raise ValueError("Unsupported data type. Use 'text', 'image', 'url', or 'table'.")

    def save_text(self, data, filename: str):
        """Save text data as a .txt file."""
        text_dir = os.path.join(self.output_dir, "text")
        if not os.path.exists(text_dir):
            os.makedirs(text_dir)
        
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(text_dir, txt_filename)
        with open(output_path, 'w') as f:
            f.write(data)

    def save_images(self, images, filename: str):
        """Save image data to image files."""
        
        if filename.endswith(".pdf"):
            images_dir = os.path.join(self.output_dir, "images")
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            for idx, image in enumerate(images):
                
                image = image['image_data']
                
                image_filename = ""

                if isinstance(image, bytes):
                    try:
                        image = PILImage.open(BytesIO(image))
                    except Exception as e:
                        print(f"Error converting bytes to image for image {idx + 1}: {e}")
                        continue

                if isinstance(image, PILImage.Image):
                    image_bytes = BytesIO()
                    try:
                        image.save(image_bytes, format='PNG')  # Save in PNG format
                        image_bytes = image_bytes.getvalue()
                        image_filename = f"{filename}_image_{idx + 1}.jpg" if filename else f"image_{idx + 1}.jpg"

                    except Exception as e:
                        print(f"Error saving image {idx + 1}: {e}")
                        continue

                image_path = os.path.join(images_dir, image_filename)

                try:
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                except Exception as e:
                    print(f"Error writing image to disk: {e}")

        elif filename.endswith(".pptx"):
            # Create the directory to store the images
            images_dir = os.path.join(self.output_dir, "images")
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            for idx, image_data in enumerate(images):
                # Image object from PIL
                image = image_data['image']
                image_ext = image_data['ext']  # Get the original image extension

                # Define the filename and path
                image_filename = f"slide_{image_data['slide_number']}_shape_{image_data['shape_number']}.{image_ext}"
                image_path = os.path.join(images_dir, image_filename)

                try:
                    # Save the image in its original format
                    image.save(image_path)
                    print(f"Saved image: {image_filename}")
                except Exception as e:
                    print(f"Failed to save image {image_filename}: {e}")
        else:
            images_dir = os.path.join(self.output_dir, "images")
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            for idx, image in enumerate(images):
                image = image['image']
                if isinstance(image, PILImage.Image):
                    image_bytes = BytesIO()
                    image.save(image_bytes, format='PNG')  # Save in PNG format
                    image_bytes = image_bytes.getvalue()
                    image_filename = f"image_{idx + 1}.png"
                else:
                    continue

                image_path = os.path.join(images_dir, image_filename)
                with open(image_path, "wb") as img_file:
                    img_file.write(image_bytes)


    def save_urls(self, urls, filename: str):
        """Save URLs to a separate .txt file."""
        urls_dir = os.path.join(self.output_dir, "urls")
        if not os.path.exists(urls_dir):
            os.makedirs(urls_dir)

        url_filename = os.path.splitext(filename)[0] + "_urls.txt"
        with open(os.path.join(urls_dir, url_filename), "w") as url_file:
            for url_info in urls:
                url_file.write(f"url: {url_info}\n")

    def save_tables(self, tables, filename: str):
        """Save table data as .csv files."""
        tables_dir = os.path.join(self.output_dir, "tables")
        if not os.path.exists(tables_dir):
            os.makedirs(tables_dir)

        for idx, table in enumerate(tables):
            table_filename = f"table_{idx + 1}.csv"
            table_path = os.path.join(tables_dir, table_filename)

            # Check if the table is a DataFrame, if not convert it to one
            if isinstance(table, pd.DataFrame):
                # Save the table as CSV if it's already a DataFrame
                table.to_csv(table_path, index=False)
            else:
                # Convert the list (or other object) to a DataFrame and then save as CSV
                df = pd.DataFrame(table)  # Assuming it's a list of lists
                df.to_csv(table_path, index=False)
