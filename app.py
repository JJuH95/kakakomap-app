
import streamlit as st
import requests

st.set_page_config(layout="centered")
st.title("📍 우리 매장 주변 키워드 자동 추출기 (선택형)")

KAKAO_API_KEY = "b3aec68754d15e6e3d7a8f7e49246a76"
HEADERS = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}

store_name = st.text_input("매장명을 입력하세요:", "스시도쿠")

if st.button("🔍 검색 결과 불러오기"):
    search_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    res = requests.get(search_url, params={"query": store_name}, headers=HEADERS)

    if res.status_code == 200 and res.json()["documents"]:
        results = res.json()["documents"]
        names = [f"{r['place_name']} ({r['address_name']})" for r in results]
        choice = st.selectbox("🔽 검색된 장소 중 하나를 선택하세요", names)
        selected = results[names.index(choice)]

        x, y = selected["x"], selected["y"]
        st.success(f"선택된 장소: {selected['place_name']} - 좌표: ({y}, {x})")

        category_codes = ["FD6", "CE7", "CS2", "HP8", "PM9", "MT1", "BK9", "OL7"]
        found_places = []

        for code in category_codes:
            cat_url = "https://dapi.kakao.com/v2/local/search/category.json"
            params = {"category_group_code": code, "x": x, "y": y, "radius": 1000, "size": 15}
            res = requests.get(cat_url, params=params, headers=HEADERS)
            if res.status_code == 200:
                found_places += [doc["place_name"] for doc in res.json()["documents"]]

        unique_places = sorted(set(found_places))
        st.markdown("### 📋 반경 1km 키워드 목록:")
        for place in unique_places:
            st.write(f"• {place}")

        if not unique_places:
            st.warning("반경 1km 내 키워드가 없습니다.")
    else:
        map_url = f"https://map.kakao.com/?q={store_name}"
        st.error(f"❌ 장소를 찾지 못했습니다. [👉 카카오 지도에서 확인하기]({map_url})", icon="⚠️")
