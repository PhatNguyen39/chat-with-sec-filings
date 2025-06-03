import streamlit as st

st.title("Hello Streamlit")
st.write("This is a simple Streamlit app.")
x = st.slider("Select a value")
st.write(f"You selected: {x}")
