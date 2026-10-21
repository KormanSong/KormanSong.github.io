+++
title = 'Skill Map'
date = 2026-10-21T20:00:00+09:00
draft = false
ShowToc = true
TocOpen = true
ShowReadingTime = false
ShowBreadCrumbs = false
summary = "무엇을, 어디까지 해 봤는지. 각 항목의 등급은 아래 기준으로 매겼고, 등급 3 이상은 근거 글을 링크했다."
+++

<!--
채우는 법:
- 등급(L1~L4)은 아래 기준표 그대로. 스스로 방어할 수 없는 등급은 적지 않는다.
- L3 이상은 반드시 "근거" 칸에 글/코드/측정 링크를 단다. 근거가 없으면 L2로 내린다.
- 안 해 본 것은 지우지 말고 "—" 로 남긴다. 빈칸도 정보다.
- 영어 독자를 위해 항목명은 영어, 설명은 한국어/영어 혼용.
-->

## 등급 기준 (Levels)

| 등급 | 의미 | 면접에서 답할 수 있어야 하는 것 |
|---|---|---|
| **L1** | 벤더 드라이버/HAL을 호출해 봤다 | 어떤 API를 어떤 순서로 불렀나 |
| **L2** | 레지스터를 직접 설정했거나 드라이버를 썼다 | 어떤 레지스터, 왜 그 값인가 |
| **L3** | 스코프/로직 애널라이저로 파형을 보며 디버깅했고, 에러와 타이밍을 다뤘다 | 어떤 파형을 봤고 뭐가 잘못돼 있었나 |
| **L4** | 프로토콜이나 구조를 설계했고, 남에게 설명해 적용시켰다 | 왜 그렇게 설계했고 대안은 뭐였나 |

---

## ① Core — MCU & Toolchain

| 항목 | 등급 | 한 줄 | 근거 |
|---|---|---|---|
| ARM Cortex-M (bare-metal) | L? | 예: 스타트업 코드, 벡터 테이블, 링커 스크립트 수정 경험 | — |
| C (embedded, MISRA 일부) | L? | | — |
| GCC / Make / CMake | L? | | — |
| JTAG/SWD 디버깅 (OpenOCD, J-Link 등) | L? | | — |
| Oscilloscope / Logic analyzer | L? | | — |

## ② Peripherals

| 항목 | 등급 | 한 줄 | 근거 |
|---|---|---|---|
| GPIO / EXTI | L? | | — |
| Timers / PWM / Input capture | L? | | — |
| ADC (+ oversampling, calibration) | L? | 센서 입력 경로 | — |
| DAC | L? | 밸브/액추에이터 출력 경로 | — |
| DMA | L? | | — |
| Flash / EEPROM (parameter storage) | L? | 캘리브레이션 값 저장 | — |
| Watchdog | L? | | — |

## ③ Communication

| 항목 | 등급 | 한 줄 | 근거 |
|---|---|---|---|
| UART | L? | | — |
| RS-485 (half-duplex, 방향 제어) | L? | | — |
| SPI | L? | | — |
| I2C | L? | | — |
| CAN | L? | | — |
| EtherCAT / Modbus / 기타 산업 프로토콜 | L? | TODO: 실제로 쓴 프로토콜 이름으로 교체 | — |
| USB (CDC 등) | L? | | — |

## ④ System

| 항목 | 등급 | 한 줄 | 근거 |
|---|---|---|---|
| FreeRTOS (tasks, queues, notifications) | L? | | [태스크는 기다림의 단위다](/posts/2026-10-21-task-is-a-unit-of-waiting/) |
| State machines (event-driven) | L? | | — |
| Bootloader / Firmware update | L? | | — |
| Embedded Linux (BeagleBone Black, Device Tree) | L1 | 커널 빌드·DT 수정 진행 중 | — |
| Linux kernel drivers (IIO) | — | 예정 | — |

## ⑤ Domain — Flow Control

| 항목 | 등급 | 한 줄 | 근거 |
|---|---|---|---|
| Mass Flow Controller firmware | L? | 반도체 장비용 MFC | — |
| PID / closed-loop control | L? | | — |
| Sensor calibration & linearization | L? | | — |
| Real-time constraints (jitter, deadlines) | L? | | — |

## ⑥ Practices

| 항목 | 등급 | 한 줄 | 근거 |
|---|---|---|---|
| Unit testing off-target (PC에서 로직 테스트) | L? | | — |
| Git / code review | L? | | — |
| Technical writing (EN) | L? | 이 블로그 | — |

---

<small>마지막 갱신: 2026-10-21. 이 페이지는 이력서가 아니라 목차다. 각 등급의 근거는 링크된 글이 담당한다.</small>
