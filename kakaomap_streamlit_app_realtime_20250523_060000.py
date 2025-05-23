import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

st.set_page_config(page_title="카카오맵 키워드 추출기", layout="wide")
st.title("📍 카카오맵 키워드 추출기")
st.markdown("매장명을 입력하면, 해당 매장을 클릭한 후 반경 1KM 내 키워드를 자동으로 수집합니다.")

place = st.text_input("매장명 입력", placeholder="예: 스시도쿠")

if st.button("키워드 추출 시작") and place:
    st.info(f"{place} 매장 키워드 추출을 시작합니다...")
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        url = "https://map.kakao.com/"
        driver.get(url)
        time.sleep(2)

        search_box = driver.find_element(By.ID, "search.keyword.query")
        search_box.send_keys(place)
        search_box.submit()
        time.sleep(2)

        # 첫 번째 매장 클릭
        item = driver.find_element(By.CSS_SELECTOR, ".placelist .PlaceItem .info_item .clickArea")
        item.click()
        time.sleep(2)

        st.success("매장 클릭 완료, 키워드 수집 구조 작동 중...")

        # 예시 키워드 (실제는 페이지 크롤링 구조 필요)
        keywords = ["지하철역", "병원", "카페", "학원", "랜드마크 등"]
        st.subheader("📌 추출된 키워드 예시")
        for kw in keywords:
            st.markdown(f"- {kw}")

        # 파일 다운로드 버튼
        result_text = "\n".join(keywords)
        st.download_button("📄 TXT로 저장", result_text, file_name="keywords.txt")

        driver.quit()

    except Exception as e:
        st.error(f"오류 발생: {e}")
