import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
import os



#chat Bot Initiallization 
st.set_page_config(page_title='AI Chat bot')
st.header('Langchain application')

os.environ['OPENAI_API_KEY'] = 'OPEN AI API'

chat = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessage']=[
        SystemMessage(content="Hey! I am AI, how can I help you today?")
        ]
    
    

def get_chat_response(questions):
    st.session_state['flowmessages'].append(HumanMessage(content=questions))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

#Streamlit initilization.

input = st.text_input('AI Bot :',key='input')
response = get_chat_response(input)
#st.write(response)

submit = st.button("Generate")

if submit:
    st.subheader("The answer is : ")
    st.write(response)