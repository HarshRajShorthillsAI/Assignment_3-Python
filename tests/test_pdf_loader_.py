from unittest.mock import patch
import pytest
from loaders.pdf_loader import PDFLoader
import os

# @pytest.fixture
# def pdf_loader():
#     """Fixture for creating a PDFLoader instance with a valid sample file."""
#     return PDFLoader("sample_file.pdf")

# class TestPDFLoader:
    
#     def test_pdf_loader_loads_file(self, pdf_loader):
#         """Test the valid file loading."""
#         assert pdf_loader.load_file() is not None

#     def test_pdf_loader_invalid_file(self):
#         """Test invalid file loading."""
#         loader = PDFLoader("non_existent_file.pdf")
#         with pytest.raises(FileNotFoundError):
#             loader.load_file()

# if __name__ == "__main__":
#     pytest.main()

class TestPDFLoader:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Set up test environment before each test method"""
        self.loader = PDFLoader()
        self.test_file_dir = "test_files"
        if not os.path.exists(self.test_file_dir):
            os.makedirs(self.test_file_dir)
        yield
        # Clean up after each test method
        if os.path.exists(self.test_file_dir):
            for file in os.listdir(self.test_file_dir):
                os.remove(os.path.join(self.test_file_dir, file))
            os.rmdir(self.test_file_dir)

    def test_load_valid_file(self):
        """TC_001: Test loading a valid PDF file"""
        test_file = os.path.join(self.test_file_dir, "valid.pdf")
        with open(test_file, 'wb') as f:
            f.write(b'%PDF-1.4\n')  # Minimal valid PDF content
        
        result = self.loader.load_file(test_file)
        assert result is not None
        assert hasattr(result, 'read')

    def test_load_max_size_file(self):
        """TC_002: Test loading a file at maximum allowed size"""
        max_size = 10 * 1024 * 1024  # 10MB example max size
        test_file = os.path.join(self.test_file_dir, "max_size.pdf")
        with open(test_file, 'wb') as f:
            f.write(b'%PDF-1.4\n' + b'0' * (max_size - 8))
        
        result = self.loader.load_file(test_file)
        assert result is not None

    def test_load_special_chars_filename(self):
        """TC_003: Test loading a file with special characters in filename"""
        test_file = os.path.join(self.test_file_dir, "test@file#1.pdf")
        with open(test_file, 'wb') as f:
            f.write(b'%PDF-1.4\n')
        
        result = self.loader.load_file(test_file)
        assert result is not None

    def test_load_password_protected(self):
        """TC_005: Test loading a password-protected PDF"""
        with patch('PDFLoader.get_password', return_value='correctpassword'):
            result = self.loader.load_file("password_protected.pdf")
            assert result is not None
            assert self.loader.is_file_loaded(result)
