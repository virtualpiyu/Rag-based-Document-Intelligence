import os
from langchain_community.vectorstores import FAISS

VECTORSTORE_PATH = "vectorstore/faiss_index"

def create_and_save_vectorstore(chunks, embedding_model):
    """
    Create FAISS vector store from text chunks and save locally.
    """
    db = FAISS.from_texts(chunks, embedding_model)
    db.save_local(VECTORSTORE_PATH)
    return db

def load_vectorstore(embedding_model):
    """
    Load FAISS vector store from disk.
    """
    if os.path.exists(VECTORSTORE_PATH):
        return FAISS.load_local(
            VECTORSTORE_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )
    return None
