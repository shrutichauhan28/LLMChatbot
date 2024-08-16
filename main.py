import os
import streamlit as st
from dotenv import  load_dotenv
import google.generativeai as gen_ai

#env variables loading
load_dotenv()

#configure streamlit 
st.set_page_config(
    page_title="Chat with gemini-pro",
    page_icon=":balloon",
    layout="centered",
)


gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    if user_role=="model":
        return "assistant"
    else:
        return user_role
    
if "chat_session" not in st.session_state:
    st.session_state.chat_session=model.start_chat(history=[])

st.title("Gemini Pro - ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt=st.chat_input("Ask Gemini pro")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_response=st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

