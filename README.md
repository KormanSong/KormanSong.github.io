# Firmware Notes

https://kormansong.github.io

반도체 장비용 질량 유량 제어기(MFC) 펌웨어 개발 기록입니다. 별도 테마 없이 이 저장소의 `layouts/`, `assets/`, `data/`로 사이트를 만들며, `main` 브랜치에 푸시하면 1~2분 뒤 자동으로 배포됩니다.

## 작성 기준

### 문체
- 사이트 안내 문구와 소개: 합니다체
- 프로젝트와 기술 역량 항목: 개조식(명사형 종결). 예: "디스플레이·카운터 태스크 분리"
- 블로그 본문: 한 편 안에서 한 가지 문체로 통일

### 용어
한 개념에는 한 용어만 씁니다.

| 개념 | 사용하는 용어 |
|---|---|
| 기록 항목 | 작업 내용, 문제, 해결 방법, 다음 계획 |
| 프로젝트 상태 | 진행 중, 예정, 완료 |
| 글 분류 | 측정, 설계, 문제 해결 |
| 등급 미입력 | 미평가 |
| 이 페이지 이름 | 기술 역량 (주소는 /skill-map/) |

### 표기
- 날짜: `2026. 10. 21.` (문장 부호 규정: 숫자 사이 띄어 쓰기, 마지막 마침표 유지)
- 대등한 항목 묶기: 가운뎃점(`타이머·PWM`). 업계에서 굳은 표기(`JTAG/SWD`)는 그대로 씁니다.
- 숫자와 단위: 띄어 쓰고 줄이 바뀌지 않게 붙임 공백을 씁니다(`2&nbsp;ms`).
- 줄바꿈: 어절 단위로 줄을 바꿉니다. 가운뎃점이 줄 첫머리에 오거나 '제어기(MFC)', '주기)을'처럼 괄호가 붙은 어절이 나뉘지 않도록 `layouts/_partials/kotext.html`이 출력 단계에서 처리하므로, 원본에는 일반 문자만 씁니다.
- 피하는 표현: 'A가 아니라 B' 대구 반복, 극적인 끊어 쓰기, 굵은 글씨 남용, 줄표로 설명 붙이기, '-시키다' 남용, 불필요한 '의'

### 디자인
- 색은 상태 표시에만 씁니다. 노란색은 '문제'와 '근거 없음'에만 표시합니다.
- 왼쪽 열에는 날짜를, 오른쪽 열에는 내용을 둡니다.
- 장식, 그림자, 애니메이션, 자바스크립트는 쓰지 않습니다.
- 서체: IBM Plex Sans KR(본문), IBM Plex Mono(코드). 색과 크기 값은 `assets/css/main.css` 맨 위에 있습니다.

## 자주 하는 작업

### 글 쓰기

GitHub 웹에서 `content/posts/` → Add file → Create new file을 선택하고, 파일 이름을 `2026-11-01-영문-제목.md` 형식으로 정한 뒤 아래 머리말을 붙여 넣고 Commit합니다.

```toml
+++
title = '제목'
date = 2026-11-01T21:00:00+09:00
categories = ['측정']        # 측정, 설계, 문제 해결 중 하나
tags = ['FreeRTOS']
summary = '목록에 표시되는 한두 문장'
did = '작업 내용'
broke = '문제'
fixed = '해결 방법'
next = ''                    # 해결 전이라면 다음 계획
+++

본문은 여기부터 마크다운으로 씁니다.
```

`did`, `broke`, `fixed`, `next` 중 비워 둔 항목은 표시되지 않습니다. PC에서는 `hugo new content posts/2026-11-01-title.md`를 실행하면 같은 머리말이 들어간 파일이 생깁니다.

### 기술 역량 등급 수정

`data/skills.yaml`의 `level`(0~4)과 `evidence`(근거 글 경로)를 수정합니다. 0은 미평가이며, 근거를 제시할 수 있는 등급만 적습니다. 기술 역량 페이지의 구성도(MCU 블록 다이어그램)와 표가 함께 바뀝니다.

```yaml
- name: FreeRTOS
  level: 2
  evidence: posts/2026-10-21-task-is-a-unit-of-waiting
```

구성도에서의 위치는 `area`, 짧은 이름은 `short`, 칩 바깥 연결은 `io`와 `io_dir`로 정합니다. `area`를 비워 두면 표에만 표시됩니다.

### 프로젝트 수정

`data/projects.yaml`을 수정하면 첫 화면의 '진행 중인 프로젝트'와 프로젝트 페이지가 함께 바뀝니다. `status`를 `now`에서 `done`으로 바꾸면 '완료'로 이동합니다.

### 첫 화면 문구

`content/_index.md`의 `title`(큰 제목)과 본문을 수정합니다.

### 이미지

`static/images/`에 넣고 글에서 `![측정 화면 설명](/images/파일명.png)` 형식으로 씁니다. 오실로스코프 캡처는 PNG 형식, 가로 1200픽셀 이하를 권장합니다.

## 미리 보기

[Hugo extended](https://gohugo.io/installation/) 0.168 이상이 필요합니다(Windows: `winget install Hugo.Hugo.Extended`).

```bash
hugo server -D      # http://localhost:1313, -D는 초안(draft)도 표시
```

## 구조

```
content/
  _index.md           첫 화면 문구
  posts/              글 (YYYY-MM-DD-slug.md)
  skill-map.md        기술 역량 소개 문단 (구성도와 표는 data/skills.yaml)
  projects.md         프로젝트 소개 문단 (목록은 data/projects.yaml)
  about.md            소개
data/
  skills.yaml         기술 역량 등급과 근거
  projects.yaml       프로젝트: 작업 내용, 문제, 해결 방법
layouts/              페이지 템플릿 (Hugo)
  _partials/          머리글, 바닥글, 등급 표시, 요약, 목록, 구성도, 줄바꿈 처리(kotext.html)
assets/css/main.css   디자인 값과 전체 스타일
static/favicon.svg    파비콘
archetypes/posts.md   새 글 머리말 틀
.github/workflows/hugo.yml   자동 배포
```

## 참고 자료

- 문장 부호 규정(문화체육관광부 고시 제2014-0039호, 2015년 시행)
- 김순영, 「영한 번역에 나타난 번역투 문장」, 『새국어생활』 22권 1호, 국립국어원, 2012
- 국립국어원 「새국어소식」 2002년 10월호 ('-시키다' 남용)
- W3C 국제화 작업 그룹, 「한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항」(klreq), 7.1절 줄 나눔 (어절 단위 줄 나눔, 줄 첫머리에 올 수 없는 문자)
