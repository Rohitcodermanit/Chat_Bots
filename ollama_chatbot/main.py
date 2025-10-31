import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']='True'
os.environ['LANGCHAIN_PROJECT']="Q&A Chatbot with OLLAMA"

# Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a help assistant.please response to the user queries"),
        ("user","question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

# title of the app
st.title("Enhanced Q&A Chatbot with Ollama")

# sidebar for setting
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your AI API key:",type='password')

# drop down to select various open AI models 
engine=st.sidebar.selectbox("Select an opne AI Model",["gemma:2b"])

# adjust response parameter
temperature=st.sidebar.slider("temperature",min_value=0.0,max_value=1.0,value=0.7)
max_token=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

# write interface for user input 
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,engine,temperature,max_token)
    st.write(response)
else:
    st.write("Please provide the query")
