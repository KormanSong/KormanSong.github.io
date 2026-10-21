+++
title = 'Projects'
date = 2026-10-21T20:00:00+09:00
draft = false
ShowReadingTime = false
ShowBreadCrumbs = false
ShowToc = false
summary = "진행 중인 것과 끝낸 것. 각 항목은 '뭘 했고 / 뭐가 안 됐고 / 어떻게 풀었나' 세 줄로."
+++

<!-- 끝난 것은 위로, 진행 중인 것은 아래로. 링크가 없는 항목은 아직 증거가 없는 항목이다. -->

## In progress

### FreeRTOS two-task counter → event-driven redesign
STM32 · FreeRTOS · 7-segment multiplexing
- **Did:** 두 태스크(디스플레이 / 카운터) + `vTaskDelayUntil`. 버튼 A/B 사양을 상태 표로 재정의.
- **Broke:** 디스플레이가 전역 변수를 자리수마다 다시 읽어 찢어진 값이 표시될 수 있었음. 디스플레이 태스크에 블로킹 호출이 없어 idle 태스크가 굶음.
- **Fixed / Next:** 프레임마다 스냅샷 1회, `vTaskDelayUntil` 2ms, 우선순위 역전(짧은 주기 → 높은 우선순위). 슈퍼루프 / FreeRTOS / 동기식 세 가지 구현 비교 예정.
- 글: [태스크는 기다림의 단위다](/posts/2026-10-21-task-is-a-unit-of-waiting/)

### BeagleBone Black — kernel from scratch
AM335x · Linux 5.10 (TI) → mainline · Device Tree
- **Did:** USB 네트워크로 SSH 접속, sysfs로 LED 트리거 제어, DT에서 주소 → compatible → 드라이버 추적.
- **Next:** Bootlin 실습으로 U-Boot/커널/루트FS 직접 빌드, DT 오버레이로 I2C 활성화, 시리얼 콘솔 연결.

## Planned

- **1 GHz Linux can't bit-bang 115200 but a 200 MHz PRU can** — `cyclictest` + 유저스페이스/커널 hrtimer/PRU 세 방식의 비트 폭 지터를 스코프로 비교.
- **I2C pressure sensor → Linux IIO driver** — 커널에 없는 센서를 골라 업스트림 후보 드라이버 작성.
- **Mini-MFC on PRU** — 유량 센서 + 밸브 + PID를 PRU로. 제어 루프 지터를 세 방식으로 측정.

## Done

<!-- 아직 없음. 첫 항목이 올라오는 날이 이 페이지가 진짜 시작되는 날. -->
