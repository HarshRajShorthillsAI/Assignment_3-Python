# test_file_loading.py
import os
import pytest
from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader

class TestFileLoading:
    def test_file_exists(self):
        """Verify the presence of valid files in the test_files directory."""
        file_paths = [
            "tests/test_files/Class Jan 2018.pptx",
            "tests/test_files/unit 5.docx",
            "tests/test_files/llm_training.pdf"
        ]
        for file_path in file_paths:
            assert os.path.isfile(file_path), f"File {file_path} does not exist."

    def test_pptx_file_validation(self):
        """Test if PPTLoader validates .pptx file correctly."""
        loader = PPTLoader("tests/test_files/Class Jan 2018.pptx")
        loader.validate_file()  # Should not raise an error

    def test_docx_file_validation(self):
        """Test if DOCXLoader validates .docx file correctly."""
        loader = DOCXLoader("tests/test_files/unit 5.docx")
        loader.validate_file()  # Should not raise an error

    def test_pdf_file_validation(self):
        """Test if PDFLoader validates .pdf file correctly."""
        loader = PDFLoader("tests/test_files/llm_training.pdf")
        loader.validate_file()  # Should not raise an error

    def test_pptx_file_loading(self):
        """Test if PPTLoader loads the .pptx file without issues."""
        loader = PPTLoader("tests/test_files/Class Jan 2018.pptx")
        loader.validate_file()
        loaded_file = loader.load_file()
        assert loaded_file is not None, "Failed to load .pptx file."

    def test_docx_file_loading(self):
        """Test if DOCXLoader loads the .docx file without issues."""
        loader = DOCXLoader("tests/test_files/unit 5.docx")
        loader.validate_file()
        loaded_file = loader.load_file()
        assert loaded_file is not None, "Failed to load .docx file."

    def test_pdf_file_loading(self):
        """Test if PDFLoader loads the .pdf file without issues."""
        loader = PDFLoader("tests/test_files/llm_training.pdf")
        loader.validate_file()
        loaded_file = loader.load_file()
        assert loaded_file is not None, "Failed to load .pdf file."

    def test_pptx_metadata_retrieval(self):
        """Test if PPTLoader retrieves metadata for .pptx file."""
        loader = PPTLoader("tests/test_files/Class Jan 2018.pptx")
        loader.validate_file()
        metadata = loader.get_metadata()
        assert isinstance(metadata, dict), "Metadata should be a dictionary."
        assert len(metadata) > 0, "Metadata dictionary should not be empty."

    def test_docx_metadata_retrieval(self):
        """Test if DOCXLoader retrieves metadata for .docx file."""
        loader = DOCXLoader("tests/test_files/unit 5.docx")
        loader.validate_file()
        metadata = loader.get_metadata()
        assert isinstance(metadata, dict), "Metadata should be a dictionary."
        assert len(metadata) > 0, "Metadata dictionary should not be empty."

    def test_pdf_metadata_retrieval(self):
        """Test if PDFLoader retrieves metadata for .pdf file."""
        loader = PDFLoader("tests/test_files/llm_training.pdf")
        loader.validate_file()
        metadata = loader.get_metadata()
        assert isinstance(metadata, dict), "Metadata should be a dictionary."
        assert len(metadata) > 0, "Metadata dictionary should not be empty."