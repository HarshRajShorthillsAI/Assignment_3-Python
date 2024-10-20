import pytest
from loaders.pdf_loader import PDFLoader
from extractors.data_extractor import DataExtractor

class TestPDFExtractor:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Fixture to set up the PDFLoader and DataExtractor instances."""
        self.loader = PDFLoader('tests/test_files/dir2/lecs110.pdf')  # Ensure this file exists
        self.extractor = DataExtractor(self.loader)

    def test_pdf_extraction(self):
        """Test PDF data extraction."""
        text_data = self.extractor.extract_text()
        assert len(text_data) > 0, "No text extracted from the PDF."

if __name__ == '__main__':
    pytest.main()


# class TestDataExtractor:

#     @pytest.fixture(autouse=True)
#     def setup(self, pdf_loader, docx_loader, ppt_loader):
#         """Setup fixtures for PDF, DOCX, and PPT loaders."""
#         self.pdf_extractor = pdf_loader
#         self.docx_extractor = docx_loader
#         self.ppt_extractor = ppt_loader

#     def test_extract_text_pdf(self):
#         """Test text extraction from a valid PDF."""
#         text = self.pdf_extractor.extract_text()
#         assert text is not None, "Text extraction returned None."
#         assert "Sample Text" in text, "Expected text not found in the extracted text."

#     def test_extract_text_docx(self):
#         """Test text extraction from a valid DOCX."""
#         text = self.docx_extractor.extract_text()
#         assert text is not None, "Text extraction returned None."
#         assert "Sample Text" in text, "Expected text not found in the extracted text."

#     def test_extract_text_ppt(self):
#         """Test text extraction from a valid PPT."""
#         text = self.ppt_extractor.extract_text()
#         assert text is not None, "Text extraction returned None."
#         assert "Sample Text" in text, "Expected text not found in the extracted text."

#     @pytest.mark.parametrize("extractor", ["pdf_extractor", "docx_extractor", "ppt_extractor"])
#     def test_extract_links(self, request, extractor):
#         """Test link extraction from various file types."""
#         extractor_instance = request.getfixturevalue(extractor)
#         links = extractor_instance.extract_links()
#         assert links is not None, "Links extraction returned None."
#         assert len(links) > 0, "No links extracted from the document."

#     def test_extract_images_pdf(self):
#         """Test image extraction from a valid PDF."""
#         images = self.pdf_extractor.extract_images()
#         assert images is not None, "Image extraction returned None."
#         assert len(images) > 0, "No images extracted from the PDF."

#     def test_extract_images_docx(self):
#         """Test image extraction from a valid DOCX."""
#         images = self.docx_extractor.extract_images()
#         assert images is not None, "Image extraction returned None."
#         assert len(images) > 0, "No images extracted from the DOCX."

#     def test_extract_images_ppt(self):
#         """Test image extraction from a valid PPT."""
#         images = self.ppt_extractor.extract_images()
#         assert images is not None, "Image extraction returned None."
#         assert len(images) > 0, "No images extracted from the PPT."

#     def test_extract_tables_pdf(self):
#         """Test table extraction from a valid PDF."""
#         tables = self.pdf_extractor.extract_tables()
#         assert tables is not None, "Table extraction returned None."
#         assert len(tables) > 0, "No tables extracted from the PDF."

#     def test_extract_tables_docx(self):
#         """Test table extraction from a valid DOCX."""
#         tables = self.docx_extractor.extract_tables()
#         assert tables is not None, "Table extraction returned None."
#         assert len(tables) > 0, "No tables extracted from the DOCX."

#     def test_extract_tables_ppt(self):
#         """Test table extraction from a valid PPT."""
#         tables = self.ppt_extractor.extract_tables()
#         assert tables is not None, "Table extraction returned None."
#         assert len(tables) > 0, "No tables extracted from the PPT."


# if __name__ == "__main__":
#     pytest.main()
