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

    def create_directory(self, sub_dir: str):
        """Create directory if it does not exist."""
        path = os.path.join(self.output_dir, sub_dir)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

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
        text_dir = self.create_directory("text")
        
        with open(os.path.join(text_dir, filename + ".txt"), 'w') as f:
            f.write(data)

    def save_images(self, images, filename: str):
        """Save image data based on file type."""
        images_dir = self.create_directory("images")
        for idx, image_data in enumerate(images):
            image = image_data.get('image')
            ext = image_data.get('ext', 'png')
            image_filename = (
                f"{filename}_image_{idx + 1}.jpg" if filename.endswith(".pdf")
                else f"slide_{image_data['slide_number']}_shape_{image_data['shape_number']}.{ext}"
                if filename.endswith(".pptx")
                else f"image_{idx + 1}.{ext}"
            )
            image_path = os.path.join(images_dir, image_filename)
            self._save_image_to_path(image, image_path)

    def _save_image_to_path(self, image, path):
        """Helper to save a PIL image to disk."""
        try:
            if isinstance(image, bytes):
                image = PILImage.open(BytesIO(image))
            if isinstance(image, PILImage.Image):
                image.save(path)
        except Exception as e:
            print(f"Error saving image at {path}: {e}")

    def save_urls(self, urls, filename: str):
        """Save URLs to a separate .txt file."""
        url_text = "\n".join(f"url: {url}" for url in urls)
        self.save_to_text_file(url_text, filename + "_urls", "urls")

    def save_tables(self, tables, filename: str):
        """Save table data as .csv files."""
        tables_dir = self.create_directory("tables")
        for idx, table in enumerate(tables):
            table_path = os.path.join(tables_dir, f"table_{idx + 1}.csv")
            df = pd.DataFrame(table) if not isinstance(table, pd.DataFrame) else table
            df.to_csv(table_path, index=False)

    def save_to_text_file(self, data, filename: str, subdir: str, ext="txt"):
        """General function for saving text-based data."""
        dir_path = self.create_directory(subdir)
        with open(os.path.join(dir_path, filename + f".{ext}"), "w") as f:
            f.write(data)