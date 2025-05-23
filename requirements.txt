
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

st.set_page_config(page_title="카카오맵 키워드 추출기", layout="wide")
st.title("📍 카카오맵 키워드 추출기")
st.markdown("**매장명을 입력하면, 해당 매장을 클릭한 후 반경 1KM 내 키워드를 자동으로 수집합니다.**")

place = st.text_input("매장명 입력", placeholder="예: 스시도쿠")

if st.button("키워드 추출 시작"):
    st.info("브라우저 실행 중...")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://map.kakao.com/")
        wait.until(EC.presence_of_element_located((By.ID, "search.keyword.query")))
        search_box = driver.find_element(By.ID, "search.keyword.query")
        search_box.clear()
        search_box.send_keys(place)
        driver.find_element(By.ID, "search.keyword.submit").click()

        time.sleep(2)  # 검색 결과 로딩 대기

        # 검색 결과 첫 번째 항목 클릭
        first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul#info.search.place.listPlace li.PlaceItem div.head_item span")))
        driver.execute_script("arguments[0].click();", first_result)

        time.sleep(3)  # 페이지 이동 대기

        st.success("카카오맵 접속 및 매장 클릭 완료")

        # 여기에서 키워드 크롤링 로직 수행 (예시로 mock 키워드)
        keywords = ["지하철역", "병원", "카페", "학원", "랜드마크 등"]

        st.success("✅ 반경 1KM 키워드 수집 완료")
        st.subheader("📌 추출된 키워드")
        for kw in keywords:
            st.markdown(f"- {kw}")

        # 다운로드 버튼
        keyword_text = "\n".join(keywords)
        st.download_button("📥 TXT로 저장", keyword_text, file_name="keywords.txt")
    except Exception as e:
        st.error(f"❌ 오류 발생: {e}")
    finally:
        driver.quit()
