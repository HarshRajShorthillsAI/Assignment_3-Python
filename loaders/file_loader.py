from abc import ABC, abstractmethod

class FileLoader(ABC):
    def __init__(self, file_path=None, password=None):
        self.file_path = file_path
        self.password = password

    @abstractmethod
    def validate_file(self):
        pass

    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def get_metadata(self):
        pass

    @abstractmethod
    def verify_content(self, Document):
        pass

    @abstractmethod
    def get_fileType(self):
        if self.file_path.endswith('pdf'):
            return "pdf"
        elif self.file_path.endswith('docx'):
            return "docx"
        elif self.file_path.endswith('pptx'):
            return "pptx"
        else:
            raise ValueError("Unsupported file format for text extraction.")