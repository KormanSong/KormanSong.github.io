+++
title = '기다리는 대상에 따른 FreeRTOS 태스크 분리'
date = 2026-10-21T21:00:00+09:00
draft = false
tags = ["FreeRTOS", "RTOS", "상태 머신", "태스크 설계"]
categories = ["Firmware"]
summary = "FreeRTOS 태스크는 기능별로 나누지 않고 태스크가 기다리는 대상(이벤트, 주기)에 따라 나눕니다. 버튼 2개로 동작하는 카운터 과제에서 정한 기준입니다."
result = "태스크 2개로 분리: 큐의 이벤트를 기다리는 로직 태스크, 2ms 주기를 기다리는 표시 태스크"
+++

<!-- 초안. 실제 있었던 일을 바탕으로 직접 다시 쓸 것. -->

FreeRTOS 태스크는 태스크가 기다리는 대상(이벤트 또는 주기)을 기준으로 나눕니다. 버튼 2개로 동작하는 카운터 과제에서 정한 기준입니다.

## 과제

7세그먼트 표시기 카운터의 사양은 다음과 같습니다.

- A 버튼: 누르면 1초마다 1씩 증가 시작. 다시 누르면 일시 정지, 한 번 더 누르면 재개
- B 버튼: 언제든 카운트를 0으로 초기화
- 일시 정지 중 B 입력 시 0을 표시하고 정지 상태 유지. 동작 중 B 입력 시 0부터 다시 증가

처음에는 태스크 2개로 구성했습니다.

- 표시 태스크: 공유 변수 값 표시
- 카운터 태스크: 1초마다 공유 변수에 1을 더함

여기까지는 정상 동작했지만, B 버튼을 어느 함수에서 처리할지 정하지 못했습니다. B의 동작이 상황마다 다르게 보였기 때문입니다. MCU 펌웨어를 2년 동안 개발했지만 처음에는 답을 찾지 못했습니다.

## 원인

장치를 입력이 들어가면 출력이 나오는 함수로 보고 있었습니다. 담당 제품인 MFC 펌웨어가 이 구조입니다(제어 루프: ADC 읽기 → 연산 → DAC 출력).

카운터는 같은 입력(B)에도 이전 상황에 따라 결과가 다릅니다. 디지털 회로로 보면 카운터는 순차 회로, 함수는 조합 회로입니다. 함수는 이전 상태를 기억하지 못하므로 카운터를 표현할 수 없습니다.

상태가 빠져 있었습니다. 상태를 넣으면 다음과 같습니다.

> 출력 = f(입력, 상태), 다음 상태 = g(입력, 상태)

상태 2개(RUN, PAUSE)와 이벤트 3개(A, B, TICK)의 상태 전이표입니다.

| 상태 \ 이벤트 | A | B | TICK |
|---|---|---|---|
| RUN | PAUSE로 전이 | count = 0 | count++ |
| PAUSE | RUN으로 전이 | count = 0 | (무시) |

- B는 두 상태 모두에서 카운트만 0으로 만들고 상태는 바꾸지 않음
- RUN 상태에서는 TICK을 계속 처리하므로 0부터 다시 증가하며, B의 추가 동작은 없음

## 분리 기준

처음에는 표시, 카운터, 버튼에 태스크를 하나씩 두려고 했습니다. 기능별 분리였고, 이 기준이 틀렸습니다.

FreeRTOS 태스크는 스택이 따로 있는 실행 단위이며, 블록 상태에서는 CPU를 쓰지 않고 기다립니다. 기다릴 대상이 없는 작업은 함수 호출로 충분합니다. 현재 분리 기준은 다음과 같습니다.

- 같은 주기에 정해진 순서로 실행하는 작업: 한 태스크에 배치
- 주기나 기다리는 이벤트가 다른 작업: 별도 태스크로 분리
- 주변장치: 분리 기준이 아님. 해당 장치가 필요한 태스크에서 사용
- 인터럽트 서비스 루틴(ISR): 이벤트를 큐에 넣고 즉시 복귀

이 기준을 적용한 구성입니다.

<figure class="flow">
  <div class="flow-steps">
    <div class="flow-src">
      <span class="flow-node">버튼 ISR<small>A, B</small></span>
      <span class="flow-node">1초 타이머<small>TICK</small></span>
    </div>
    <span class="flow-arrow" aria-hidden="true"></span>
    <span class="flow-node">큐</span>
    <span class="flow-arrow" aria-hidden="true"></span>
    <span class="flow-node">로직 태스크<small>상태 머신</small></span>
    <span class="flow-arrow" aria-hidden="true"></span>
    <span class="flow-node">표시 태스크</span>
  </div>
  <figcaption>버튼 ISR과 1초 타이머는 이벤트를 큐에 넣음. 로직 태스크는 큐에서 이벤트를 하나씩 꺼내 처리하고, 표시 태스크는 전달받은 값을 표시함.</figcaption>
</figure>

- 로직 태스크: 이벤트 대기
- 표시 태스크: 2ms 주기 대기
- 대기 대상이 다르므로 태스크 2개로 분리. 세 번째 태스크는 불필요
- 버튼과 타이머는 태스크가 아니며 큐에 이벤트만 넣음

```c
typedef enum { EV_A, EV_B, EV_TICK } event_t;
typedef enum { RUN, PAUSE } state_t;

void vLogicTask(void *p) {
    state_t s = PAUSE; uint32_t count = 0; event_t ev;
    for (;;) {
        xQueueReceive(q, &ev, portMAX_DELAY);   /* 대기는 이곳에서만 */
        switch (s) {
        case RUN:
            if (ev == EV_A) s = PAUSE;
            else if (ev == EV_B) count = 0;
            else if (ev == EV_TICK) count++;
            break;
        case PAUSE:
            if (ev == EV_A) s = RUN;
            else if (ev == EV_B) count = 0;
            break;                              /* TICK 무시 */
        }
        g_display_value = count;
    }
}
```

- 상태 전이표의 칸 1개가 `if` 문 1개에 대응
- 표에 없는 조합은 코드에도 없음
- 디버깅 시 확인 항목은 현재 상태와 수신 이벤트 2가지

## 제품 펌웨어 적용

담당 MFC 펌웨어에도 경로가 2가지 있습니다.

| 경로 | 처리 내용 | 구조 | 실행 주체 |
|---|---|---|---|
| 빠른 데이터 경로 | 센서 입력, 제어 연산, 밸브 구동 출력 | 함수 | 주기 태스크 1개 또는 타이머 ISR |
| 느린 명령 경로 | 명령, 모드 전환, 오류 처리 | 상태 머신 | 큐 1개와 로직 태스크 1개 |

‘장치는 함수’라는 처음 관점은 빠른 경로에만 맞습니다. 버튼 문제는 느린 경로를 빠른 경로처럼 다뤄서 생겼습니다.

## 요약

- 태스크는 기다리는 대상(이벤트 또는 주기)별로 분리
- 이벤트를 처리하는 로직은 상태 전이표를 먼저 작성한 뒤 코드 작성

## 향후 계획

- 같은 사양을 슈퍼루프, FreeRTOS, 동기식 설계(모든 이벤트를 `tick()` 함수 하나에서 처리)로 각각 구현
- 하드웨어 없이 PC에서 시험하기 쉬운 정도 비교
