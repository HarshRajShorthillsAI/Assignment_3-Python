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
        self.extracted_data = {
          'text': None,
          'images': None,
          'urls': None,
          'tables': None  
        }
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

        # Define extractors for each type of data
        extraction_methods = {
            'text': extractor.extract_text,
            'image': extractor.extract_images,
            'url': extractor.extract_urls,
            'table': extractor.extract_tables
        }

        # Execute extraction methods for each data type
        for data_type, extraction_method in extraction_methods.items():
            self.extracted_data[data_type] = extraction_method()

        

        # Close the file (if applicable)
        if hasattr(self.loader, 'close_file'):
            self.loader.close_file()

    def save_extracted_data(self):
        # Create a folder for storing the extracted data
        base_name = os.path.splitext(os.path.basename(self.file_path))[0]
        self.output_dir = os.path.join("extracted_data", base_name)
        file_storage = FileStorage(self.output_dir)

        # Save each extracted data type to files
        for data_type, data in self.extracted_data.items():
            if data:
                file_storage.save(data, os.path.basename(self.file_path), data_type)

    def save_to_database(self):
        # Save the extracted data into SQLite
        db_path = "extracted_data.db"  # Path to your SQLite database
        sql_storage = SQLStorage(db_path)

        # Save each extracted data type to the database
        for data_type, data in self.extracted_data.items():
            if data:
                sql_storage.save(data, data_type)

        sql_storage.close()

        print(f"Extracted data saved to: {self.output_dir} and SQLite database: {db_path}")

    def run(self):
        # Execute the main steps
        self.determine_loader()
        self.process_file()
        self.save_extracted_data()
        self.save_to_database()

    @staticmethod
    def list_directories_and_files(root_dir):
        for dirpath, dirnames, filenames in os.walk(root_dir):
            print(f"Directory: {dirpath}")
            for filename in filenames:
                print(f"  File: {filename}")
            print()  # Blank line for better readability

# import subprocess

if __name__ == "__main__":
    Main.list_directories_and_files("tests/test_files")
    
    # file_path = input("Write valid file path here: ")

    file_path = "tests/test_files/unit 5.docx"  # Change this to the file you want to process
    main_instance = Main(file_path)
    
    main_instance.run()