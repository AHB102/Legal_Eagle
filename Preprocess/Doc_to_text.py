import fitz 
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def document_to_text(document):
    verdict_doc = document

    with fitz.open(verdict_doc) as doc:
        text = ''
        for page in doc:
             c_text = page.get_text()
             c_text = c_text.replace('\n', ' ')
             text += c_text

    return text

def chunking(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 5000, chunk_overlap = 20)
    chunks = text_splitter.create_documents([text])
    return chunks