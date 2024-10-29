import pptx
import msoffcrypto
import io
from loaders.file_loader import FileLoader

class PPTLoader(FileLoader):
    def __init__(self, file_path, password=None):
        super().__init__(file_path, password)

    def validate_file(self):
        if not self.file_path.endswith('.pptx'):
            raise ValueError("Invalid file type. Expected a PPT file.")

    def load_file(self):
        """Attempt to load the PPTX file, handling decryption if necessary."""
        try:
            # Check if the file is encrypted
            with open(self.file_path, "rb") as file:
                office_file = msoffcrypto.OfficeFile(file)
                
                # If the file is encrypted, handle decryption
                if office_file.is_encrypted():
                    if self.password is None:
                        raise ValueError("The PPTX file is password-protected. A password is required to open it.")

                    # Load the key with the correct password
                    office_file.load_key(password=self.password)

                    # Decrypt the file into a BytesIO object
                    decrypted_file = io.BytesIO()
                    office_file.decrypt(decrypted_file)
                    decrypted_file.seek(0)  # Reset pointer to the start of the in-memory file

                    # Load the decrypted PPTX from the in-memory file
                    pptx_document = pptx.Presentation(decrypted_file)

                else:
                    # If the file is not encrypted, load it directly
                    pptx_document = pptx.Presentation(file)

                return pptx_document

        except Exception as e:
            raise ValueError(f"Failed to load the PPTX file: {e}")

    def get_metadata(self):
        ppt = self.load_file()
        core_props = ppt.core_properties

        metadata_dict = {prop: getattr(core_props, prop) for prop in dir(core_props) if not prop.startswith("_") and not callable(getattr(core_props, prop))}
        return metadata_dict
    
    def get_fileType(self):
        return super().get_fileType()