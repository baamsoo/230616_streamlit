import streamlit as st


st.title("마크다운")

# 마크다운
# https://heropy.blog/2017/09/30/markdown/

# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정
# st.markdown -> 마크다운을 사용하겠다

# 제목 마크다운
st.write("""
# 가장 큰 제목 테스트 (h1 - headline1 - st.title)
## 그다음 큰 제목 테스트 (h2 - st.header)
### 그그다음 큰 제목 테스트 <- 보통 여까지 씀 (h3 - st.subheader)
#### 그그그다음 큰 제목 테스트 (h4)
##### 그그그그다음 큰 제목 테스트 (h5)
###### 그그그그그다음 큰 제목 테스트 (h6)
""")  # 문자열을 넣으면 마크다운

# 서식
text = """
기울임 : *별표*, _밑줄_ 하나씩 써주면

진하게 : **별표**, __밑줄__ 두개 써주면

기울임 + 진하게 : ***별표***, ___밑줄___ 세개 써주면

취소선 : ~물결표~

형광팬 : <mark>형광팬</mark>
"""
# st.write(text)
# 태그를 허용하는 옵션
st.markdown(text, unsafe_allow_html=True)

# 레이아웃
st.divider()
st.subheader("레이아웃")
st.write("""
    #### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 붙여쓰면 안된다
        * 들여쓰기
            * 들여쓰기
    - -를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - 붙여쓰면 안된다
""")
st.write("""
    #### 순서가 있는 리스트
    1. 순서가
    2. 있는
    4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
        1. 들여
            1. 쓰기는 1로 시작해야함
                2. 아니면 무시
    1. 1을 넣어도
    1. 들여쓰기 안하면 무시함
    ### 가로줄
    ---
    (---)
    ___
    (___)
    ### 테이플(표)
    |머리|이름|
    |-|-|
    |몸통|파이썬|
    |다리는없나|ㅎㅇㅇㅎ
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://www.naver.com"
l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
st.write(f"""
    * [표시할 텍스트](https://www.naver.com/)
    * [표시할 텍스트2]({l1})
    * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
    * ![이미지에 대한 설명]({l2})
    * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
""")

st.divider()
st.subheader("인용")
st.write(f"""
    > 따라라라란따

    > 삐리리리리리
    >> 인용 인용
    >>> 인인인용

    #### 코드
    `코드를 나타낼 때 주로 쓰이는 묶음 표시(한줄)`
    ```
    여러줄도 되고
    줄바꿔도 되고
    ```
    ```python
    print("파이썬")
    ```
    ```java
    printf("자바")
    ```
""")