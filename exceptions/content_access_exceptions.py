# exceptions.py
class ContentAccessError(Exception):
    """Exception raised when content access verification fails for a loaded document."""
    def __init__(self, message="Failed to access document content."):
        super().__init__(message)
