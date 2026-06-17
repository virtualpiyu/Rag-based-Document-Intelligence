# # import streamlit as st
# # import os

# # from modules.document_loader import load_pdf

# # from modules.embeddings import get_embeddings
# # from modules.vector_db import save_to_faiss, load_faiss
# # from modules.rag_pipeline import create_rag_chain

# # st.set_page_config(page_title="Educational AI Assistant", layout="wide")

# # st.title("📘 Educational RAG-Based AI Assistant")

# # uploaded_file = st.file_uploader("Upload Study Material (PDF)", type=["pdf"])

# # if uploaded_file:
# #     file_path = f"data/documents/{uploaded_file.name}"
# #     with open(file_path, "wb") as f:
# #         f.write(uploaded_file.getbuffer())

# #     text = load_pdf(file_path)
# #     chunks = chunk_text(text)
# #     embeddings = get_embeddings()
# #     save_to_faiss(chunks, embeddings)

# #     st.success("Document indexed successfully!")

# # st.divider()

# # question = st.text_input("Ask a question from your study material")

# # if question:
# #     embeddings = get_embeddings()
# #     db = load_faiss(embeddings)

# #     if db:
# #         rag_chain = create_rag_chain(db)
# #         response = rag_chain.run(question)
# #         st.write("### Answer")
# #         st.write(response)
# #     else:
# #         st.warning("Please upload documents first.")











# import streamlit as st
# import os
# from Document_loader import load_pdf
# from text_chunker import chunk_text
# from embedding import get_embedding_model

# # st.set_page_config(page_title="Educational RAG-Based AI Assistant", layout="wide")

# # st.title("📘 Educational RAG-Based AI Assistant")

# # UPLOAD_DIR = "data/documents"
# # os.makedirs(UPLOAD_DIR, exist_ok=True)

# # uploaded_file = st.file_uploader(
# #     "Upload your study material (PDF & Text Extractable images only)",
# #     type=["pdf","png","jpg","jpeg"]
# # )

# # if uploaded_file:
# #     file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

# #     with open(file_path, "wb") as f:
# #         f.write(uploaded_file.getbuffer())

# #     st.success("PDF uploaded successfully.")

# #     with st.spinner("Extracting text from document..."):
# #         extracted_text = load_pdf(file_path)

# #     st.subheader("Extracted Text Preview")
# #     st.text(extracted_text[:2000])  # preview only


# from vector_db import create_and_save_vectorstore, load_vectorstore

# st.set_page_config(page_title="Educational RAG-Based AI Assistant", layout="wide")
# st.title("📘 Educational RAG-Based AI Assistant")

# UPLOAD_DIR = "data/documents"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# uploaded_file = st.file_uploader("Upload study material (PDF)", type=["pdf"])

# embedding_model = get_embedding_model()

# if uploaded_file:
#     file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     st.success("PDF uploaded successfully.")

#     text = load_pdf(file_path)
#     chunks = chunk_text(text)

#     st.write(f"Total chunks created: {len(chunks)}")

#     with st.spinner("Creating vector database..."):
#         create_and_save_vectorstore(chunks, embedding_model)

#     st.success("Document indexed into FAISS vector database.")

# st.divider()

# st.subheader("🔍 Similarity Search Test")

# query = st.text_input("Enter a test query (no AI answer yet)")

# if query:
#     db = load_vectorstore(embedding_model)

#     if db:
#         results = db.similarity_search(query, k=3)

#         st.write("Top matching chunks:")
#         for i, doc in enumerate(results, 1):
#             st.markdown(f"**Result {i}:**")
#             st.text(doc.page_content[:500])
#     else:
#         st.warning("Please upload and index a document first.")









import streamlit as st
import os

from Document_loader import load_pdf
from text_chunker import chunk_text
from embedding import get_embedding_model
from vector_db import create_and_save_vectorstore, load_vectorstore
from rag_pipeline import create_rag_chain

st.set_page_config(page_title="Educational RAG-Based AI Assistant", layout="wide")
st.title("📘 Educational RAG-Based AI Assistant")

UPLOAD_DIR = "data/documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)

embedding_model = get_embedding_model()

# ------------------ DOCUMENT UPLOAD ------------------
# st.header("📂 Upload Study Material")

# uploaded_file = st.file_uploader("Upload PDF document", type=["pdf"])

# if uploaded_file:
#     file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     text = load_pdf(file_path)
#     chunks = chunk_text(text)

#     with st.spinner("Indexing document..."):
#         create_and_save_vectorstore(chunks, embedding_model)

#     st.success("Document indexed successfully!")

# ------------------ DOCUMENT UPLOAD ------------------
st.header("📂 Upload Study Material")

uploaded_file = st.file_uploader("Upload PDF document", type=["pdf"])

if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = load_pdf(file_path)

    # DEBUG: check extracted text
    print("EXTRACTED TEXT SAMPLE:\n", text[:1000])
    st.write(text[:500])   # optional: show in UI

    chunks = chunk_text(text)

    with st.spinner("Indexing document..."):
        create_and_save_vectorstore(chunks, embedding_model)

    st.success("Document indexed successfully!")

#  QUESTION ANSWERING 
st.divider()
st.header("💬 Ask a Question")

question = st.text_input("Ask a question from the uploaded material")

if question:
    vectorstore = load_vectorstore(embedding_model)

    if vectorstore:
        qa_chain = create_rag_chain(vectorstore)

        with st.spinner("Generating answer..."):
            response = qa_chain(question)

        st.subheader("Answer")
        st.write(response["result"])

        with st.expander("📄 Source Chunks"):
            for i, doc in enumerate(response["source_documents"], 1):
                st.markdown(f"**Source {i}:**")
                st.text(doc.page_content[:500])

    else:
        st.warning("Please upload a document first.")
