# # from langchain_google_genai import ChatGoogleGenerativeAI
# from google import genai
# # from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_classic.chains import RetrievalQA

# def create_rag_chain(vectorstore):
#     """
#     Create Retrieval-Augmented Generation chain.
#     """

#     prompt = PromptTemplate(
#         input_variables=["context", "question"],
#         template="""
# You are an educational AI assistant.
# Answer the question strictly using the given context.
# If the answer is not present in the context, respond with:
# "Information not available in the provided study material."

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
#     )
#     llm = genai.Client()  # Initialize Gemini client (API key should be set in environment variable)

#     response = llm.generate_content(
#     model="gemini-3-pro", # Specify the model version
#     contents="Explain how AI works in a few words"
# )
#     # print(response.text)

#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
#         chain_type_kwargs={"prompt": prompt},
#         return_source_documents=True
#     )

#     return qa_chain



from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA


def create_rag_chain(vectorstore):
    """
    Create Retrieval-Augmented Generation chain.
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an educational AI assistant.
Answer the question strictly using the given context.
If the answer is not present in the context, respond with:
"Information not available in the provided study material."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    # Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1
    )

    # RAG Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return qa_chain