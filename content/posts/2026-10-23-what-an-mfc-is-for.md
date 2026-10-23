+++
title = 'What an MFC is for: the same command, the same dose'
date = 2026-10-23T12:10:00+09:00
draft = false
categories = ["Design"]
tags = ["MFC", "Semiconductor process", "Requirements"]
summary = "I used to define an MFC as a device that delivers an accurate flow, fast. The wafer taught me a better definition: the same command must deliver the same dose, under any condition."
did = "Asked what the wafer actually feels from an MFC, and rewrote the definition of an MFC from the wafer's side."
broke = "My definition came from the spec sheet: accuracy, settling time, overshoot. It did not say what those numbers are for."
fixed = "New definition: an MFC delivers an accurate flow, fast, and the same way under any condition. Four new spec lines make it testable."
+++

A mass flow controller (MFC) delivers an accurate flow, fast, and the same way under any condition. The last part is what I missed for two years. This post explains how I got there, in three steps.

## Step 1: The spec-sheet definition

A spec sheet describes an MFC with three lines like these:

| Item | Example spec |
|---|---|
| Accuracy | ±1&nbsp;% |
| Settling time | Less than 1&nbsp;s |
| Overshoot | Less than 0.2&nbsp;% |

This was my definition: an MFC delivers an accurate flow, fast, without overshoot. Everything I did served these three lines: tuning, frequency analysis, and signal-to-noise work. The direction was not wrong, but it was incomplete. I never asked what the three lines are for.

## Step 2: What the wafer feels

The MFC sees only its own sensor. The gas then goes through a pipe, fills a chamber, and reaches the wafer. The wafer never sees the flow signal of the MFC. It feels three things:

- the dose: how many molecules arrived
- the ratio between the gases
- the chamber pressure

The wafer is an integrating sensor. Film thickness is the deposition rate integrated over time:

> thickness = ∫ R(t) dt

In plasma-enhanced chemical vapor deposition (PECVD), the gas stays in the chamber for hundreds of milliseconds to a few seconds. This smooths out fast changes in flow. So the wafer cannot tell an MFC that settles in 0.7&nbsp;s from one that settles in 0.3&nbsp;s.

What the wafer feels from a transient is one number: the missing area.

![A step response rises from zero to the setpoint. The grey area between the setpoint and the response is the dose that never arrived.](/images/missing-area.png)

For the flow loop in my [previous post](/posts/2026-10-23-step-response-spectrum/), the missing area is 1/Ki ≈ 0.21&nbsp;s, multiplied by the flow. For a 60&nbsp;s step, that is 0.35&nbsp;% of the dose. For a 3&nbsp;s step, it is 7&nbsp;%. So the transient matters less as the step gets longer. Speed is not quality. The area is.

## Step 3: The same, every time

Processes repeat. A 3D NAND memory stack repeats the same pair of layers 200 times or more. Atomic layer deposition (ALD) can repeat the same cycle 1,000 times.

This changes which errors matter:

- A constant error is corrected once. If every step delivers 2&nbsp;% too little, the engineer changes the step time once, for example from 10&nbsp;s to 10.2&nbsp;s.
- A varying error cannot be corrected. If every step is off by a different amount, even ±0.5&nbsp;%, there is nothing to adjust. The error adds up over the layers.

So the user does not need a zero error. The user needs the same error every time.

### When the user says "Huh?"

A process engineer builds recipes with a simple model: dose = setpoint × time. In this model, a plot of thickness against step time is a straight line through zero. Real lines do not go through zero, because of the missing area. That is fine if the intercept stays in one place.

![Thickness against step time. The expected line goes through zero. The actual lines start later, and each run starts at a different point.](/images/intercept.png)

This figure is an illustration, not measured data. The problem starts when the intercept moves. The gas supply has memory: gas trapped in the pipe, the tail of the previous step, and a gas box that cooled down overnight. Then the user sees things like these:

| What the user did | What happened | The broken assumption |
|---|---|---|
| Ran the step in the middle of a recipe | A different dose | Steps add up |
| Changed the order of two steps | A different dose | Order does not matter |
| Cut the step time in half | Not half the dose | Dose is proportional to time |
| Ran the first wafer of the day | A different dose | Nothing changes over time |
| Replaced the MFC | The recipe no longer works | Units are interchangeable |

Each "Huh?" in this table is the intercept moving.

### Why users ask for less than 0.2 % overshoot

In theory, an overshoot could cancel the missing area and give a zero intercept. Users still ask for almost no overshoot. There are three reasons:

1. Overshoot is a sign of a small stability margin. Its shape changes with conditions, and a moving intercept cannot be corrected.
2. The process does not cancel too much against too little. Particles, a poisoned sputter target, or a wrong interface composition do not go away later.
3. If a process needs extra gas at the start, the recipe can add it in the command. An overshoot that comes from the loop cannot be removed.

Too little gas can be corrected. Too much gas cannot be undone. So an overdamped loop is not a slow design. It is a safe design.

### The environment

The cleanroom stays at 22 ± 0.5&nbsp;°C, but the MFC is not in the cleanroom air. It is in a gas box, next to a chamber at about 400&nbsp;°C, heated lines, and an RF power supply. The gas box temperature follows how busy the tool is.

Here is an example. Take a zero drift of 0.05&nbsp;% of full scale (F.S.) per °C. A change of 5&nbsp;°C then moves the zero by 0.25&nbsp;% F.S. At a setpoint of 10&nbsp;% F.S., that is 2.5&nbsp;% of the setpoint. This is larger than a repeatability spec of ±0.3&nbsp;%. It also changes slowly, so the integration in the wafer does not average it out.

The biggest threat to "the same dose" is not fast noise. It is this slow dependence on the environment.

## The tool maker pushes back

Then I looked at the problem from the side of the equipment maker. A tool maker would push back, and fairly:

- Their recipes already keep the fast transient out of the film. They use stabilization steps, and vent and run valves.
- The gas ratio belongs to the gas box design and the recipe.
- The memory is in the pipe, not in the MFC.

This depends on the recipe. A single-film PECVD recipe usually waits until the flow is stable, then turns on the plasma. Some 3D NAND stack recipes switch gases with the plasma on, so the transient goes into the film. In ALD and short etch steps, the transient is the process.

So the MFC does not own everything that the wafer feels. The work splits like this:

- The tool maker removes the fast transient.
- The MFC keeps the slow part the same: drift, dependence on temperature and pressure, and differences between units.

## Four lines for the spec sheet

A definition that you cannot measure is not useful. A tool maker buys thousands of MFCs and needs numbers that incoming inspection can check quickly. So I translated the definition into four new spec lines. Each one can be tested with one gas and one flow meter. The values are my proposal, not an industry standard.

| New line | Proposed spec |
|---|---|
| Environment | ±0.5&nbsp;% of setpoint when the temperature or the inlet pressure changes |
| Response shape | The missing area (∫e dt) stays within ±10&nbsp;% across conditions |
| Tail after shutoff | The gas delivered after the off command is less than setpoint × 0.1&nbsp;s |
| Unit to unit | The missing area of different units agrees within ±10&nbsp;% |

## What the field reports say

These problems are not only theory:

- At a NIST workshop with the semiconductor industry, attendees named interchangeability as the most important MFC requirement. They added that MFCs must be interchangeable for transient flows as well as for steady flows ([NIST SP 400-101](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication400-101.pdf), 2001).
- One thermal MFC was stepped from 0 to 50&nbsp;% 150 times. The overshoot ranged from 7 to 17&nbsp;%, and the settling time from 0.7 to 2.85&nbsp;s. In another case, an MFC delivered about 5&nbsp;% too little at 30&nbsp;sccm, but its own feedback looked normal ([Solid State Technology](https://sst.semiconductor-digest.com/?p=31263), 2011).
- A zero shift of 0.045&nbsp;% F.S. matched a 1.1&nbsp;% flow error at a 4&nbsp;% setpoint ([Brooks Instrument white paper](https://www.crossco.com/wp-content/uploads/2020/03/brooks-instrument-whitepaper-a-new-class-of-mfcs-with-embedded-flow-diagnostics.pdf), 2016).

## What I got wrong

- I thought that an MFC is just a machine that delivers an accurate flow quickly. Accuracy and speed are means. The end is the same dose for the same command.
- When I first saw that the wafer integrates everything, I went too far. I wanted the MFC to own everything that the wafer feels. The view from the tool maker's side showed me which parts belong to the recipe and the pipe.
- I treated a better signal-to-noise ratio as a goal. It is a tool. It keeps the dose the same at low flow and during pressure changes.

## Summary

The old definition was not wrong. Accuracy and speed are two posts, and they stay. What was missing is the beam across them:

> An MFC delivers an accurate flow, fast, and the same way under any condition.

- The wafer feels the dose, not the flow. A transient counts only as its missing area.
- A constant error is corrected once. A varying error cannot be corrected.
- The MFC owns the slow part that recipes cannot absorb: drift, the environment, and differences between units.
- Four spec lines make this definition testable.
