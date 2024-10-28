import pytest
from loaders.pdf_loader import PDFLoader

@pytest.fixture
def pdf_loader():
    """Fixture for creating a PDFLoader instance with a valid sample file."""
    return PDFLoader("sample_file.pdf")

class TestPDFLoader:
    
    def test_pdf_loader_loads_file(self, pdf_loader):
        """Test the valid file loading."""
        assert pdf_loader.load_file() is not None

    def test_pdf_loader_invalid_file(self):
        """Test invalid file loading."""
        loader = PDFLoader("non_existent_file.pdf")
        with pytest.raises(FileNotFoundError):
            loader.load_file()

if __name__ == "__main__":
    pytest.main()
