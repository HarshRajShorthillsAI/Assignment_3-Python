import pytest
from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader


class TestEmptyFileLoader:
    @pytest.fixture
    def empty_test_files(self):
        # Paths to your large files
        return {
            'pptx': 'tests/test_files/zero_PPTX.pptx',  # Replace with your actual path
            'docx': 'tests/test_files/zero_DOCX.docx',  # Replace with your actual path
            'pdf': 'tests/test_files/zero_PDF.pdf'      # Replace with your actual path
        }

    def test_empty_pptx_loader(self, empty_test_files):
        pptx_loader = PPTLoader(empty_test_files['pptx'])
        
        with pytest.raises(ValueError, match="Failed to load the PPTX file: Unsupported file format"):
            pptx_loader.validate_file()
            pptx_loader.load_file()

    def test_empty_docx_loader(self, empty_test_files):
        docx_loader = DOCXLoader(empty_test_files['docx'])
        
        with pytest.raises(ValueError, match="Failed to load DOCX file: Unsupported file format"):
            docx_loader.validate_file()
            docx_loader.load_file()
    def test_empty_pdf_loader(self, empty_test_files):
        pdf_loader = PDFLoader(empty_test_files['pdf'])
        base_error_message = 'Failed to load PDF file:'
        expected_pdf_file = empty_test_files['pdf']  # Get the PDF file name
    
        with pytest.raises(ValueError, match=f'{base_error_message}.*{expected_pdf_file}'):
            pdf_loader.validate_file()
            pdf_loader.load_file()