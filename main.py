# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    with st.spinner('시 작성 중...'):
        system_template = "Translate the following from English into Korean"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}에 대한 시를 써줘")]
        )

        messages = prompt_template.invoke({"text": content})
        result = model.invoke(messages)
        st.write(result)


# messages = [
#     SystemMessage(content="Translate the following from English into Korean"),
#     HumanMessage(content= content + "에 대한 시를 써줘!"),
# ]

# print(result)



