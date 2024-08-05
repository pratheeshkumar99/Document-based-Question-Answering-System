import streamlit as st
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
import os

# Load environment variables from .env file
load_dotenv()

def load_and_prepare_data(document_text):
    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    
    # Wrap the string in a Document object and split
    doc = Document(page_content=document_text)
    document_chunks = text_splitter.split_documents([doc])
    
    # Embed documents
    embedding = OpenAIEmbeddings()
    vector_store_faiss = FAISS.from_documents(document_chunks, embedding)
    
    return vector_store_faiss

# Streamlit UI
st.title('Information Query System')

uploaded_file = st.file_uploader("Choose a text file", type="txt")
if uploaded_file is not None:
    document_text = str(uploaded_file.read(), 'utf-8')  # Read and convert from binary to text
    vector_store_faiss = load_and_prepare_data(document_text)  # Process the uploaded document
    
    query = st.text_input("Enter your query:")
    
    if st.button('Get Answer'):
        # Retrieve and process the query
        result = vector_store_faiss.similarity_search(query, top_k=3)
        context = " ".join([doc.page_content for doc in result])
        
        # Prepare the LLM and the retrieval chain
        llm = ChatOpenAI(model="gpt-4")
        prompt = ChatPromptTemplate.from_template(
            """
            Answer the following question based only on the provided context:
            <context>
            {context}
            </context>
            """
        )
        
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = vector_store_faiss.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        # Invoke the retrieval chain
        response = retrieval_chain.invoke({"input": query, "context": context})
        answer = response.get('answer', 'No answer found.')
        
        st.write('Answer:', answer)