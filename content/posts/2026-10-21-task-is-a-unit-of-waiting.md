+++
title = 'Split FreeRTOS tasks by what they wait for'
date = 2026-10-21T21:00:00+09:00
draft = false
tags = ["FreeRTOS", "RTOS", "State machines", "Task design"]
categories = ["Firmware"]
summary = "A small counter with two buttons taught me one rule: split work into FreeRTOS tasks by what each task waits for, not by feature."
result = "Two tasks: one waits on a queue for events, one waits for a 2&nbsp;ms period"
+++

<!-- Draft. Rewrite it in your own words, based on what really happened. -->

This post gives one rule for splitting work into FreeRTOS tasks: split by what each task waits for, not by feature. I found the rule while I built a small counter with two buttons.

## The problem

The exercise was a counter on a 7-segment display. The specification:

- Button A starts the count. The count goes up by 1 every second. Press A again to pause. Press it once more to continue.
- Button B always resets the count to 0.
- If you press B while the counter is paused, the display shows 0 and the counter stays paused. If you press B while the counter runs, the count starts again from 0.

I used two tasks. A display task showed the value of a shared variable. A counter task added 1 to the value every second. This part worked.

Then I could not decide where to handle button B. B seemed to do different things in different situations, and I did not know which function should handle it. I had written MCU firmware for two years, but I did not see the answer at first.

## The cause

I thought of the device as a function: inputs go in, and outputs come out. The product I work on has this structure. Its control loop reads the ADC, calculates, and writes to the DAC.

The counter is different. The same input (B) gives a different result, depending on what happened before. In digital logic terms, the counter is sequential logic, and a function is combinational logic. A function has no memory, so it cannot describe the counter.

The missing idea was state. With state, the device looks like this:

> output = f(input, state), next state = g(input, state)

There are two states (RUN and PAUSE) and three events (A, B, and TICK). This is the state transition table:

| State \ Event | A | B | TICK |
|---|---|---|---|
| RUN | Go to PAUSE | count = 0 | count++ |
| PAUSE | Go to RUN | count = 0 | (ignore) |

The table makes B simple. In both states, B sets the count to 0 and does not change the state. In RUN, the count starts again from 0 only because RUN continues to handle TICK events. B itself does nothing more.

## The rule

At first, I wanted one task for each feature: the display, the counter, and the buttons. That was the wrong rule.

In FreeRTOS, a task is a unit of execution with its own stack. A task can block, which means that it waits without using the CPU. If some work never waits for anything, it does not need its own task. A function call is enough. So I now split tasks by what they wait for:

- Work that runs at the same period, in a fixed order, goes into one task.
- Work that has a different period, or that waits for a different event, goes into a separate task.
- Peripherals do not decide the split. A peripheral is used by the task that needs it.
- An interrupt service routine (ISR) puts an event in a queue and returns immediately.

With these rules, the design looks like this:

<figure class="flow">
  <div class="flow-steps">
    <div class="flow-src">
      <span class="flow-node">Button ISR<small>A, B</small></span>
      <span class="flow-node">1&nbsp;s timer<small>TICK</small></span>
    </div>
    <span class="flow-arrow" aria-hidden="true"></span>
    <span class="flow-node">Queue</span>
    <span class="flow-arrow" aria-hidden="true"></span>
    <span class="flow-node">Logic task<small>state machine</small></span>
    <span class="flow-arrow" aria-hidden="true"></span>
    <span class="flow-node">Display task</span>
  </div>
  <figcaption>The button ISR and the 1&nbsp;s timer put events in a queue. The logic task takes each event from the queue and updates the state. The display task shows the value that it receives.</figcaption>
</figure>

There are still two tasks. The logic task waits for events. The display task waits for its 2&nbsp;ms period. They wait for different things, so they are separate tasks, and there is no reason for a third task. The buttons and the timer are not tasks. They only put events in the queue.

```c
typedef enum { EV_A, EV_B, EV_TICK } event_t;
typedef enum { RUN, PAUSE } state_t;

void vLogicTask(void *p) {
    state_t s = PAUSE; uint32_t count = 0; event_t ev;
    for (;;) {
        xQueueReceive(q, &ev, portMAX_DELAY);   /* waits only here */
        switch (s) {
        case RUN:
            if (ev == EV_A) s = PAUSE;
            else if (ev == EV_B) count = 0;
            else if (ev == EV_TICK) count++;
            break;
        case PAUSE:
            if (ev == EV_A) s = RUN;
            else if (ev == EV_B) count = 0;
            break;                              /* ignore TICK */
        }
        g_display_value = count;
    }
}
```

Each cell of the table maps to one `if` statement. A combination that is not in the table is not in the code either. To debug, I need to check only two things: the current state and the event that the task received.

## How this applies to my product

The product I work on also has two paths:

- The fast data path: sensor input, control calculation, and actuator output. This path is a function. One periodic task or a timer ISR runs it.
- The slow control path: commands, mode changes, and error handling. This path is a state machine. One queue and one logic task run it.

My first idea, "a device is a function," is true only for the fast path. I could not solve the button problem because I treated the slow path like the fast path.

## Summary

- Split tasks by what they wait for (an event or a period), not by feature.
- For logic that handles events, write the state transition table first. Then write the code.

In the next post, I will build the same design in three ways: a superloop, FreeRTOS, and a synchronous design that handles every event in one `tick()` function. Then I will compare how easy it is to test each one on a PC without hardware.
