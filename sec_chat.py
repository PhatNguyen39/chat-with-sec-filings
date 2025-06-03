from langchain_community.embeddings import OllamaEmbeddings

from langchain.vectorstores import FAISS

from langchain_community.chat_models import ChatOllama

from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
import os

def load_and_embed(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    
    #embeddings = OpenAIEmbeddings()
    embeddings = OllamaEmbeddings(model="mistral")

    vectorstore = FAISS.from_documents(pages, embeddings)
    return vectorstore

def ask_question(vectorstore, query):
    #llm = ChatOpenAI(temperature=0)
    llm = ChatOllama(model="mistral", temperature=0.7)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa_chain.run(query)



