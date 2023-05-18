# 머신러닝 특강 내용
# https://docs.streamlit.io/library/api-reference
# https://news.hada.io/
# pip install streamlit openai

import streamlit as st
import openai

# st.write("Hello World!")
# streamlit run app.py 터미널에서 실행하기

openai.api_key = "#"

# ballons 만들기
st.balloons()

st.title("ChatGPT Plus DALL-E!")

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")


if submit:
    # st.write(user_input)

    gpt_prompt = []

    # 여기에 영어로 변역하라는 말도 적어줄 수 있음! 뭐든 추가할 수 있을듯!
    gpt_prompt.append({
        "role": "system",
        "content": "Imagine the detail appearance of the input. Response shortly. Translate to english"
    })

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Waiting for chatGPT..."):
        prompt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=gpt_prompt)

    # st.markdown(prompt["choices"][0]["message"]["content"])

    prompt = prompt["choices"][0]["message"]["content"]
    st.caption(prompt)

    # DALL-E
    with st.spinner("Waiting for DALL-E..."):
        result = openai.Image.create(
            prompt=prompt,
            size="1024x1024"
        )

    st.image(result["data"][0]["url"])
