# Muse 시작 가이드

Meta Muse 가입 절차를 한국어로 정리한 독립적인 안내 페이지입니다. 원문 글의 네 단계 흐름을 새 문장으로 작성하고, 각 단계에 직접 제작한 SVG 그림과 GIF 애니메이션을 넣었습니다. 실제 Muse 화면 캡처가 아니라 안내용 예시입니다.

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

방문자는 이 페이지에서 초대 코드 `L2FZL2`를 복사한 뒤, [Muse 공식 가입 페이지](https://muse.ai/join)에서 가입하고 공식 화면의 초대 코드 항목에 입력합니다. 이 웹페이지가 계정 정보나 결제 정보를 받지는 않습니다.

## 수정 방법

- 글과 링크: `index.html`
- 스타일: `styles.css`
- 초대 코드와 복사 기능: `script.js`의 `REFERRAL_CODE`
- 단계별 그림과 GIF: `assets/`
- 그림 재생성: `tools/make_assets.py` (Pillow 필요)

서비스 제공 지역, 초대 혜택, 결제 및 환불 조건은 변경될 수 있습니다. 게시 전에 [Meta 공식 발표](https://about.fb.com/ko/news/2026/09/introducing-muse-the-worlds-first-personal-ai-agent-built-for-everyone/)와 [Muse 가입 화면](https://muse.ai/join)의 현재 내용을 재확인하세요.

## 참고

- [참고한 한국어 글](https://argous.tistory.com/73): 절차의 흐름만 참고했습니다.
- [GitHub Pages 공식 문서](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
