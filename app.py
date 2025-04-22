import streamlit as st
import requests

st.set_page_config(page_title="AI Mental Health Counselor", layout="centered")

st.title("🧠 AI Mental Health Counselor")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_bot_response(user_input):
    response = requests.post("http://localhost:5000/chat", json={"message": user_input})
    return response.json().get("reply", "Sorry, I couldn't process that.")

user_input = st.text_input("Hi! There I'am Hear For You:", key="input")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = get_bot_response(user_input)
    st.session_state.chat_history.append(("Bot", bot_reply))

for speaker, text in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {text}")
