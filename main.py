import streamlit as st
from Preprocess.Doc_to_text import document_to_text, chunking

def process_document(document):
    st.write("Processing Document")
    filtered_content = document.read()
    filtered_text = document_to_text(filtered_content)
    chunks = chunking(filtered_text)
    return chunks


uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None :
    st.write("Not None")
    chunks = process_document(uploaded_file)
    st.text(chunks)
# process_document(uploaded_file)


