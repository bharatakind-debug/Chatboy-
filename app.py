import streamlit as st

st.title("Chatboy")
user_input = st.chat_input("Say something...")

if user_input:
    st.write(f"You said: {user_input}")
    st.write("Chatboy is listening!")
