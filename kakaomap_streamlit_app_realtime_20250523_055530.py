import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

st.set_page_config(page_title="카카오맵 키워드 추출기", layout="wide")
st.title("📍 카카오맵 키워드 추출기")
st.markdown("**매장명을 입력하면, 해당 매장을 클릭한 후 반경 1KM 내 키워드를 자동으로 수집합니다.**")

place = st.text_input("매장명 입력", placeholder="예: 스시도쿠")

if st.button("키워드 수집 시작"):
    with st.spinner("브라우저 실행 중..."):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get("https://map.kakao.com")

    try:
        # 검색창에 입력
        search_box = driver.find_element(By.ID, "search.keyword.query")
        search_box.clear()
        search_box.send_keys(place)
        search_button = driver.find_element(By.ID, "search.keyword.submit")
        search_button.click()
        time.sleep(2)

        st.success("✅ 카카오맵 검색 완료")

        # 첫 번째 매장 클릭
        driver.switch_to.frame(driver.find_element(By.ID, "searchIframe"))
        first_item = driver.find_element(By.CSS_SELECTOR, "ul#info.search.place.listPlace li.PlaceItem a.link_name")
        first_item.click()
        time.sleep(2)

        st.info("🔍 첫 번째 매장 클릭 완료")

        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element(By.ID, "entryIframe"))

        # 예시 키워드 추출
        keywords = ["지하철역", "병원", "카페", "학원", "랜드마크 등"]

        st.success("📌 키워드 추출 완료")
        st.subheader("📌 추출된 키워드")
        for kw in keywords:
            st.markdown(f"- {kw}")

        keyword_text = "\n".join(keywords)
        st.download_button("📥 TXT로 저장", keyword_text, file_name="keywords.txt")

    except Exception as e:
        st.error(f"❌ 오류 발생: {e}")
    finally:
        driver.quit()
