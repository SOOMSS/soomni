import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

st.title("학생 성적 데이터 시각화")  # 페이지 제목

# NanumGothic 폰트 경로 지정 (절대경로로 지정)
font_path = os.path.join(os.path.dirname(__file__), "../fonts/NanumGothic-Regular.ttf")
fontprop = fm.FontProperties(fname=font_path)

# matplotlib에 NanumGothic 폰트 등록 및 적용
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# 데이터 생성
data = {
    '이름': ['홍길동', '김영희', '이철수', '박민수', '최지은'],
    '수학': [85, 90, 70, 95, 60],
    '영어': [78, 88, 65, 92, 72],
    '과학': [92, 84, 75, 89, 68]
}
df = pd.DataFrame(data)

st.subheader("원본 데이터")
st.dataframe(df)  # 원본 데이터 표시

# 학생별 평균 점수 계산
df['평균 점수'] = df[['수학', '영어', '과학']].mean(axis=1)
st.subheader("학생별 평균 점수")
st.dataframe(df[['이름', '평균 점수']])

# 과목별 석차 계산
st.subheader("과목별 석차")
rank_df = df.copy()
for col in ['수학', '영어', '과학']:
    rank_df[f'{col} 석차'] = rank_df[col].rank(ascending=False, method='min').astype(int)
st.dataframe(rank_df[['이름'] + [f'{col} 석차' for col in ['수학', '영어', '과학']]])

# 학생별 평균 점수 그래프
st.subheader("학생별 평균 점수 그래프")
fig, ax = plt.subplots()
ax.bar(df['이름'], df['평균 점수'], color='skyblue')
ax.set_xlabel('학생 이름', fontproperties=fontprop)
ax.set_ylabel('평균 점수', fontproperties=fontprop)
ax.set_title('학생별 평균 점수', fontproperties=fontprop)
plt.xticks(rotation=45, fontproperties=fontprop)
st.pyplot(fig)

# 과목별 성적 분포 박스플롯
st.subheader("과목별 성적 분포 그래프")
fig2, ax2 = plt.subplots()
ax2.boxplot([df[col] for col in ['수학', '영어', '과학']], labels=['수학', '영어', '과학'])
ax2.set_title('과목별 성적 분포', fontproperties=fontprop)
ax2.set_ylabel('점수', fontproperties=fontprop)
plt.setp(ax2.get_xticklabels(), fontproperties=fontprop)
st.pyplot(fig2)

st.caption("NanumGothic 폰트를 활용하여 한글이 포함된 성적 그래프를 시각화합니다.")