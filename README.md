# Firmware Notes

https://kormansong.github.io

임베디드 펌웨어 작업 기록. 테마 없이 이 저장소의 `layouts/`, `assets/`, `data/` 만으로 만들어지고, `main`에 push하면 1~2분 뒤 자동으로 배포됩니다.

## 디자인 원칙

1. **색은 신호일 때만 쓴다.** 흰 종이, 회색 잉크, 그리고 노란 표시등 하나. 노랑은 "막힌 곳"과 "근거 없음"처럼 뭔가 맞지 않는 곳에만 켜진다. (반도체 팹 노광 구역의 황색 조명, 계측기 표시등)
2. **왼쪽 열은 시간, 오른쪽 열은 내용.** 날짜, 시작한 달, 기준일은 늘 왼쪽에 있다.
3. **모든 기록은 세 줄로 요약한다.** 한 일, 막힌 곳, 고친 방법(또는 다음).
4. **주장에는 근거를 붙인다.** 스킬 맵에서 3등급 이상인데 근거 글이 없으면 페이지가 스스로 표시한다.
5. **덜어낸다.** 카드, 그림자, 장식, 애니메이션, 자바스크립트를 쓰지 않는다.

서체는 IBM Plex Sans KR(본문), IBM Plex Mono(코드). 색과 크기 값은 `assets/css/main.css` 맨 위에 모여 있습니다.

## 자주 하는 일

### 글 쓰기

GitHub 웹에서 바로 쓸 수 있습니다. `content/posts/` → **Add file → Create new file** → 파일 이름을 `2026-11-01-짧은-영문-제목.md` 처럼 짓고, 아래 머리말을 붙여 넣고 **Commit**.

```toml
+++
title = '제목'
date = 2026-11-01T21:00:00+09:00
categories = ['측정']        # 측정, 깨달음, 실수 중 하나
tags = ['FreeRTOS']
summary = '목록에 보이는 한두 문장'
did = '한 일'
broke = '막힌 곳. 이 줄에 노란 표시등이 켜집니다'
fixed = '고친 방법'
next = ''                    # 아직 못 고쳤다면 다음 단계
+++

본문은 여기부터 마크다운으로.
```

`did`, `broke`, `fixed`, `next` 중 비워 둔 줄은 표시되지 않습니다. PC에서 쓸 때는 `hugo new content posts/2026-11-01-title.md` 로 같은 머리말이 채워진 파일이 생깁니다.

### 스킬 맵 등급 바꾸기

`data/skills.yaml` 의 `level`(0~4)과 `evidence`(근거 글 경로)를 고칩니다. 0은 "평가 전"이고, 방어할 수 있는 등급만 적습니다.

```yaml
- name: FreeRTOS
  level: 2
  evidence: posts/2026-10-21-task-is-a-unit-of-waiting
```

### 프로젝트 갱신

`data/projects.yaml` 하나를 고치면 첫 화면의 "지금 하는 일"과 프로젝트 페이지가 함께 바뀝니다. `status`를 `now` → `done`으로 바꾸면 끝낸 일로 옮겨집니다.

### 첫 화면 문구

`content/_index.md` 의 `title`(큰 제목)과 본문.

### 이미지

`static/images/` 에 넣고 글에서 `![무엇을 잰 화면인지](/images/파일.png)`. 스코프 캡처는 PNG, 가로 1200px 이하.

## 미리 보기

[Hugo extended](https://gohugo.io/installation/) 0.168 이상 (Windows: `winget install Hugo.Hugo.Extended`)

```bash
hugo server -D      # http://localhost:1313, -D 는 초안(draft)도 표시
```

## 구조

```
content/
  _index.md           첫 화면 문구
  posts/              글 (YYYY-MM-DD-slug.md)
  skill-map.md        스킬 맵 소개 문단 (표는 data/skills.yaml 에서)
  projects.md         프로젝트 소개 문단 (목록은 data/projects.yaml 에서)
  about.md            소개
data/
  skills.yaml         스킬 맵 등급과 근거
  projects.yaml       프로젝트: 한 일, 막힌 곳, 고친 방법
layouts/              페이지 틀 (Hugo 템플릿)
  _partials/          머리, 꼬리, 등급 미터, 세 줄 요약, 목록 한 줄
assets/css/main.css   디자인 토큰과 모든 스타일
static/favicon.svg    기록장의 세 줄과 표시등
archetypes/posts.md   새 글 머리말 틀
.github/workflows/hugo.yml   자동 배포
```
