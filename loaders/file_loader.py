from abc import ABC, abstractmethod

class FileLoader(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def validate_file(self):
        pass

    @abstractmethod
    def load_file(self):
        pass