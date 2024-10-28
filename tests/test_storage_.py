import pytest
from storage.file_storage import FileStorage
from storage.sql_storage import SQLStorage
from extractors.data_extractor import DataExtractor
from loaders.pdf_loader import PDFLoader

@pytest.fixture
def file_storage(tmp_path):
    extractor = DataExtractor(PDFLoader("sample_file.pdf"))
    return FileStorage(extractor, tmp_path)

@pytest.fixture
def sql_storage():
    extractor = DataExtractor(PDFLoader("sample_file.pdf"))
    return SQLStorage(extractor, db_url="sqlite:///:memory:")

class TestStorage:

    def test_file_storage_saves_text(self, file_storage):
        """Test that FileStorage saves text correctly."""
        file_storage.save_text()
        text_file = file_storage.directory / "text.txt"
        assert text_file.exists(), "Text file was not created."
        
        with open(text_file, "r") as f:
            content = f.read()
            assert "Sample Text" in content, "Sample Text was not found in the saved file."

    def test_sql_storage_saves_data(self, sql_storage):
        """Test that SQLStorage saves data correctly."""
        sql_storage.save_text()
        # Assuming a method `fetch_saved_text()` to check data in SQL
        assert sql_storage.fetch_saved_text() == "Sample Text", "Saved text in SQL does not match."

if __name__ == "__main__":
    pytest.main()