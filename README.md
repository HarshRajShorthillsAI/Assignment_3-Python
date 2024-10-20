# Assignment_3-Python
Extract Text, Links, Images, and Tables from PDF, DOCX, and PPT with Metadata

# Data Extraction Tool

This tool provides functionality to extract text, images, tables, and URLs from various document formats (PDF, DOCX, and PPTX).

## Functionalities

- [x] Text
- [x] Image
- [ ] Table      PDF
- [ ] Link

- [x] Text
- [x] Image
- [ ] Table     DOCX
- [ ] Link

- [x] Text
- [x] Image
- [ ] Table     PPTX
- [ ] Link

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
