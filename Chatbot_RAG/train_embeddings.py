from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import time

persist_directory = "./docs/chroma"
oembeddings = OllamaEmbeddings(model="mxbai-embed-large:335m")

pdf_files = [f for f in os.listdir("./pdf/") if f.endswith(".pdf")]
txt_files = [f for f in os.listdir("./pdf/") if f.endswith(".txt")]
pdf_loader = [PyPDFLoader("./pdf/"+i) for i in pdf_files]
txt_loader = [TextLoader("./pdf/"+i) for i in txt_files]

docs = []
for loader in pdf_loader + txt_loader:
    docs.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150, add_start_index=True)
splits = text_splitter.split_documents(docs)

vectordb = Chroma.from_documents(
    documents=splits,
    embedding=oembeddings,
    persist_directory=persist_directory
)
print("Database updated successfully!") 