import pptx
from loaders.file_loader import FileLoader

class PPTLoader(FileLoader):
    def validate_file(self):
        if not self.file_path.endswith('.pptx'):
            raise ValueError("Invalid file type. Expected a PPT file.")

    def load_file(self):
        return pptx.Presentation(self.file_path)