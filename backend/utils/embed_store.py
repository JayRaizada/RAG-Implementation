from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def store_embeddings(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)  # Optimized for OpenAI
    
    # Split and extract content
    text_chunks = []
    for doc in docs:
        text_chunks.extend(splitter.split_text(doc.page_content))
    
    # Convert each chunk back to a Document
    final_docs = [doc.__class__(page_content=chunk) for chunk in text_chunks]

    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # or "text-embedding-3-large"
    
    print("Embedding has been done")
    return FAISS.from_documents(final_docs, embeddings)
