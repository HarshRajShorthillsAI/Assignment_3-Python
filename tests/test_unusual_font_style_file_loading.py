import os
import pytest

from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader
from loaders.ppt_loader import PPTLoader

class TestUnusualTextFileLoading:
    # Specify the path to your unusual text content file
    pdf_file_path = "tests/test_files/styled-document.pdf"                 # Update this path as necessary
    docx_file_path = "tests/test_files/styled-document.docx"               # Update this path as necessary
    pptx_file_path = "tests/test_files/styled_document.pptx"               # Update this path as necessary

    def test_load_pdf_file(self):
        # Precondition: Verify that the PDF file exists
        assert os.path.exists(self.pdf_file_path), "PDF file does not exist."

        try:
            # Load the PDF file using PDFLoader
            pdf_loader = PDFLoader(self.pdf_file_path, None)
            pdf_loader.validate_file()
            pdf_document = pdf_loader.load_file()  # Assuming load_file handles decryption if needed

            # Check that we can access the number of pages
            assert pdf_document.page_count > 0, "The PDF file has no pages."
            print("PDF file loaded successfully.")
            print(f"Number of pages: {pdf_document.page_count}")

        except Exception as e:
            pytest.fail(f"An error occurred while loading the PDF file: {e}")

    def test_load_docx_file(self):
        # Precondition: Verify that the DOCX file exists
        assert os.path.exists(self.docx_file_path), "DOCX file does not exist."

        try:
            # Load the DOCX file using DOCXLoader
            docx_loader = DOCXLoader(self.docx_file_path, None)
            docx_loader.validate_file()
            docx_document = docx_loader.load_file()  # Assuming load_file handles decryption if needed

            # Check that we can access the number of paragraphs
            assert len(docx_document.paragraphs) > 0, "The DOCX file has no paragraphs."
            print("DOCX file loaded successfully.")
            print(f"Number of paragraphs: {len(docx_document.paragraphs)}")

        except Exception as e:
            pytest.fail(f"An error occurred while loading the DOCX file: {e}")

    def test_load_pptx_file(self):
        # Precondition: Verify that the PPTX file exists
        assert os.path.exists(self.pptx_file_path), "PPTX file does not exist."

        try:
            # Load the PPTX file using PPTLoader
            ppt_loader = PPTLoader(self.pptx_file_path, None)
            ppt_loader.validate_file()
            pptx_document = ppt_loader.load_file()  # Assuming load_file handles decryption if needed

            # Check that we can access the number of slides
            assert len(pptx_document.slides) > 0, "The PPTX file has no slides."
            print("PPTX file loaded successfully.")
            print(f"Number of slides: {len(pptx_document.slides)}")

        except Exception as e:
            pytest.fail(f"An error occurred while loading the PPTX file: {e}")

# To run the tests, you would typically use a command like:
# pytest -q --tb=line test_file_loading.py