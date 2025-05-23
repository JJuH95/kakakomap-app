
import streamlit as st

st.set_page_config(layout="centered")
st.title("📍 우리 매장 주변 장소 자동 검색기")

st.markdown("""
이 앱은 [카카오 지도 API](https://developers.kakao.com/)를 사용하여  
**입력한 주소 기준 반경 1km 내의 장소**를 카테고리별로 자동 검색합니다.

👇 아래 버튼을 눌러 검색기를 실행하세요!
""", unsafe_allow_html=True)

# 실제 Netlify 배포 주소로 수정
st.link_button("🔎 장소 검색기 실행", "https://your-netlify-site.netlify.app/index.html")
