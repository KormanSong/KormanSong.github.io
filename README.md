# Firmware Notes — Hugo + PaperMod + GitHub Pages

임베디드 펌웨어 작업 기록 블로그. 글은 전부 `content/` 안의 마크다운이고, `main`에 push하면 자동으로 배포된다.

## 처음 한 번만 (약 20분)

### 1. GitHub 저장소 만들기
GitHub에서 새 저장소를 **`KormanSong.github.io`** 이름으로, **Public**, 빈 상태(README 없이)로 만든다.

### 2. 이 폴더를 올리기
```bash
cd blog
git submodule update --init --recursive    # 테마가 비어 있으면 한 번 실행
git add -A
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/KormanSong/KormanSong.github.io.git
git push -u origin main
```
> zip에는 `.git`이 포함되어 있어 `git init`은 필요 없다. 만약 `git status`가 안 되면 `git init` 후 위 순서대로.

### 3. Pages 켜기
저장소 **Settings → Pages → Build and deployment → Source** 를 **GitHub Actions** 로 바꾼다.
그러면 **Actions** 탭에서 "Deploy Hugo site to Pages"가 돌고, 1~2분 뒤 `https://KormanSong.github.io` 에서 열린다.

### 4. TODO 채우기
`hugo.toml`, `content/about.md` 안의 `KormanSong` 과 `TODO` 를 찾아 바꾼다.
```bash
grep -rn "KormanSong\|TODO" hugo.toml content/
```

## 글 쓰는 법 (매번)

```bash
hugo new content posts/2026-11-01-my-title.md   # 템플릿이 archetypes/posts.md 에서 복사됨
# 글 쓰고, 맨 위 draft = true 를 false 로
git add -A && git commit -m "post: my title" && git push
```

로컬에서 미리 보려면 (Hugo 설치: https://gohugo.io/installation/ — Windows는 `winget install Hugo.Hugo.Extended`):
```bash
hugo server -D        # http://localhost:1313  (-D 는 draft도 표시)
```

Hugo 없이도 된다. 마크다운을 `content/posts/`에 넣고 push만 하면 GitHub가 빌드한다.

## 구조

```
content/
  posts/        글. 파일명은 YYYY-MM-DD-slug.md 로 통일
  skill-map.md  무엇을 어디까지 해 봤는지 (등급 L1~L4 + 근거 링크)
  projects.md   진행 중 / 예정 / 완료
  about.md      소개 (영어 단락이 먼저)
  search.md, archives.md   PaperMod 기능 페이지
archetypes/posts.md   새 글 템플릿
hugo.toml             설정
.github/workflows/hugo.yml   자동 배포
themes/PaperMod       테마 (git submodule, 건드리지 않음)
```

## 글의 세 가지 종류 (categories)

- **측정** — 스코프 캡처와 숫자가 있는 실험. 영어로.
- **깨달음** — 생각이 바뀐 지점. 한국어로.
- **실수** — 틀렸던 것과 이유.

한 편의 최소 구조는 세 줄이다: 뭘 했고 / 뭐가 안 됐고 / 어떻게 풀었나.

## 이미지

`static/images/` 에 넣고 글에서 `![설명](/images/파일명.png)` 로 참조. 스코프 캡처는 PNG, 1200px 이하로.

## 커스텀 도메인 (선택)

도메인을 사면 `static/CNAME` 파일에 도메인 한 줄 적고, Settings → Pages → Custom domain 에 입력.
