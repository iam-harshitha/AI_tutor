from PyPDF2 import PdfReader
from typing import List

def extract_text_from_pdf(pdf_path: str) -> List[str]:
    """
    Extracts text from a PDF and returns a list of pages.
    Each page is a separate string in the list.
    """
    reader = PdfReader(pdf_path)
    pages = []
    
    for page in reader.pages:
        text = page.extract_text()
        if text:  # Only add non-empty pages
            pages.append(text)
    
    return pages

def chunk_text(pages: List[str], chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Splits the text into chunks with optional overlap.
    """
    chunks = []
    
    for page in pages:
        words = page.split()
        for i in range(0, len(words), chunk_size - overlap):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
    
    return chunks