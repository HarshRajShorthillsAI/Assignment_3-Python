import pytest

from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader
from loaders.ppt_loader import PPTLoader

import os
from dotenv import load_dotenv

load_dotenv()
class TestPasswordProtectedFileLoading:

    """
    Test case expected result demands user input for correct password but for now hard coded the password to check the loading of password protected documents
    """

    @classmethod
    def setup_class(cls):
        cls.protected_pdf_file_path = "tests/test_files/unit 5_protected.pdf"  # Path to the password-protected PDF
        cls.protected_docx_file_path = "tests/test_files/servlet_protected.docx"
        cls.protected_pptx_file_path = "tests/test_files/IOmra_protected.pptx"
        cls.pdf_correct_password = os.getenv("PDF_PASSWORD")  # Replace with the actual password
        cls.docx_correct_password = os.getenv("DOCX_PASSWORD")
        cls.pptx_correct_password = os.getenv("PPTX_PASSWORD")
    
    def test_load_password_protected_pdf_file(self):
        assert self.protected_pdf_file_path is not None, "Path to the password-protected PDF file is not set."
        assert self.pdf_correct_password is not None, "Password for the PDF file is not provided."

        # Instantiate the PDFLoader with the file path and password
        pdf_loader = PDFLoader(file_path=self.protected_pdf_file_path, password=self.pdf_correct_password)

        try:
            # Attempt to load the file, which should handle the password authentication internally
            pdf_document = pdf_loader.load_file()

            # Verify that we can successfully access the document content
            first_page_text = pdf_document[0].get_text()  # Extract text from the first page
            assert first_page_text is not None, "Failed to load content from the password-protected PDF."
        
        except ValueError as e:
            # Fail the test if an error occurs during loading
            pytest.fail(f"An error occurred while loading the password-protected PDF: {e}")


    def test_load_password_protected_docx_file(self):
        # Ensure that the password-protected DOCX file path and password are provided
        assert self.protected_docx_file_path is not None, "Path to the password-protected DOCX file is not set."
        assert self.docx_correct_password is not None, "Password for the DOCX file is not provided."

        # Instantiate the DOCXLoader with the file path and password
        docx_loader = DOCXLoader(file_path=self.protected_docx_file_path, password=self.docx_correct_password)

        try:
            # Attempt to load the file, which should handle the password decryption internally
            docx_document = docx_loader.load_file()

            # Verify that we can successfully access the document content
            paragraphs = [para.text for para in docx_document.paragraphs]
            assert paragraphs, "Failed to load content from the password-protected DOCX."

            print("Password-protected DOCX loaded and content is accessible.")

        except ValueError as e:
            pytest.fail(f"An error occurred while loading the password-protected DOCX: {e}")

    def test_load_password_protected_pptx_file(self):
        """Test case for loading a password-protected PPTX file."""
        try:
            # Initialize the PPTLoader with the path to the protected PPTX file and the correct password
            ppt_loader = PPTLoader(self.protected_pptx_file_path, password=self.pptx_correct_password)
            
            # Attempt to load the PPTX file
            presentation = ppt_loader.load_file()

            # Check if the presentation was loaded successfully
            assert presentation is not None, "Failed to load the PPTX presentation."

            # Access the number of slides to confirm we can access the content
            slide_count = len(presentation.slides)
            assert slide_count > 0, "The PPTX presentation contains no slides."

            # Optionally, access the first slide to ensure we can interact with it
            first_slide = presentation.slides[0]
            assert first_slide is not None, "Failed to access the first slide of the PPTX presentation."

        except Exception as e:
            pytest.fail(f"An error occurred while loading the password-protected PPTX: {e}")