
# 우리 매장 주변 장소 자동 검색기 (카카오맵 기반)

이 프로젝트는 카카오 지도 API를 활용하여 입력한 주소를 기준으로 반경 1km 내 장소들을 자동 검색합니다.  
카테고리는 음식점, 카페, 병원, 약국, 마트 등으로 분류됩니다.

## 🔧 구성 파일

- `index.html` : 장소 자동 검색 기능을 포함한 정적 웹페이지 (Netlify 등으로 배포)
- `app.py` : Streamlit 앱. 배포된 웹페이지로 링크 연결합니다.
- `requirements.txt` : Streamlit 설치용

## 🌐 빠른 시작

1. `index.html` 파일만 포함된 새 GitHub 레포 생성
2. [Netlify](https://app.netlify.com/) 에서 해당 레포 연결하여 배포
3. 배포된 주소를 `app.py`에 반영 후 Streamlit 배포

## 예시 주소

Netlify 배포 주소 예시: `https://your-netlify-site.netlify.app/index.html`  
Streamlit 앱에서 이 링크를 통해 HTML 실행
