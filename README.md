# Firmware Notes

https://kormansong.github.io

Firmware development notes for mass flow controllers (MFCs) in semiconductor equipment. The site uses no theme. Everything comes from `layouts/`, `assets/`, `data/`, and `i18n/` in this repository. When you push to the `main` branch, the site is published 1 to 2 minutes later.

English is the source language. The Korean version is a translation, published under `/ko/` (see [Translation](#translation)).

## Writing rules

### Plain English for a global audience

Many readers do not speak English as a first language, and some read a machine translation. If a reader whose first language is not English can understand a post, the explanation is clear. So the blog follows these rules:

- Keep each sentence to 25 words or fewer. Keep instructions to 20 words or fewer.
- Give each sentence one idea. Give each paragraph one topic and no more than six sentences.
- Use the active voice and the present tense when possible.
- Use common words: "use", not "utilize" or "leverage".
- Do not use idioms, slang, humor, or cultural references.
- Use a one-word verb instead of a phrasal verb when one exists: "find", not "find out".
- Spell out each abbreviation the first time: "real-time operating system (RTOS)".
- Use one term for one concept, with the same capitalization every time (see the table below).
- Do not use Latin abbreviations. Write "for example", not "e.g.", and "that is", not "i.e.".
- Do not use contractions. Write "do not", not "don't".
- Keep helper words such as "that" and "then" when they prevent confusion.
- Do not put more than two nouns in front of a noun.
- Keep text in figures short, because figures are not translated.
- Use sentence case for titles and headings: "Split FreeRTOS tasks by what they wait for".
- These rules are for body text. Titles, labels, and list entries are short phrases with numbers, as in a datasheet: "Line length cut from 83 to 67 characters".

### Terms

| Concept | Term |
|---|---|
| Rows of a project entry | What I did, Problem, Solution, Next step |
| Project status | In progress, Planned, Done |
| Post category (topic) | Firmware, Control, Process, Linux, Writing |
| A skill with no level | Not rated |
| The skills page | Skills (the address is /skill-map/) |
| The product | mass flow controller (MFC) |

### Numbers, units, and dates

- Put a space between a number and its unit, and keep them on one line. In a post, write `2&nbsp;ms`. In a YAML file, type a real no-break space (U+00A0).
- Dates are formatted automatically for each language: "Oct 21, 2026" in English and "2026. 10. 21." in Korean.

### Post structure

These rules come from Patrick Winston's talk "How to Speak" and from the references at the end of this file.

- Give each post one main idea. If a post has two ideas, write two posts.
- State the main idea in the title and in the first paragraph. Put the conclusion first.
- Repeat the main idea in three places: the title, the result line, and the "Summary" section at the end.
- Give every performance claim a number, the test conditions, and the instrument.
- If you were wrong about something, add a "What I got wrong" section.
- End with what the reader learned and what comes next. Do not end with "Thanks for reading".

### Design

The values behind the design are in the post "Blog design: order, not decoration".

- Nothing unnecessary. Every element on a page carries information.
- Lists are dense: one row per post, with its date, title, key result, and category.
- Reading text sits in one centered column, about 66 characters per line, at 18 pixels (17 on phones).
- Lists, figures, and the skill map may use the wide column (46 rem). Nothing else does.
- Color is used only to show status. Yellow marks only "Problem" and "No evidence".
- No decoration, shadows, animation, or JavaScript.
- Fonts: IBM Plex Sans (text) and IBM Plex Mono (code). Korean pages use IBM Plex Sans KR. Colors and sizes are at the top of `assets/css/main.css`.

## Common tasks

### Write a post

On GitHub, open `content/posts/`, then select Add file → Create new file. Name the file `2026-11-01-short-title.md`, paste the front matter below, and commit.

```toml
+++
title = 'Short title that states the point'
date = 2026-11-01T21:00:00+09:00
categories = ['Firmware']      # Firmware, Control, Process, Linux, or Writing
tags = ['FreeRTOS']
summary = 'One or two sentences for search engines and RSS.'
result = 'The key result, with a number and its condition'
+++

Write the post here in Markdown.
```

`result` appears in every list and under the title, so write it as a short phrase with a number, for example `FFT of dy/dt matches T(jω) within 0.007&nbsp;% below 5&nbsp;Hz`. Titles are short phrases, not full sentences. On a PC, `hugo new content posts/2026-11-01-title.md` creates a file with the same front matter and a section outline.

Then add the Korean translation next to the English file (see [Translation](#translation)).

### Change a skill level

Edit `level` (0 to 4) and `evidence` (the path of a post) in `data/en/skills.yaml`, and make the same change in `data/ko/skills.yaml`. Level 0 means "not rated". Give a level only if you can show evidence for it. The diagram and the tables on the skills page update together.

```yaml
- name: FreeRTOS
  level: 2
  evidence: posts/2026-10-21-task-is-a-unit-of-waiting
```

`area` sets the position in the diagram, `short` sets the short label, and `io` and `io_dir` set the connection outside the chip. If `area` is empty, the skill shows only in the table.

### Change a project

Edit `data/en/projects.yaml` and `data/ko/projects.yaml`. The "Current projects" list on the home page and the projects page update together. Change `status` from `now` to `done` to move a project to "Done".

### Change the home page text

Edit the `title` (the large heading) and the text in `content/_index.md` and `content/_index.ko.md`.

### Add an image

Put the file in `static/images/` and use it in a post as `![What the image shows](/images/file-name.png)`. For oscilloscope captures, use PNG at 1200 pixels wide or less.

Put grey charts with a white background in `static/images/charts/`. In dark mode, the site inverts them so that they do not glare. Do not put photos or scope captures there.

## Translation

The Korean version is a translation of the English text. It is published under `/ko/`, and each translated page shows a "한국어" link in the menu.

- Pages and posts: a translated file next to each English file, with `.ko` before `.md`. For example: `content/about.ko.md`.
- Data: `data/ko/` has the same keys, paths, and values as `data/en/`, with the text fields translated. If a file is missing in `data/ko/`, the Korean pages use the English file.
- Interface text (menus, labels, dates): `i18n/ko.yaml`.
- Korean line breaks: `layouts/_partials/kotext.html`.

To translate a new post:

1. Add `content/posts/<same file name>.ko.md`. Keep `date` and `draft` the same as in the English file.
2. Translate `title`, `summary`, `result`, `categories`, and `tags`. Use the terms in the table below.
3. Point links to other posts at `/ko/posts/...`. Keep image paths and `/code/` paths unchanged.
4. Keep every number, unit, code line, and link target. Translate only the comments in code.

To hide the Korean version, set `disabled = true` under `[languages.ko]` in `hugo.toml`.

### Korean style

The Korean text follows the tone of Korean official documents (공문서):

- Prose uses the formal -ㅂ니다 style (합니다체), with -하였습니다 for the past tense.
- Lists, table cells, `result` lines, and data entries use the noun-ending style (개조식), with no final period. Separate the items with ". ", because the home page shows only the first item of `broke` or `next`.
- Headings are numbered (`## 1.`, `### 가.`). A title line goes above each table (`<표 1> 상태 전이표`). A Korean title goes above each chart (`[그림 1] ...`), because the charts are in English.
- The first paragraph states the conclusion. Do not start with "이 글에서는 ... 설명합니다".
- Do not copy the rhetoric of the English text. Write metaphors and "X is not A. It is B." contrasts as plain statements. Do not start list items with bold text.
- Avoid translationese: 가지다 for "have", the plural -들, ~에 대한, ~을 통해, ~로부터, ~에 의해, ~에서의, and chains of -의.
- Type Korean quotation marks (‘ ’ “ ”) directly. Straight quotes before a particle, as in '2 %'라는, render as the wrong curly quote.
- Put a no-break space between a number and an SI unit, as in English (`2&nbsp;ms`). Write Korean counters without a space (1초, 2년, 11장).
- Keep diagram labels (`short` in `data/ko/skills.yaml`) short. A Hangul character is about twice as wide as a Latin letter.

| English | Korean |
|---|---|
| setpoint | 설정값 |
| full scale (F.S.), reading (Rd) | 풀 스케일(F.S.), 지시값(Rd) |
| dose | 공급량 |
| transient, settling time, missing area | 과도 응답, 정정 시간, 부족 면적 |
| step (in a recipe), step response | 스텝, 계단 응답 |
| repeatability, reproducibility | 반복성, 재현성 |
| trueness, precision, accuracy | 진도, 정밀도, 정확도 |
| bias, scatter, drift | 바이어스, 산포, 드리프트 |
| unit to unit, interchangeability | 개체 간, 호환성 |
| tool maker, fab | 장비사, 팹 |
| thermal MFC, pressure-based MFC | 열식 MFC, 압력식 MFC |
| task, queue, block | 태스크, 큐, 블로킹(대기) |
| state transition table | 상태 전이표 |
| Firmware, Control, Process, Linux, Writing (categories) | 펌웨어, 제어, 공정, 리눅스, 글쓰기 |

## Preview

You need [Hugo extended](https://gohugo.io/installation/) 0.168 or later (Windows: `winget install Hugo.Hugo.Extended`).

```bash
hugo server -D      # http://localhost:1313. -D also shows drafts.
```

## Structure

```
content/
  _index.md           Home page text
  posts/              Posts (YYYY-MM-DD-slug.md)
  skill-map.md        Intro text of the skills page (the diagram and tables come from data/en/skills.yaml)
  projects.md         Intro text of the projects page (the list comes from data/en/projects.yaml)
  about.md            About page
  *.ko.md             Korean translation of the file with the same name
data/en/
  skills.yaml         Skill levels and evidence
  projects.yaml       Projects: what I did, problems, solutions
data/ko/              Korean translation of data/en/ (same keys and paths)
i18n/
  en.yaml, ko.yaml    Interface text for each language
layouts/              Page templates (Hugo)
  _partials/          Header, footer, level meter, summary list, lists, diagram, data lookup, Korean line breaks
assets/css/main.css   Design values and all styles
static/favicon.svg    Site icon
archetypes/posts.md   Front matter and outline for new posts
.github/workflows/hugo.yml   Automatic deployment
```

## References

Plain English

- ASD-STE100 Simplified Technical English, Issue 9 (2025). Sentence length, one topic per paragraph, one word for one meaning.
- Google developer documentation style guide, "Write for a global audience": https://developers.google.com/style/translation

Post structure

- Patrick Winston, "How to Speak", MIT OpenCourseWare (2018)
- Simon Peyton Jones, "How to write a great research paper", Microsoft Research
- George Gopen and Judith Swan, "The Science of Scientific Writing", American Scientist (1990)
- Julia Evans, "Blogging principles": https://jvns.ca/blog/2017/03/20/blogging-principles/

Korean translation

- 행정 효율과 협업 촉진에 관한 규정 시행규칙 (rules for Korean official documents, including the item numbering 1. 가. 1) 가))
- 김순영, 「영한 번역에 나타난 번역투 문장」, and 강주헌, 「국어다운 번역을 위하여」, 『새국어생활』 22권 1호, National Institute of Korean Language (2012). Translationese from English.
- 문장 부호 규정 (Korean punctuation rules, Ministry of Culture, Sports and Tourism notice 2014-0039, effective 2015)
- W3C, Requirements for Hangul Text Layout and Typography (klreq), section 7.1 on line breaking: https://www.w3.org/TR/klreq
