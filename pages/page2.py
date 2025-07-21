import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV 파일 업로드 및 성적 분석")  # 페이지 제목

# 1. CSV 파일 업로드 위젯
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # CSV 파일을 데이터프레임으로 읽기
    st.dataframe(df)  # 원본 데이터 표시

    st.write("업로드된 CSV 컬럼명:", df.columns.tolist())  # 컬럼명 출력

    # 컬럼명 매핑: 사용자 데이터에 맞게 컬럼명 지정
    # 예시: 이름, 수학, 영어, 과학
    score_cols = ['수학', '영어', '과학']
    name_col = '이름'

    # 모든 컬럼이 존재하는지 확인
    if all(col in df.columns for col in score_cols) and name_col in df.columns:
        # 학생별 평균 점수 계산
        df['평균 점수'] = df[score_cols].mean(axis=1)
        st.subheader("학생별 평균 점수")
        st.dataframe(df[[name_col, '평균 점수']])

        # 과목별 석차 계산 및 표시
        st.subheader("과목별 석차")
        rank_df = df.copy()
        for col in score_cols:
            rank_df[f'{col} 석차'] = rank_df[col].rank(ascending=False, method='min').astype(int)
        st.dataframe(rank_df[[name_col] + [f'{col} 석차' for col in score_cols]])

        # 성적 분포 시각화 (막대 그래프)
        st.subheader("학생별 평균 점수 그래프")
        fig, ax = plt.subplots()
        ax.bar(df[name_col], df['평균 점수'], color='skyblue')
        ax.set_xlabel('학생 이름')
        ax.set_ylabel('평균 점수')
        ax.set_title('학생별 평균 점수')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # 과목별 성적 분포 시각화 (박스플롯)
        st.subheader("과목별 성적 분포 그래프")
        fig2, ax2 = plt.subplots()
        ax2.boxplot([df[col] for col in score_cols], labels=score_cols)
        ax2.set_title('과목별 성적 분포')
        ax2.set_ylabel('점수')
        st.pyplot(fig2)

        st.caption("학생별 평균 점수와 과목별 석차, 성적 분포 그래프를 분석하여 보여줍니다.")  # 각주
    else:
        st.error("CSV 파일에 '이름', '수학', '영어', '과학' 컬럼이 모두 포함되어 있어야 합니다.")  # 오류 안내
else:
    st.info("학생 성적 CSV 파일을 업로드해주세요.")  # 파일이 업로드되지 않았을 경우 안내 메시지