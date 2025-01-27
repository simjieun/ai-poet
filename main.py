# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import streamlit.components.v1 as components

components.html("""
            <head>
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2532708487251314" crossorigin="anonymous"></script>
            </head>
            """, height=0)

model = ChatOpenAI()

parser = StrOutputParser()

st.title('인공지능 시인')

content = st.text_input("시의 주제를 제시해주세요.")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button("시 작성 요청하기", on_click=click_button)

if content or st.session_state.clicked:
    with st.spinner('시 작성 중...'):
        system_template = "Translate the following from English into Korean"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}에 대한 시를 써줘")]
        )
        messages = prompt_template.invoke({"text": content})
        result = model.invoke(messages)
        st.write(parser.invoke(result))

