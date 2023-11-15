## Conversational Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from secret import openai_api_key


## Streamlit UI
st.set_page_config(page_title="Nirbhay Assitant Bot!")
st.header("Hey Nirbhay I am ready to assist you for your queries!")

# from dotenv import load_dotenv
# load_dotenv()
import os

chat=ChatOpenAI(temperature=0.5,openai_api_key=openai_api_key)

if 'flowmessages' not in st.session_state:  
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]

## Function to load OpenAI model and get respones

def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
