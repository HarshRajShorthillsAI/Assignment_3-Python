import pytest
from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader
from loaders.ppt_loader import PPTLoader
from storage.file_storage import FileStorage
from storage.sql_storage import SQLStorage
from data_extractor import DataExtractor

@pytest.fixture
def pdf_loader():
    # Fixture for PDFLoader with a sample file
    return PDFLoader("sample_file.pdf")

@pytest.fixture
def docx_loader():
    # Fixture for DOCXLoader with a sample file
    return DOCXLoader("sample_file.docx")

@pytest.fixture
def ppt_loader():
    # Fixture for PPTLoader with a sample file
    return PPTLoader("sample_file.ppt")

@pytest.fixture
def pdf_extractor(pdf_loader):
    # Fixture for DataExtractor initialized with PDFLoader
    return DataExtractor(pdf_loader)

@pytest.fixture
def docx_extractor(docx_loader):
    # Fixture for DataExtractor initialized with DOCXLoader
    return DataExtractor(docx_loader)

@pytest.fixture
def ppt_extractor(ppt_loader):
    # Fixture for DataExtractor initialized with PPTLoader
    return DataExtractor(ppt_loader)

@pytest.fixture
def file_storage(tmp_path, pdf_extractor):
    # Fixture for FileStorage, using temporary path and PDF extractor
    return FileStorage(pdf_extractor, tmp_path)

@pytest.fixture
def sql_storage():
    # Fixture for SQLStorage, using an in-memory SQLite database
    return SQLStorage(DataExtractor(PDFLoader("sample_file.pdf")), db_url="sqlite:///:memory:")
