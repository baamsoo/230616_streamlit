import streamlit as st  # streamlit을 st라는 변수명으로 streamlit의 기능들을 사용하겠다

st.title("나의 파이썬 웹페이지")
st.header("수업 8일차")
st.subheader("ㅎㅎㅎㅎㅎ")
st.write("아 배고프다ㅏㅏㅏㅏ")

# 기능이 실행되는 순서대로
st.video("https://www.youtube.com/watch?v=REFmxA9hUa4") # 유튜브 링크
st.image("https://i.imgur.com/zKrqcZG.jpeg") # 이미지 링크
# 옵션을 넣어서 세부 기능 차이 가능
st.image("https://i.imgur.com/zKrqcZG.jpeg", use_column_width=True) # 이미지 링크
st.image("img/mnDTYJO.jpeg", width=200)
st.image(image="img/mnDTYJO.jpeg") # 키워드