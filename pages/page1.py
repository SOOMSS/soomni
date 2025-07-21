import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# NanumGothic 폰트 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)

# matplotlib에 NanumGothic 폰트 적용
plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

st.title("matplotlib을 활용한 데이터 시각화 예시")  # 페이지 제목

# 예시 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선', color='blue')  # 한글 라벨
ax.set_title('matplotlib 한글 그래프 예시', fontproperties=fontprop)  # 한글 제목
ax.set_xlabel('x축', fontproperties=fontprop)  # 한글 x축
ax.set_ylabel('y축', fontproperties=fontprop)  # 한글 y축
ax.legend(prop=fontprop)  # 범례에 폰트 적용

st.pyplot(fig)  # Streamlit에 그래프 표시
