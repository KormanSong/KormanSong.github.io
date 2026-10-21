+++
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
date = {{ .Date }}
draft = true
categories = []   # 측정, 깨달음, 실수 중 하나
tags = []
summary = ''      # 목록에 보이는 한두 문장

# 제목 아래 세 줄 요약. 쓰지 않는 줄은 비워 두면 표시되지 않습니다.
did = ''          # 한 일
broke = ''        # 막힌 곳. 이 줄에 노란 표시등이 켜집니다.
fixed = ''        # 고친 방법
next = ''         # 아직 못 고쳤다면 다음 단계
+++

