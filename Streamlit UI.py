# app.py

import streamlit as st
from chatbot_logic import get_response

st.set_page_config(page_title="CrisisConnect", page_icon="🆘")
st.title("🆘 CrisisConnect Chatbot")
st.markdown("Helping Indianapolis residents connect with safety resources.")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your question or describe your issue", key="user_input")

if user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("CrisisConnect", response))

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")
