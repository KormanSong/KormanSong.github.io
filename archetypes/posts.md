+++
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
date = {{ .Date }}
draft = true
categories = []   # 측정, 설계, 문제 해결 중 하나
tags = []
summary = ''      # 목록에 표시되는 한두 문장

# 제목 아래 요약. 개조식(명사형 종결)으로 쓰고, 쓰지 않는 항목은 비워 둡니다.
did = ''          # 작업 내용
broke = ''        # 문제. 노란색 표시가 붙습니다.
fixed = ''        # 해결 방법
next = ''         # 해결 전이라면 다음 계획
+++

