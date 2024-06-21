# AI-Chatbot-using-Streamlit-and-Langchain
This repository contains a simple AI chatbot application built using Streamlit and Langchain. The chatbot leverages OpenAI's GPT-3.5 model to generate responses to user inputs. The primary goal of this project is to demonstrate how to create an interactive web application for chatting with an AI

## Features
Interactive chat interface using Streamlit.
AI-powered responses using OpenAI's GPT-3.5 model via Langchain.
Maintains conversation context throughout the session.

## Prerequisites
Before running the application, ensure you have the following installed:

Python 3.7 or higher
Streamlit
Langchain
OpenAI API key
Installation

## Clone the repository:
git clone [Repo](https://github.com/smadiwale29/AI-Chatbot-using-Streamlit-and-Langchain/tree/main)

cd ai-chatbot

## Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

## Install the required packages:
pip install -r requirements.txt
Set your OpenAI API key:

Open the app.py file and replace 'OPEN AI API' with your actual OpenAI API key.
Usage

## Run the Streamlit application:
streamlit run app.py
Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501).

Interact with the chatbot by typing your message in the input box and pressing "Generate".

## Code Explanation
Here's a brief overview of the code in app.py:

### Streamlit Page Configuration:
st.set_page_config(page_title='AI Chat bot')
st.header('Langchain application')

### API Key Setup:
os.environ['OPENAI_API_KEY'] = 'OPEN AI API'
Chat Model Initialization:
chat = ChatOpenAI(temperature=0.5)

### Session State Initialization:
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessage'] = [
        SystemMessage(content="Hey! I am AI, how can I help you today?")
    ]

    
### Chat Response Function:
def get_chat_response(questions):
    st.session_state['flowmessages'].append(HumanMessage(content=questions))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content
    
### Streamlit UI Components:
input = st.text_input('AI Bot :', key='input')
response = get_chat_response(input)
submit = st.button("Generate")

if submit:
    st.subheader("The answer is : ")
    st.write(response)
