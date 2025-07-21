
import streamlit as st
import pandas as pd
import numpy as np

st.title("서울대학교 AI융합교육학과")  # 페이지 제목

st.header("수민이의 페이지")  # 헤더
st.subheader("서울대학교 마이크로디그리형")  # 서브헤더
st.text("AI융합교육학과")  # 일반 텍스트
st.markdown("**마크다운** _지원_")  # 마크다운 텍스트

st.header("입력 위젯")  # 입력 위젯 섹션
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의하십니까?")  # 체크박스
color = st.radio("좋아하는 색상은?", ["빨강", "파랑", "초록"])  # 라디오 버튼
hobby = st.selectbox("취미를 선택하세요", ["독서", "운동", "게임"])  # 셀렉트박스
multi_hobby = st.multiselect("여러 취미를 선택하세요", ["독서", "운동", "게임"])  # 멀티셀렉트
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력
file = st.file_uploader("파일을 업로드하세요")  # 파일 업로더
st.button("버튼을 눌러보세요")  # 버튼

st.header("슬라이더와 폼")  # 슬라이더와 폼 섹션
value = st.slider("값을 선택하세요", 0, 100, 50)  # 슬라이더

with st.form("my_form"):
    st.write("폼 내부 요소")
    form_text = st.text_input("폼 텍스트 입력")
    submitted = st.form_submit_button("폼 제출")
    if submitted:
        st.write(f"폼 제출됨: {form_text}")

st.header("데이터 표시")  # 데이터 표시 섹션
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=["a", "b", "c"]
)
st.dataframe(df)  # 데이터프레임 표시
st.table(df)  # 테이블 표시
st.json({"name": "홍길동", "age": 30})  # JSON 표시

st.header("차트와 이미지")  # 차트와 이미지 섹션
st.line_chart(df)  # 라인 차트
st.bar_chart(df)  # 바 차트
st.area_chart(df)  # 에어리어 차트

st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 이미지 표시

st.header("알림 및 진행 표시")  # 알림 및 진행 표시 섹션
st.success("성공 메시지입니다.")  # 성공 메시지
st.info("정보 메시지입니다.")  # 정보 메시지
st.warning("경고 메시지입니다.")  # 경고 메시지
st.error("에러 메시지입니다.")  # 에러 메시지

st.progress(70)  # 진행률 표시

st.header("코드 및 기타 요소")  # 코드 및 기타 요소 섹션
st.code("print('Hello, Streamlit!')", language="python")  # 코드 표시
st.caption("설명 또는 캡션입니다.")  # 캡션

st.header("마이크로디그리형")  # 사이드바 섹션
st.sidebar.title("마이크로디그리형")  # 사이드바 제목
st.sidebar.text_input("AI융합교육학과")  # 사이드바 텍스트 입력

# 각주: 각 요소 옆에 설명을 달았습니다.
# - 텍스트, 입력, 데이터, 차트, 이미지, 알림, 진행률, 코드, 사이드바 등 Streamlit에서 자주 사용하는 모든 주요 요소를 포함했습니다.