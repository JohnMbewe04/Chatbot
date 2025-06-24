import streamlit as st
from chatbot_logic import get_response

st.set_page_config(page_title="CrisisConnect Chatbot", page_icon="🛟")
st.title("🛟 CrisisConnect — Public Safety Assistant")

st.markdown("Type your question or describe your issue below:")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    st.session_state.messages.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.messages.append(("bot", response))

# Display messages
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**CrisisConnect:** {msg}")
