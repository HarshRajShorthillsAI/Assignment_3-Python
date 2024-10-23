import os
from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader
from loaders.ppt_loader import PPTLoader
from extractors.data_extractor import DataExtractor
from storage.file_storage import FileStorage
from storage.sql_storage import SQLStorage

class Main:
    def __init__(self, file_path):
        self.file_path = file_path
        self.loader = None
        self.extracted_text = None
        self.images = None
        self.urls = None
        self.tables = None
        self.output_dir = None

    def determine_loader(self):
        # Determine the file type and use the appropriate loader
        if self.file_path.endswith(".pdf"):
            self.loader = PDFLoader(self.file_path)
        elif self.file_path.endswith(".docx"):
            self.loader = DOCXLoader(self.file_path)
        elif self.file_path.endswith(".pptx"):
            self.loader = PPTLoader(self.file_path)
        else:
            raise ValueError("Unsupported file format. Use PDF, DOCX, or PPTX.")

    def process_file(self):
        # Validate the file type
        self.loader.validate_file()

        # Load the file
        self.loader.load_file()

        # Create an instance of DataExtractor for extracting content
        extractor = DataExtractor(self.loader)

        # Extract text, images, URLs, and tables
        self.extracted_text = extractor.extract_text()
        self.images = extractor.extract_images()
        self.urls = extractor.extract_urls() #if self.file_path.endswith(('.pdf', '.docx')) else None
        self.tables = extractor.extract_tables() #if self.file_path.endswith(('.pdf', '.docx')) else None

        # Close the file (if applicable)
        if hasattr(self.loader, 'close_file'):
            self.loader.close_file()

    def save_extracted_data(self):
        # Create a folder for storing the extracted data
        base_name = os.path.splitext(os.path.basename(self.file_path))[0]
        self.output_dir = os.path.join("extracted_data", base_name)
        file_storage = FileStorage(self.output_dir)

        # Save extracted text, images, URLs, and tables to files
        if self.extracted_text:
            file_storage.save(self.extracted_text, os.path.basename(self.file_path), 'text')
        if self.images:
            file_storage.save(self.images, os.path.basename(self.file_path), 'image')
        if self.urls:
            file_storage.save(self.urls, os.path.basename(self.file_path), 'url')
        if self.tables:
            file_storage.save(self.tables, os.path.basename(self.file_path), 'table')

    def save_to_database(self):
        # Save the extracted data into SQLite
        db_path = "extracted_data.db"  # Path to your SQLite database
        sql_storage = SQLStorage(db_path)

        # Save extracted data to the database
        if self.extracted_text:
            sql_storage.save(self.extracted_text, 'text')
        if self.images:
            sql_storage.save(self.images, 'image')
        if self.urls:
            sql_storage.save(self.urls, 'url')
        if self.tables:
            sql_storage.save(self.tables, 'table')

        print(f"Extracted data saved to: {self.output_dir} and SQLite database: {db_path}")

    def run(self):
        # Execute the main steps
        self.determine_loader()
        self.process_file()
        self.save_extracted_data()
        self.save_to_database()


if __name__ == "__main__":
    file_path = "tests/test_files/dir2/PMDocs.pdf"  # Change this to the file you want to process
    main_instance = Main(file_path)
    main_instance.run()