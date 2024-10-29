import pytest
from unittest.mock import MagicMock
from extractors.data_extractor import DataExtractor


# @pytest.fixture
# def mock_loader():
#     """Fixture for a mock loader object."""
#     loader = MagicMock()
#     return loader


# @pytest.fixture
# def data_extractor(mock_loader):
#     """Fixture to create a DataExtractor instance."""
#     return DataExtractor(mock_loader)


# class TestDataExtractor:

#     def test_extract_text_pdf(self, data_extractor, mock_loader):
#         """Test text extraction from a PDF file."""
#         mock_loader.file_path = "sample.pdf"
#         mock_loader.load_file.return_value = MagicMock(pages=[
#             MagicMock(extract_text=MagicMock(return_value="Sample text from PDF."))
#         ])

#         result = data_extractor.extract_text()
#         assert result == "Sample text from PDF."

#     def test_extract_text_docx(self, data_extractor, mock_loader):
#         """Test text extraction from a DOCX file."""
#         mock_loader.file_path = "sample.docx"
#         mock_loader.load_file.return_value = MagicMock(paragraphs=[
#             MagicMock(text="Sample text from DOCX.")
#         ])

#         result = data_extractor.extract_text()
#         assert result == "Sample text from DOCX.\n"

#     def test_extract_text_pptx(self, data_extractor, mock_loader):
#         """Test text extraction from a PPTX file."""
#         mock_loader.file_path = "sample.pptx"
#         mock_loader.load_file.return_value = MagicMock(slides=[
#             MagicMock(shapes=[
#                 MagicMock(text="Text from slide 1"),
#                 MagicMock(text="Text from slide 2")
#             ])
#         ])

#         result = data_extractor.extract_text()
#         assert result == "Text from slide 1\nText from slide 2\n"

#     def test_extract_images_pdf(self, data_extractor, mock_loader):
#         """Test image extraction from a PDF file."""
#         mock_loader.file_path = "sample.pdf"
#         mock_loader.load_file.return_value = MagicMock()
#         mock_loader.load_file.return_value.pages = [
#             MagicMock(get_images=MagicMock(return_value=[(0, 0, 0, 0, 0, 0)]))
#         ]
#         mock_loader.load_file.return_value.extract_image = MagicMock(return_value={
#             "image": b"sample_image_data",
#             "ext": "png",
#             "width": 100,
#             "height": 100
#         })

#         result = data_extractor.extract_images()
#         assert len(result) == 1
#         assert result[0]["image_data"] == b"sample_image_data"
#         assert result[0]["ext"] == "png"
#         assert result[0]["dimensions"] == (100, 100)

#     def test_extract_images_docx(self, data_extractor, mock_loader):
#         """Test image extraction from a DOCX file."""
#         mock_loader.file_path = "sample.docx"
#         mock_loader.load_file.return_value = MagicMock(part=MagicMock(rels={
#             "image_id": MagicMock(target_part=MagicMock(blob=b"sample_image_data"))
#         }))

#         result = data_extractor.extract_images()
#         assert len(result) == 1
#         assert result[0]["image_data"] == b"sample_image_data"

#     def test_extract_images_pptx(self, data_extractor, mock_loader):
#         """Test image extraction from a PPTX file."""
#         mock_loader.file_path = "sample.pptx"
#         mock_loader.load_file.return_value = MagicMock(slides=[
#             MagicMock(shapes=[
#                 MagicMock(shape_type=0, image=MagicMock(blob=b"sample_image_data", ext="png"))
#             ])
#         ])

#         result = data_extractor.extract_images()
#         assert len(result) == 1
#         assert result[0]["image_data"] == b"sample_image_data"
#         assert result[0]["ext"] == "png"

#     def test_extract_urls_pdf(self, data_extractor, mock_loader):
#         """Test URL extraction from a PDF file."""
#         mock_loader.file_path = "sample.pdf"
#         mock_loader.load_file.return_value = MagicMock(pages=[
#             MagicMock(get_links=MagicMock(return_value=[
#                 {"uri": "http://example.com", "from": MagicMock(x0=0, y0=0, x1=0, y1=0)}
#             ]))
#         ])

#         result = data_extractor.extract_urls()
#         assert len(result) == 1
#         assert result[0]["url"] == "http://example.com"

#     def test_extract_urls_docx(self, data_extractor, mock_loader):
#         """Test URL extraction from a DOCX file."""
#         mock_loader.file_path = "sample.docx"
#         mock_loader.load_file.return_value = MagicMock(part=MagicMock(rels={
#             "hyperlink_id": MagicMock(reltype="http://example.com")
#         }))

#         result = data_extractor.extract_urls()
#         assert len(result) == 1
#         assert result[0]["url"] == "http://example.com"

#     def test_extract_urls_pptx(self, data_extractor, mock_loader):
#         """Test URL extraction from a PPTX file."""
#         mock_loader.file_path = "sample.pptx"
#         mock_loader.load_file.return_value = MagicMock(slides=[
#             MagicMock(shapes=[
#                 MagicMock(has_text_frame=True, text_frame=MagicMock(paragraphs=[
#                     MagicMock(runs=[MagicMock(hyperlink=MagicMock(address="http://example.com"))])
#                 ]))
#             ])
#         ])

#         result = data_extractor.extract_urls()
#         assert len(result) == 1
#         assert result[0]["url"] == "http://example.com"

#     def test_extract_tables_pdf(self, data_extractor, mock_loader):
#         """Test table extraction from a PDF file."""
#         mock_loader.file_path = "sample.pdf"
#         mock_loader.load_file.return_value = MagicMock()
#         mock_loader.load_file.return_value.pages = [
#             MagicMock(get_images=MagicMock(return_value=[]))
#         ]

#         result = data_extractor.extract_tables()
#         assert len(result) == 0  # Adjust based on your expectation

#     def test_extract_tables_docx(self, data_extractor, mock_loader):
#         """Test table extraction from a DOCX file."""
#         mock_loader.file_path = "sample.docx"
#         mock_loader.load_file.return_value = MagicMock(tables=[
#             MagicMock(rows=[
#                 MagicMock(cells=[MagicMock(text='Header1'), MagicMock(text='Header2')]),
#                 MagicMock(cells=[MagicMock(text='Row1Col1'), MagicMock(text='Row1Col2')])
#             ])
#         ])

#         result = data_extractor.extract_tables()
#         assert len(result) == 1
#         assert result[0] == [['Header1', 'Header2'], ['Row1Col1', 'Row1Col2']]

#     def test_extract_tables_pptx(self, data_extractor, mock_loader):
#         """Test table extraction from a PPTX file."""
#         mock_loader.file_path = "sample.pptx"
#         mock_loader.load_file.return_value = MagicMock(slides=[
#             MagicMock(shapes=[
#                 MagicMock(has_text_frame=True, table=MagicMock(rows=[
#                     MagicMock(cells=[MagicMock(text='Header1'), MagicMock(text='Header2')]),
#                     MagicMock(cells=[MagicMock(text='Row1Col1'), MagicMock(text='Row1Col2')])
#                 ]))
#             ])
#         ])

#         result = data_extractor.extract_tables()
#         assert len(result) == 1
#         assert result[0] == [['Header1', 'Header2'], ['Row1Col1', 'Row1Col2']]

class TestPDFExtractor:
    @pytest.fixture(autouse=True)
    def setup(self, pdf_loader):
        """Set up PDFExtractor with PDFLoader"""
        self.extractor = DataExtractor.PDFExtractor()
        self.loader = pdf_loader

    def test_extract_text_only(self):
        """TC_014: Test extracting text from text-only PDF"""
        pdf_content = self.loader.load_file("text_only.pdf")
        result = self.extractor.extract_text(pdf_content)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_extract_images_only(self):
        """TC_015: Test extracting images from image-only PDF"""
        pdf_content = self.loader.load_file("images_only.pdf")
        images = self.extractor.extract_images(pdf_content)
        assert isinstance(images, list)
        assert len(images) > 0

    def test_extract_mixed_content(self):
        """TC_018: Test extracting mixed content"""
        pdf_content = self.loader.load_file("mixed_content.pdf")
        result = self.extractor.extract_all_content(pdf_content)
        assert 'text' in result
        assert 'images' in result
        assert 'tables' in result
        assert 'urls' in result
