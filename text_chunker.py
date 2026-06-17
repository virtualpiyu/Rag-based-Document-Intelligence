from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text: str):
    """
    Split text into overlapping chunks for better context retrieval.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=500
    )
    return splitter.split_text(text)
