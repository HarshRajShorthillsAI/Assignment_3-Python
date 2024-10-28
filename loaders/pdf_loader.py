from PyPDF2 import PdfReader
from loaders.file_loader import FileLoader

class PDFLoader(FileLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def validate_file(self):
        # Ensure that the file is a PDF by checking its extension
        if not self.file_path.lower().endswith('.pdf'):
            raise ValueError(f"Invalid file type: {self.file_path} is not a PDF.")
        # Further validation can be added here if needed

    def load_file(self):
        try:
            reader = PdfReader(self.file_path)
            return reader
        except Exception as e:
            raise ValueError(f"Failed to load PDF file: {e}")

    def get_metadata(self):
        reader = PdfReader(self.file_path)
        metadata = reader.metadata
        return metadata
