# terminal) pip install openai streamlit
# Python 3.12.7
# Streamlit 기본포트 : 8501
# terminal) streamlit run app.py --실행

from openai import OpenAI
import streamlit as st

st.title("챗봇 만들기")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 세션 상태 관리        모델과 대화 기록을 유지하기 위해 세션 상태를 사용합니다
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI 응답 생성
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})