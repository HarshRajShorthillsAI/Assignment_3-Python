import fitz
from loaders.file_loader import FileLoader

class PDFLoader(FileLoader):
    def __init__(self, file_path, password=None):
        super().__init__(file_path, password)

    def validate_file(self):
        # Ensure that the file is a PDF by checking its extension
        if not self.file_path.endswith('.pdf'):
            raise ValueError(f"Invalid file type: Expected a PDF file.")
        # Further validation can be added here if needed

    def load_file(self):
        """Attempt to load the PDF file."""
        try:
            # Open the PDF document
            pdf_document = fitz.open(self.file_path)
            # If the document is encrypted, attempt to authenticate using the password
            if pdf_document.is_encrypted:
                if self.password is None:
                    raise ValueError("The PDF file is password-protected. A password is required to open it.")

                # Attempt to authenticate with the provided password
                if not pdf_document.authenticate(self.password):
                    raise ValueError("Failed to open PDF. The provided password is incorrect.")

            return pdf_document
        except Exception as e:
            error = f'Failed to load PDF file: {e}'
            raise ValueError(error)

    def verify_content(self):
        return super().verify_content()
    
    def get_metadata(self):
        """Retrieve metadata from the PDF file."""
        try:
            pdf_document = self.load_file()
            metadata = pdf_document.metadata
            pdf_document.close()  # Close file after accessing metadata
            return metadata
        except Exception as e:
            raise ValueError(f"Failed to retrieve PDF metadata: {e}")

    def get_fileType(self):
        return super().get_fileType()