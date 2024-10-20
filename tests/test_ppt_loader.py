import pytest
from extractors.ppt_loader import PPTLoader

@pytest.fixture
def ppt_loader():
    """Fixture for creating a PPTLoader instance."""
    loader = PPTLoader("sample.pptx")  # Ensure this file exists
    yield loader
    # Teardown can be added here if needed

class TestPPTLoader:

    def test_validation(self, ppt_loader):
        """Test PPTLoader for file validation."""
        assert ppt_loader.validate_file(), "PPT file validation failed."

    def test_load_file(self, ppt_loader):
        """Test loading a PPT file."""
        ppt_loader.load_file()
        # Optionally, check for extracted data
        # For example: assert ppt_loader.get_text() is not None

    def test_extract_text(self, ppt_loader):
        """Test text extraction from PPT file."""
        ppt_loader.load_file()  # Ensure the file is loaded
        text = ppt_loader.get_text()  # Assume this method exists
        assert text is not None, "Text extraction returned None."
        assert len(text) > 0, "No text extracted from the PPT file."

    def test_extract_images(self, ppt_loader):
        """Test image extraction from PPT file."""
        ppt_loader.load_file()  # Ensure the file is loaded
        images = ppt_loader.extract_images()  # Assume this method exists
        assert images is not None, "Image extraction returned None."
        assert len(images) > 0, "No images extracted from the PPT file."

    def test_extract_tables(self, ppt_loader):
        """Test table extraction from PPT file."""
        ppt_loader.load_file()  # Ensure the file is loaded
        tables = ppt_loader.extract_tables()  # Assume this method exists
        assert tables is not None, "Table extraction returned None."
        assert len(tables) > 0, "No tables extracted from the PPT file."

if __name__ == "__main__":
    pytest.main()
