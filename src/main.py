import streamlit as st
from back import llm, RAG
from time import time
# Simple response function
def get_response(user_input):
    return uva_llm.invoke(user_input)

rag = RAG.RAG("cp3").get_docsearch()         
uva_llm = llm.UVA_LLM(rag=rag)  

# Streamlit app
st.set_page_config(page_title="UVA Chatbot", layout="centered")
st.image("assets/ojlogo2.svg.png")
st.title("UVA Chatbot")

st.markdown("""
    <style>
    .chat-message {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .chat-label {
        font-weight: bold;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        margin-right: 10px;
    }
    .user-message {
        background-color: #DCF8C6;
        text-align: right;
    }
    .user-label {
        background-color: #34B7F1;
        color: white;
    }
    .bot-message {
        background-color: #E3E3E3;
        text-align: left;
    }
    .bot-label {
        background-color: #FF5733;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = []

for sender, message in st.session_state.history:
        if sender == "You":
            st.markdown(f'''
                <div class="chat-label user-label">H</div>
                <div class="chat-message user-message">
                    <div>{message}</div>
                </div>
                ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
                <div class="chat-label bot-label">B</div>
                <div class="chat-message bot-message">
                    <div>{message}</div>
                </div>
                ''', unsafe_allow_html=True)

def response(user_input):
    with st.spinner('Processing...'):
        if user_input:
            st.session_state.history.append(("You", user_input))
            bot_response = get_response(user_input)
            st.markdown(f'''
                <div class="chat-label user-label">H</div>
                <div class="chat-message user-message">
                    <div>{user_input}</div>
                </div>
                ''', unsafe_allow_html=True)
            st.markdown(f'''
                <div class="chat-label bot-label">B</div>
                <div class="chat-message bot-message">
                    <div>{bot_response}</div>
                </div>
                ''', unsafe_allow_html=True)
            st.session_state.history.append(("Bot", bot_response))

user_input = st.text_input("Type your message here...", key="input")

if st.button("Send"):
    response(user_input)
