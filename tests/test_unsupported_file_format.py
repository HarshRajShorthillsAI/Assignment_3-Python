import pytest

from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader


class TestLoadUnsupportedFileFormatLoader:
    @pytest.fixture
    def unsupported_files(self):
        # Paths to your large files
        return [
            'tests/test_files/SampleAudio_0.4mb.mp3'  # Replace with your actual path
        ]

    def test_load_unsupported_file_format_pptx_loader(self, unsupported_files):
        pptx_loader = PPTLoader(unsupported_files[0])
        # Assert that loading the unsupported file raises a ValueError
        with pytest.raises(ValueError, match="Invalid file type. Expected a PPTX file."):
            pptx_loader.validate_file()
            pptx_loader.load_file()

    def test_load_unsupported_file_format_docx_loader(self, unsupported_files):
        docx_loader = DOCXLoader(unsupported_files[0])
        # Assert that loading the unsupported file raises a ValueError
        with pytest.raises(ValueError, match="Invalid file type. Expected a DOCX file."):
            docx_loader.validate_file()
            docx_loader.load_file()

    def test_load_unsupported_file_format_pdf_loader(self, unsupported_files):
        pdf_loader = PDFLoader(unsupported_files[0])
        # Assert that loading the unsupported file raises a ValueError
        with pytest.raises(ValueError, match="Invalid file type. Expected a PDF file."):
            pdf_loader.validate_file()
            pdf_loader.load_file()