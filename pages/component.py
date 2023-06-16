import streamlit as st

st.title("컴포넌트")
# 위-아래로 한줄로만
st.write("🐯")
cols = st.columns(2) # 컬럼 리스트를 가지게 됨
cols[0].write("🐯")
cols[1].write("🐯🐯")
cols = st.columns(3)
cols[0].write("🦁")
cols[1].write("🦁🦁")
cols[2].write("🦁🦁🦁") # cols[-1].write("🦁🦁🦁")
cols = cols[0].columns(3) # 열의 열도 가능
cols[0].write(")")
cols[1].write("))")
cols[2].write(")))")
col1, col2 = st.columns(2) # 리스트 언패킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")

with col1 : # col1을 기준으로 streamlit을 써주겠다
    # 블록 (:) 을 열면 이 안에서는 streamlit 기능 사용시 col1에 종속됨
    st.write("왼쪽")
with col2 : # col2을 기준으로 streamlit을 써주겠다
    # 블록 (:) 을 열면 이 안에서는 streamlit 기능 사용시 col2에 종속됨
    st.write("오른쪽")


# tabs = st.tabs(["김치찌개", "된장찌개", "순두부찌개"])
tab_menus = ["김치찌개", "된장찌개", "순두부찌개"]
tab1, tab2, tab3 = st.tabs(tab_menus)
img1 = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAzMDVfMTg3%2FMDAxNjc4MDE4Nzk0MjY1.XJjFwipOMvY6tyYFqill2WXMzySR3EJA9BHHEoRh4CEg.4DClJDd_VLtXOboG-afuaQtFae9kltlAObpVwgIUH-Yg.JPEG.h2ryubimui%2FIMG_2773.jpg&type=sc960_832"
tab1.image(img1)
with tab2:
    img2 = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAzMjBfMTU3%2FMDAxNjc5MzA1NDUyOTU0.C3XnDShbwPp0HSvvRIF8yzxiTmce3evvJJTk_VzlNvQg.K1GGfilZprrzX_EoC1iKE9SOipaHZGwI4Zi7Y6CqLacg.JPEG.bdan9333%2FIMG_0071.JPG&type=sc960_832"
    st.image(img2)
tab3.write("순두부는 상상에...")

exp = st.expander("ㅎㅇ")
exp.image("https://static.wtable.co.kr/image-resize/production/service/recipe/1074/4x3/d3c0b5c1-2671-483e-9bbf-76496bb443fd.jpg")
# with exp : ...

# 입력
st.title("입력")
name1 = st.text_input("나의 이름은") # 변수로 받을 수 있음
name2 = st.text_input("너의 이름은") # 변수로 받을 수 있음
st.write(f"너는 {name1}이구나")
st.write(f"나는 {name2}이구나")
age = st.number_input("당신의 나이는?", step=1)
st.write(f"나는 {age}살이다")
height = st.number_input("당신의 키는?", step=0.1)
st.write(f"나는 {height}cm이다")
# https://docs.streamlit.io/library/api-reference/widgets, input 정보

st.divider()
mode = st.checkbox("잔소리 ON/OFF")
col1, col2, col3 = st.columns(3)
r = col1.radio("내용 선택", ["취업", "코딩", "출결"])
s = col2.slider("강도 선택", min_value=1, max_value=10)
b = col3.selectbox("꾸미기", ["친절하게", "반말", "욕"])
if mode :
    format = None
    if b == "친절하게" :
        format = lambda x : f"여러분~ {x}"
    elif b == "반말" :
        format = lambda x : f"야 {x}"
    elif b == "욕" :
        format = lambda x : f"XX, {x}"
    if r == "취업":
        for i in range(s) :
            st.write(format("8월에는 자소서...?"))
    elif r == "코딩":
        st.write(format("헉"))
    elif r == "출결":
        st.write(format("qr 잘찍으세요"))
else :
    st.write(format("밥 맛있게 먹으세요"))