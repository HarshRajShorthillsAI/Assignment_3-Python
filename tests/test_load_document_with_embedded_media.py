import os
import pytest
from loaders.docx_loader import DOCXLoader  # Update import paths as per your project structure
from loaders.ppt_loader import PPTLoader
from loaders.pdf_loader import PDFLoader

class TestFileWithEmbeddedMedia:

    @classmethod
    def setup_class(cls):     
        # Path to the file with embedded media
        cls.media_pdf_path = "test_files/media_file_with_embedded_content.pdf"  # Update this path accordingly
        cls.media_docx_path = "test_files/media_file_with_embedded_content.docx"  # Update this path accordingly
        cls.media_pptx_path = "test_files/media_file_with_embedded_content.pptx"  # Update this path accordingly

    def test_load_pdf_with_embedded_media(self):
        # Precondition: Verify that the media file exists
        assert os.path.exists(self.media_pdf_path), "The file with embedded media does not exist."

        try:
            pdf_loader = PDFLoader(self.media_file_path)

            # Load the file
            pdf_document = pdf_loader.load_file()

            # Verify that the text content was extracted successfully
            extracted_text = pdf_document[0].get_text()  # Assuming `extract_text` is a method to get all text content
            assert extracted_text is not None, "No text content could be extracted from the file with embedded media."
            assert len(extracted_text) > 0, "Extracted text content is empty, which is unexpected."

        except Exception as e:
            pytest.fail(f"An error occurred while loading the file with embedded media: {e}")
