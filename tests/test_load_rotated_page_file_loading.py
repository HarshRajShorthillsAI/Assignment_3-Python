import pytest

from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader


class TestLoadRotatedPageFileLoader:
    @pytest.fixture
    def large_test_files(self):
        # Paths to your large files
        return {
            'pptx': 'tests/test_files/IOmra_pages_rotated.pptx',  # Replace with your actual path
            'docx': 'tests/test_files/unit 5_page_rotated.docx',  # Replace with your actual path
            'pdf': 'tests/test_files/unit 5_rotated_pages.pdf'      # Replace with your actual path
        }

    def test_load_rotated_page_pptx_loader(self, large_test_files):
        pptx_loader = PPTLoader(large_test_files['pptx'])
        pptx_loader.validate_file()
        docs = pptx_loader.load_file()
        assert docs is not None, "Failed to load PPTX file."

    def test_load_rotated_page_docx_loader(self, large_test_files):
        docx_loader = DOCXLoader(large_test_files['docx'])
        docx_loader.validate_file()
        docs = docx_loader.load_file()
        assert docs is not None, "Failed to load DOCX file."

    def test_load_rotated_page_pdf_loader(self, large_test_files):
        pdf_loader = PDFLoader(large_test_files['pdf'])
        pdf_loader.validate_file()
        docs = pdf_loader.load_file()
        assert docs is not None, "Failed to load PDF file."