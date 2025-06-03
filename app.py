import streamlit as st
from sec_chat import load_and_embed, ask_question
import os

st.set_page_config(page_title="Chat with SEC Filings", layout="wide")
st.title("📄 Chat with SEC Filings")

uploaded_file = st.file_uploader("Upload a 10-K or 10-Q SEC filing (PDF)", type="pdf")
query = st.text_input("Ask a question about the filing:")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("File uploaded. Embedding...")

    vectorstore = load_and_embed("temp.pdf")
    st.success("File embedded successfully.")

    if query:
        with st.spinner("Thinking..."):
            response = ask_question(vectorstore, query)
        st.markdown("### 📢 Answer:")
        st.write(response)
