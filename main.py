import streamlit as st
from streamlit_chat import message
import openai

# OpenAI API key
openai.api_key = "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"


# Generating the response form API
def get_response(prompt):
    compilation = openai.Completion.create(
        engine="text-davinci-003",
        prompt = prompt,
        max_tokens=1024,
        n = 1,
        stop= None,
        temperature=0.5,
    )
    message = compilation['choices'][0]['text']
    return message

# Creating the chatbot Interface
st.title("Chatbot")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# User input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = get_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state.generated:
    for i in range(len(st.session_state.generated)-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + "_user")