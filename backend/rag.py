from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from backend.llm import get_llm
from langchain_core.prompts import ChatPromptTemplate
import os

# Load documents
loader = TextLoader("data/company.txt")
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size= 500,
    chunk_overlap= 50
)

docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Store in FAISS
# vectorstore = FAISS.from_documents(docs, embeddings)
if os.path.exists("faiss_index"):
    vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization= True)
else:
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index")


# Create retriever
retriever = vectorstore.as_retriever()

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are an AI Sales Assistant.

Use the context below to answer the question.
                                          
Context:
{context}
                                          
question:
{question}
                                
Answer clearly and concisely.
""")

# RAG function
def rag_response(question):
    relevant_docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in relevant_docs])

    llm = get_llm()

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content