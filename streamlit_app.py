import streamlit as st
import time

st.set_page_config(page_title="카카오맵 키워드 추출기", layout="wide")

st.title("📍 카카오맵 키워드 추출기")
st.markdown("**매장명을 입력하면, 해당 매장을 클릭한 후 반경 1KM 내 키워드를 자동으로 수집합니다.**")
st.warning("⚠️ 현재 데모는 실제 크롤링 없이 구조만 구현되어 있습니다.")

place = st.text_input("매장명 입력", placeholder="예: 스시도쿠")

if st.button("키워드 추출 시작"):
    with st.spinner("브라우저 실행 중..."):
        time.sleep(2)  # 실제 크롤링 대신 대기
        st.success("카카오맵 접속 완료")
        time.sleep(1)
        st.info("매장 검색 및 첫 번째 결과 클릭 완료")
        time.sleep(1)
        st.success("반경 1KM 키워드 수집 완료")

    st.subheader("🔍 추출된 키워드 예시")
    st.markdown("- 지하철역")
- 병원
- 카페
- 학원
st.markdown("- 랜드마크 등")
st.download_button("📥 TXT로 저장", "지하철역")
병원
카페
학원
st.download_button("📥 TXT로 저장", "지하철역, 병원, 카페, 학원, 랜드마크", file_name="keywords.txt")
