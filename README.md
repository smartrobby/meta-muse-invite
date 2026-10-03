# Muse 시작 가이드

Meta Muse 가입 절차를 한국어로 정리한 독립적인 안내 페이지입니다. 원문 글의 네 단계 흐름을 새 문장으로 작성했습니다. STEP 01–03에는 직접 제작한 그림과 GIF를, STEP 04에는 실제 Muse 화면 사진을 사용합니다.

## 미리 보기

`index.html`을 브라우저에서 열거나 아래처럼 로컬 서버를 실행하세요.

```sh
python3 -m http.server 8000
```

브라우저에서 `http://localhost:8000`으로 접속합니다.

## 공개 방법: GitHub Pages

1. 이 저장소의 변경 사항을 `main` 브랜치에 올립니다.
2. GitHub 저장소의 **Settings → Pages**로 이동합니다.
3. **Build and deployment → Source**를 **Deploy from a branch**로 설정합니다.
4. 브랜치는 **main**, 폴더는 **/(root)**를 선택하고 **Save**를 누릅니다.
5. 배포가 끝나면 `https://smartrobby.github.io/meta-muse-invite/`에서 확인합니다. 처음 반영될 때 몇 분 걸릴 수 있습니다.

페이지 주소를 한국의 방문자에게 공유하면 누구나 접속할 수 있습니다. 검색 엔진에 발견되도록 하려면 Google Search Console 등에 공개 URL을 등록하고, 검색 결과 반영에는 시간이 걸릴 수 있음을 감안하세요. 별도 도메인이 있다면 GitHub Pages의 **Custom domain** 설정과 DNS CNAME 레코드를 추가할 수 있습니다.

검색용 대표 주소는 `https://smartrobby.github.io/meta-muse-invite/`입니다. 검색 엔진에 등록할 때는 이 주소와 `https://smartrobby.github.io/meta-muse-invite/sitemap.xml`을 사용하세요. 페이지의 해시태그는 관련 단계로 이동하는 링크이며 검색 순위를 보장하지 않습니다.

방문자는 이 페이지에서 초대 코드 `L2FZL2`를 복사한 뒤, 미국 VPN 연결 상태의 스마트폰 Chrome 또는 Edge에서 [Meta Muse 소개 페이지](https://ai.meta.com/muse/)를 엽니다. 브라우저 메뉴에서 **데스크톱 사이트**를 선택하고, **CREATOR STORIES · Get inspired** 아래의 **MUSE FOR SMALL BUSINESS** 구역까지 내려가 그 구역의 **Try Muse**를 눌러 [소상공인용 가입 웹페이지](https://muse.ai/business)로 이동합니다. 상단이나 Get inspired 구역의 일반 Try Muse가 앱스토어로 연결되더라도 이 가이드에서는 앱을 설치하지 않고 웹사이트에서 가입을 진행합니다. 계정 등록과 코드 입력은 Muse 공식 화면에서 진행하며, 이 웹페이지가 계정 정보나 결제 정보를 받지는 않습니다.

STEP 02에 들어간 소상공인 구역의 공식 화면 사진은 2026년 10월 3일 [Meta Muse 소개 페이지](https://ai.meta.com/muse/)를 캡처한 것으로, 이후 화면이 달라질 수 있습니다. Muse for Small Business의 [공식 안내](https://muse.ai/business)는 현재 미국·캐나다의 만 18세 이상 대상이라고 표시합니다.

## 수정 방법

- 글과 링크: `index.html`
- 스타일: `styles.css`
- 초대 코드와 복사 기능: `script.js`의 `REFERRAL_CODE`
- 단계별 그림과 STEP 01–03 GIF: `assets/`
- STEP 04의 실제 Muse 화면 사진: `assets/redeem/` (원본 파일명에 담긴 15:07:00 → 15:07:18 순서)
- 그림 재생성: `tools/make_assets.py` (Pillow 필요)

STEP 04 사진은 작업 폴더에 제공된 Samsung Browser 스크린샷 네 장을 사용합니다. 사진은 **메뉴 → 설정 → 일반** 화면까지 보여 주며 실제 리딤 코드 입력창은 포함하지 않습니다. 안내 문구도 그 범위에 맞춰 작성했습니다.

서비스 제공 지역, 초대 혜택, 결제 및 환불 조건은 변경될 수 있습니다. 게시 전에 [Meta 공식 발표](https://about.fb.com/ko/news/2026/09/introducing-muse-the-worlds-first-personal-ai-agent-built-for-everyone/)와 [Muse 가입 화면](https://muse.ai/join)의 현재 내용을 재확인하세요.

## 참고

- [참고한 한국어 글](https://argous.tistory.com/73): 절차의 흐름만 참고했습니다.
- [GitHub Pages 공식 문서](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
