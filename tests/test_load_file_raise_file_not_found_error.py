import pytest

# Assuming PDFLoader is defined in a module named pdf_loader_module
from loaders.pdf_loader import PDFLoader
from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader

class TestFileNotFoundInLoadFile:

    @pytest.fixture
    def unavailable_test_files(self):
        # Paths to your large files
        return {
            'pptx': 'tests/test_files/zero.pptx',  # Replace with your actual path
            'docx': 'tests/test_files/zero.docx',  # Replace with your actual path
            'pdf': 'tests/test_files/zero.pdf'      # Replace with your actual path
        }
    
    def test_load_pptx_raises_file_not_found_error(self, unavailable_test_files):
        # Step 1: Create an instance of PDFLoader
        pptx_loader = PPTLoader(unavailable_test_files['pptx'])
        
        base_error_message = r'Failed to load the PPTX file: \[Errno 2\] No such file or directory: '
        expected_pptx_file = unavailable_test_files['pptx']  # Get the PDF file name

        with pytest.raises(ValueError, match=f'{base_error_message}.*{expected_pptx_file}'):
            
            pptx_loader.validate_file()
            pptx_loader.load_file()

    def test_load_docx_raises_file_not_found_error(self, unavailable_test_files):
        # Step 1: Create an instance of PDFLoader
        docx_loader = DOCXLoader(unavailable_test_files['docx'])
        
        base_error_message = r'Failed to load DOCX file: \[Errno 2\] No such file or directory: '
        expected_docx_file = unavailable_test_files['docx']  # Get the PDF file name

        with pytest.raises(ValueError, match=f'{base_error_message}.*{expected_docx_file}'):
            
            docx_loader.validate_file()
            docx_loader.load_file()

    def test_load_pdf_raises_file_not_found_error(self, unavailable_test_files):
        # Step 1: Create an instance of PDFLoader
        pptx_loader = PPTLoader(unavailable_test_files['pptx'])
        
        base_error_message = r'Failed to load the PPTX file: \[Errno 2\] No such file or directory: '
        expected_pptx_file = unavailable_test_files['pptx']  # Get the PDF file name

        with pytest.raises(ValueError, match=f'{base_error_message}.*{expected_pptx_file}'):
            
            pptx_loader.validate_file()
            pptx_loader.load_file()