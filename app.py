import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


prompt_template=ChatPromptTemplate.from_messages([
    ("system","You are a proffesor.Respond questions asked in that manner"),
    ("user","question:{question}")
])


st.title("This is my proffesor model made with llama3 model")
prompt=st.text_input("What is your doubht")
ll=Ollama(model='llama3')
parser=StrOutputParser()
chain=prompt_template|ll|parser

if prompt:
    st.write(chain.invoke({'question':prompt}))




