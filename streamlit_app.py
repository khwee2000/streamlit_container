import streamlit as st
import numpy as np

# 예시 코드 1
with st.container():
    st.write("This is inside the first container")
    st.bar_chart(np.random.randn(50, 3))

# 예시 코드 2
container = st.container()
container.write("This is inside the second container")
st.write("This is outside the second container")

# 예시 코드 3
with st.container():
    st.write("This is inside the third container")
    st.bar_chart(np.random.randn(50, 3))

# 컨테이너 외부에 요소 추가
st.write("This is outside all containers")
