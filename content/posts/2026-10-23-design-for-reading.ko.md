+++
title = '가독성 중심의 블로그 디자인 개선'
date = 2026-10-23T14:00:00+09:00
draft = false
categories = ["Writing"]
tags = ["디자인", "타이포그래피", "블로그 운영"]
summary = "영문판 글의 한 줄 길이가 평균 83자로 권장 범위(45~75자)를 넘어, 본문을 가운데 한 단으로 배치하고 평균 67자로 줄였습니다."
result = "한 줄 글자 수(영문) 평균 83자 → 67자(최적 66자)"
+++

영문판 글 페이지의 한 줄 길이가 평균 83자로 권장 범위(45~75자)를 넘었습니다. 장식은 추가하지 않고 본문을 가운데 한 단으로 배치해 평균 67자로 줄였습니다.

## 참고한 디자인 원칙

### Dieter Rams의 원칙

Dieter Rams는 Braun 제품을 수십 년간 디자인했습니다. [좋은 디자인의 10가지 원칙](https://vitsoe.com/gb/about/good-design) 중 이 블로그에 적용한 5가지는 다음과 같습니다.

| 원칙 | 블로그 적용 |
|---|---|
| 좋은 디자인은 제품을 유용하게 한다 | 블로그의 용도는 읽기이며, 다른 요소는 부차적임 |
| 좋은 디자인은 제품의 이해를 돕는다 | 독자가 다음에 읽을 위치를 찾지 않도록 배치 |
| 좋은 디자인은 눈에 띄지 않는다 | 디자인 요소보다 내용이 먼저 보이도록 구성 |
| 좋은 디자인은 마지막 디테일까지 빈틈없다 | Rams: “어떤 것도 임의로 정하거나 우연에 맡겨서는 안 된다” |
| 좋은 디자인은 가능한 한 적게 디자인한 것이다 | Rams의 요약: “Less, but better” |

### Jony Ive의 단순함

- Apple 디자인 책임자. 2013년 iOS 7 발표에서 “True simplicity is derived from so much more than just the absence of clutter and ornamentation”(단순함은 어수선함과 장식을 없애는 것만으로 얻어지지 않음)이라고 설명
- 단순함을 ‘복잡한 것에 질서를 부여하는 일’로 정의([TechRadar](https://www.techradar.com/pro/quote-of-the-day-by-former-apple-design-chief-jony-ive-true-simplicity-is-derived-from-so-much-more-than-just-the-absence-of-clutter-and-ornamentation-laying-the-foundation-for-a-timeless-design-philosophy))
- 2025년 [Stripe Sessions](https://stripe.com/sessions/2025/a-conversation-with-sir-jony-ive) 대담에서 아무도 보지 않는 가구 안쪽까지 마감하는 장인을 예로 들어 “사람으로서 얼마나 성숙했는지는 아무도 보지 않을 때 하는 일에서 드러난다”고 언급([Jim Nielsen의 기록](https://blog.jim-nielsen.com/2025/notes-from-interview-with-jony-ive/)에서 인용)

이 블로그에 적용한 내용은 다음과 같습니다.

- 제어 루프, 신호, 가스 유량 내용은 줄일 수 없으므로 글의 순서와 그림 위치를 정리해 단순화
- 그림은 해당 그림을 설명하는 문단 바로 옆에 배치
- 독자가 잘 보지 않는 부분(대체 텍스트, 줄바꿈, 다크 모드)까지 관리

## 타이포그래피 기준

| 항목 | Matthew Butterick | Robert Bringhurst |
|---|---|---|
| 한 줄 글자 수(영문) | 45~90자 | 45~75자, 최적 66자 |
| 웹 본문 글자 크기 | 15~25px | – |
| 줄 간격 | 글자 크기의 120~145% | – |

- Butterick의 첫 번째 규칙은 본문 우선. 문서 품질은 대부분 본문 모양이 결정함([Practical Typography](https://practicaltypography.com/typography-in-ten-minutes.html))
- Bringhurst 수치의 출처는 『The Elements of Typographic Style』([인용 출처](https://webtypography.net/2.1.2))

## 참고한 기술 사이트

- Bartosz Ciechanowski: [GPS](https://ciechanow.ski/gps/) 등 작동 원리를 설명하는 긴 글. 조작 가능한 그림을 해당 설명 바로 옆에 배치
- Edward Tufte: 강의 유인물에 잘 짜인 본문, 여백 주석, 본문에 포함된 차트를 사용. [Tufte CSS](https://github.com/edwardtufte/tufte-css)는 이 방식을 웹에 적용한 것
- Gwern Branwen: 미니멀리즘, 타이포그래피, 흑백, 여백 주석이 기본. 링크한 페이지의 사본을 보관해 링크 끊김 방지([Design](https://gwern.net/design))
- Julia Evans: 아는 것과 모르는 것을 구분해 밝히고, 처음 배울 때 찾던 글을 씀([Blogging principles](https://jvns.ca/blog/2017/03/20/blogging-principles/))

네 사이트 모두 장식 요소가 없고, 본문은 한 단이며, 그림은 필요한 위치에 있습니다.

## 기존 디자인의 문제점

영문판 글 페이지를 브라우저에서 측정한 결과입니다.

![이전 디자인. 왼쪽에 좁은 날짜 열, 본문 열은 오른쪽으로 크게 치우쳐 시작. 본문 앞에 요약 라벨 3개](/images/design-before.png)

1. 한 줄 길이 초과: 넓은 화면에서 평균 83자, 최대 89자. Bringhurst 권장 범위 45~75자 초과
2. 본문 위치: 왼쪽 열에는 날짜와 읽는 시간만 있고, 본문 열은 화면 중앙보다 훨씬 오른쪽에서 시작
3. 요약 가독성: 라벨이 옆 열에 있어 휴대전화에서 요약 내용 한 줄에 약 30자(영문)만 들어감. 요약의 시각적 비중이 본문과 같음
4. 차트: 본문과 폭이 같아 라벨 글자가 작고, 다크 모드에서 흰색 사각형으로 표시됨

## 디자인 원칙

1. 본문 글자 크기와 줄 길이를 먼저 정하고, 나머지는 본문에 맞춤
2. 장식 없이 한 단 구성, 분명한 제목 위계, 문단 옆 그림 배치
3. 서체 패밀리 1개(IBM Plex), 회색 계열, 상태 표시 색 1개만 사용. 애니메이션과 자바스크립트는 사용하지 않음
4. 숫자와 단위가 줄바꿈으로 분리되지 않게 하고, 모든 그림에 대체 텍스트를 넣고, 차트도 다크 모드에 맞춤
5. 모든 수치에 조건을 붙이고, 글마다 잘못 판단한 내용을 기록
6. 순수 HTML과 CSS로 작성하고, 금방 낡아 보일 유행은 따르지 않음

## 변경 결과

![새 디자인. 가운데 한 단 배치. 날짜는 제목 위, 요약 라벨은 해당 내용 위](/images/design-after.png)

| 항목 | 변경 전 | 변경 후 |
|---|---|---|
| 넓은 화면의 한 줄 글자 수(영문) | 평균 83자 | 평균 67자 |
| 본문 글자 크기 | 17px | 18px(휴대전화 17px) |
| 레이아웃 | 날짜 열과 본문 열 | 가운데 한 단, 날짜는 제목 위 |
| 요약 | 라벨을 옆 열에 배치 | 라벨을 내용 위에 배치, 왼쪽에 얇은 선 |
| 차트 | 본문 폭, 다크 모드에서 흰색 | 최대 46rem 폭, 다크 모드에서 반전 |

## 향후 계획

- 넓은 화면에서 출처를 여백 주석으로 이동(Tufte, Gwern 방식)
- 차트를 SVG 파일로 바꿔 페이지 색과 일치시킴

## 잘못 판단한 내용

- 처음에는 한국어 본문 기준으로 한 줄을 약 36자로 맞췄음. 블로그를 영어로 다시 쓰면서 줄 길이를 다시 측정하지 않았고, 같은 폭에 영문 83자가 들어감
- 날짜 열은 실험 노트 형식을 따라 만들었고, 독자에게 필요한지는 검토하지 않았음

## 요약

- 기술 블로그는 가독성을 기준으로 설계하고, 본문 글자 크기와 줄 길이를 먼저 정함
- 복잡한 내용은 덜어 내지 않고 순서와 배치를 정리해 단순화
- 한 줄 길이는 영문 기준 약 45~75자, 최적 66자
- 대체 텍스트, 줄바꿈, 다크 모드처럼 잘 보이지 않는 부분까지 관리
