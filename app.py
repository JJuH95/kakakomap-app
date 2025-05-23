
import streamlit as st
import requests

st.set_page_config(layout="centered")
st.title("📍 우리 매장 주변 키워드 자동 추출기")

KAKAO_API_KEY = "b3aec68754d15e6e3d7a8f7e49246a76"
HEADERS = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}

def get_coordinates(query):
    # 1. 주소 검색
    addr_url = "https://dapi.kakao.com/v2/local/search/address.json"
    addr_res = requests.get(addr_url, params={"query": query}, headers=HEADERS)
    if addr_res.status_code == 200 and addr_res.json()["documents"]:
        doc = addr_res.json()["documents"][0]
        return doc["x"], doc["y"], doc.get("address_name", query)

    # 2. 키워드 검색
    keyword_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    key_res = requests.get(keyword_url, params={"query": query}, headers=HEADERS)
    if key_res.status_code == 200 and key_res.json()["documents"]:
        doc = key_res.json()["documents"][0]
        return doc["x"], doc["y"], doc.get("place_name", query)

    # 실패
    return None, None, None

store_name = st.text_input("매장명 또는 주소를 입력하세요:", "서울 성동구 행당동 268")

if st.button("🔍 키워드 자동 추출"):
    x, y, label = get_coordinates(store_name)

    if x and y:
        st.success(f"📍 '{label}' 의 좌표 찾음: {y}, {x}")
        category_codes = ["FD6", "CE7", "CS2", "HP8", "PM9", "MT1", "BK9", "OL7"]
        found_places = []

        for code in category_codes:
            search_cat_url = "https://dapi.kakao.com/v2/local/search/category.json"
            params = {
                "category_group_code": code,
                "x": x,
                "y": y,
                "radius": 1000,
                "size": 15
            }
            res = requests.get(search_cat_url, params=params, headers=HEADERS)
            if res.status_code == 200:
                found_places += [doc["place_name"] for doc in res.json()["documents"]]

        unique_places = sorted(set(found_places))
        st.markdown("### 📋 추출된 키워드 목록:")
        for place in unique_places:
            st.write(f"• {place}")

        if not unique_places:
            st.warning("반경 1km 내 장소가 없습니다.")
    else:
        map_url = f"https://map.kakao.com/?q={store_name}"
        st.error(f"❌ 장소를 찾지 못했습니다. [👉 카카오 지도에서 직접 검색해보기]({map_url})", icon="⚠️")
