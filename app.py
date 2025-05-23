
import streamlit as st
import requests

st.set_page_config(layout="centered")
st.title("📍 우리 매장 주변 키워드 자동 추출기")

# 카카오 API 키
KAKAO_API_KEY = "b3aec68754d15e6e3d7a8f7e49246a76"
HEADERS = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}

# 매장명 입력
store_name = st.text_input("매장명 또는 주소를 입력하세요:", "서울 용산구 이태원로 123")

if st.button("🔍 키워드 자동 추출"):
    # 1. 주소 → 좌표 변환
    geocode_url = "https://dapi.kakao.com/v2/local/search/address.json"
    geo_res = requests.get(geocode_url, params={"query": store_name}, headers=HEADERS)

    if geo_res.status_code == 200 and geo_res.json()["documents"]:
        first = geo_res.json()["documents"][0]
        x, y = first["x"], first["y"]
        st.success(f"📍 좌표 찾음: {y}, {x}")

        # 2. 주변 키워드 추출 (카테고리 목록)
        category_codes = ["FD6", "CE7", "CS2", "HP8", "PM9", "MT1", "BK9", "OL7"]  # 음식점, 카페 등

        found_places = []

        for code in category_codes:
            search_url = "https://dapi.kakao.com/v2/local/search/category.json"
            params = {
                "category_group_code": code,
                "x": x,
                "y": y,
                "radius": 1000,
                "size": 15  # 최대 15개씩
            }
            res = requests.get(search_url, params=params, headers=HEADERS)
            if res.status_code == 200:
                found_places += [doc["place_name"] for doc in res.json()["documents"]]

        # 중복 제거 및 출력
        unique_places = sorted(set(found_places))
        st.markdown("### 📋 추출된 키워드 목록:")
        for place in unique_places:
            st.write(f"• {place}")

        if not unique_places:
            st.warning("반경 1km 내 장소가 없습니다.")
    else:
        st.error("❌ 주소를 찾을 수 없습니다. 다시 시도해보세요.")
