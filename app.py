
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("📍 우리 매장 주변 카테고리 기반 장소 자동 검색기")

with open("index_auto.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=950, scrolling=True)
