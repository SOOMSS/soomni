import streamlit as st
import pandas as pd

st.title("CSV 파일 업로드 및 성적 분석")  # 페이지 제목

# 1. CSV 파일 업로드 위젯
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # CSV 파일을 데이터프레임으로 읽기
    st.dataframe(df)  # 원본 데이터 표시

    st.write("업로드된 CSV 컬럼명:", df.columns.tolist())  # 컬럼명 출력

    # 필요한 컬럼명 정의
    score_cols = ['수학 성적', '영어 성적', '과학 성적']

    # 모든 컬럼이 존재하는지 확인
    if all(col in df.columns for col in score_cols) and '학생이름' in df.columns:
        # 학생별 평균 점수 계산
        df['평균 점수'] = df[score_cols].mean(axis=1)
        st.subheader("학생별 평균 점수")
        st.dataframe(df[['학생이름', '평균 점수']])

        # 과목별 석차 계산 및 표시
        st.subheader("과목별 석차")
        rank_df = df.copy()
        for col in score_cols:
            rank_df[f'{col} 석차'] = rank_df[col].rank(ascending=False, method='min').astype(int)
        st.dataframe(rank_df[['학생이름'] + [f'{col} 석차' for col in score_cols]])

        st.caption("학생별 평균 점수와 과목별 석차를 분석하여 보여줍니다.")  # 각주
    else:
        st.error("CSV 파일에 '학생이름', '수학 성적', '영어 성적', '과학 성적' 컬럼이 모두 포함되어 있어야 합니다.")  # 오류 안내
else:
    st.info("학생 성적 CSV 파일을 업로드해주세요.")  # 파일이 업로드되지 않았을 때 안내  