import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st

model = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

parser = StrOutputParser()

template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in business knowledge. Give all the answers accurately and in around 30 words."),
    ("user", "Question:{question}")
])

def get_response(question):
    try:
        
        chain = template | model | parser
        
        response = chain.invoke({'question': question})
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
st.title("Business Expert Query System")
st.write("Ask a business-related question and get expert insights!")
user_question = st.text_input("Enter your question:")
if st.button("Get Response"):
    if user_question.strip() == "":
        st.warning("Please enter a valid question!")
    else:
        
        with st.spinner("Fetching response..."):
            response = get_response(user_question)
        st.success("Response:")
        st.write(response)


