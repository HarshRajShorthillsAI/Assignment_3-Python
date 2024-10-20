import pytest
from extractors.docx_loader import DOCXLoader
from extractors.pdf_loader import PDFLoader
from extractors.ppt_loader import PPTLoader

@pytest.fixture
def pdf_loader():
    """Fixture for creating a PDFLoader instance."""
    loader = PDFLoader("sample.pdf")
    yield loader
    # Teardown can be added here if needed

@pytest.fixture
def docx_loader():
    """Fixture for creating a DOCXLoader instance."""
    loader = DOCXLoader("sample.docx")
    yield loader
    # Teardown can be added here if needed

@pytest.fixture
def ppt_loader():
    """Fixture for creating a PPTLoader instance."""
    loader = PPTLoader("sample.pptx")
    yield loader
    # Teardown can be added here if needed

class TestPDFLoader:
    
    def test_pdf_loader(self, pdf_loader):
        """Test PDFLoader for validation and loading."""
        assert pdf_loader.validate_file(), "PDF file validation failed."
        pdf_loader.load_file()
        # Optionally, check for extracted data
        # For example: assert pdf_loader.get_text() is not None

class TestDOCXLoader:
    
    def test_docx_loader(self, docx_loader):
        """Test DOCXLoader for validation and loading."""
        assert docx_loader.validate_file(), "DOCX file validation failed."
        docx_loader.load_file()
        # Optionally, check for extracted data
        # For example: assert docx_loader.get_text() is not None

class TestPPTLoader:
    
    def test_ppt_loader(self, ppt_loader):
        """Test PPTLoader for validation and loading."""
        assert ppt_loader.validate_file(), "PPT file validation failed."
        ppt_loader.load_file()
        # Optionally, check for extracted data
        # For example: assert ppt_loader.get_text() is not None

if __name__ == "__main__":
    pytest.main()
