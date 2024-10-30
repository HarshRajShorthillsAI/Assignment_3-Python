import pytest
from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader
import msoffcrypto


class TestCrruptedFileLoader:
    @pytest.fixture
    def corr_test_files(self):
        # Paths to your large files
        return {
            'pptx': 'tests/test_files/ch01_corrupted.pptx',  # Replace with your actual path
            'docx': 'tests/test_files/utf8_test_file_corrupted.docx',  # Replace with your actual path
            'pdf': 'tests/test_files/utf8_test_file_corrupted.pdf'      # Replace with your actual path
        }

    def test_corr_pptx_loader(self, corr_test_files):
        pptx_loader = PPTLoader(corr_test_files['pptx'])
        
        with pytest.raises(ValueError, match="Failed to load the PPTX file: Unsupported file format"):
            pptx_loader.validate_file()
            pptx_loader.load_file()
        
    def test_corr_docx_loader(self, corr_test_files):
        docx_loader = DOCXLoader(corr_test_files['docx'])
        
        with pytest.raises(ValueError, match="Failed to load DOCX file: Unsupported file format"):
            docx_loader.validate_file()
            docx_loader.load_file()
        
    def test_corr_pdf_loader(self, corr_test_files):
        pdf_loader = PDFLoader(corr_test_files['pdf'])
    
        base_error_message = 'Failed to load PDF file:'
        expected_pdf_file = corr_test_files['pdf']  # Get the PDF file name
    
        with pytest.raises(ValueError, match=f'{base_error_message}.*{expected_pdf_file}'):
            pdf_loader.validate_file()
            pdf_loader.load_file()
