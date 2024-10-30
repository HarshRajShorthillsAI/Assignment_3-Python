import pytest
from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader


class TestLargeFileLoader:
    @pytest.fixture
    def large_test_files(self):
        # Paths to your large files
        return {
            'pptx': 'tests/test_files/coa.pptx',  # Replace with your actual path
            'docx': 'tests/test_files/servlet.docx',  # Replace with your actual path
            'pdf': 'tests/test_files/Python Cookbook.pdf'      # Replace with your actual path
        }

    def test_large_pptx_loader(self, large_test_files):
        pptx_loader = PPTLoader(large_test_files['pptx'])
        docs = pptx_loader.load_file()
        assert docs is not None, "Failed to load PPTX file. No documents found."

    def test_large_docx_loader(self, large_test_files):
        docx_loader = DOCXLoader(large_test_files['docx'])
        docs = docx_loader.load_file()
        assert docs is not None, "Failed to load DOCX file. No documents found."

    def test_large_pdf_loader(self, large_test_files):
        pdf_loader = PDFLoader(large_test_files['pdf'])
        docs = pdf_loader.load_file()
        assert docs is not None, "Failed to load PDF file. No documents found."
