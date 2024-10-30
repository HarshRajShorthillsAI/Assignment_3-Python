# Assignment_3-Python
Extract Text, Links, Images, and Tables from PDF, DOCX, and PPT with Metadata

# Data Extraction Tool

This tool provides functionality to extract text, images, tables, and URLs from various document formats (PDF, DOCX, and PPTX).

## Functionalities

- [x] Text
- [x] Image
- [x] Table      PDF
- [x] Link

- [x] Text
- [x] Image
- [x] Table     DOCX
- [x] Link

- [x] Text
- [x] Image
- [x] Table     PPTX
- [x] Link

## Test cases with pytest covered
- [x] Load a valid file format.
- [x] Load a file till the maximum allowed size.
- [x] Load a file with special characters in the filename.
- [x] Load a file with UTF-8 encoding.
- [x] Load a file with password protected files
- [x] Load file with unusual text fonts and styles
- [ ] Load a file with embedded media (audio, video)
- [x] Load file with rotated pages
- [x] Load an unsupported file format.
- [x] Load a corrupted file.
- [ ] Load a file exceeding the maximum allowed size.
- [x] Load an empty file (0 bytes).
- [x] Test if load_file raises FileNotFoundError.
- [ ] Extract text from a file containing only text.
- [ ] Extract images from a file containing only images.
- [ ] Extract URLs from a file containing only URLs.
- [ ] Extract tables from a file containing only tables.
- [ ] Extract mixed content (text, images, URLs, tables) from a file.
- [ ] Extract formatted text and verify formatting is preserved.
- [ ] Attempt to extract content from a file with password protection
- [ ] Attempt to extract content from a file with password protection
- [ ] Handle files with partial data corruption (e.g., half-loaded images).
- [ ] Extract content from a password-protected or encrypted file.
- [ ] Handle files with broken or malformed structures (e.g., incomplete tables).
- [ ] Create a directory with the file's name.
- [ ] Save extracted text to the appropriate directory.
- [ ] Save images in the 'image' directory.
- [ ] Save tables in the 'table' directory.
- [ ] Save tables in the 'text' directory.
- [ ] Save tables in the 'url' directory.
- [ ] Attempt to save content to a non-existent directory.
- [ ] Handle scenarios where saving fails due to disk space limitations.
- [ ] Simulate a failure during directory creation (e.g., permissions issue).
- [ ] Attempt to save to the database when the connection is down.
- [ ] Handle error when storing to invalid SQL DB
- [ ] Perform an end-to-end test for loading, extracting, and storing mixed content.
- [ ] Process multiple files in a batch and verify all are correctly handled.
- [ ] Simulate an interruption during the extraction process.
- [ ] Verify rollback or cleanup occurs if saving fails after extraction.
- [ ] Validate metadata extraction from PDF of Images
- [ ] Validate metadata extraction from PDF of Tables
- [ ] Validate metadata extraction from PDF of Links
- [ ] Handle missing metadata in PDF

### Legend:

- [ ] Functionality not yet implemented
- [x] Functionality implemented

---

## Detailed Descriptions

### 1. **Text Extraction**
- Extracts all text from the provided files.
- Supports **PDF**, **DOCX**, and **PPTX** formats.

### 2. **Image Extraction**
- Extracts all images embedded in the document.
- Supports **PDF**, **DOCX**, and **PPTX** formats.

### 3. **Table Extraction**
- Extracts tables embedded within the document.
- Supports **PDF**, **DOCX**, and **PPTX** formats.

### 4. **URL Extraction**
- Extracts hyperlinks embedded in the document.
- Supports **PDF** and **DOCX** formats. **PPTX** extraction is limited.

---

### How to Use

1. Install the necessary dependencies:
   ```bash
   pip install fitz camelot-py docx pptx pillow
