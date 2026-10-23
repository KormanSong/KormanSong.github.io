+++
title = 'The FFT of a step response mostly shows the step'
date = 2026-10-23T12:00:00+09:00
draft = false
categories = ["Design"]
tags = ["Control", "FFT", "Signal processing", "MFC"]
summary = "The spectrum of a step response is largest at 0 Hz and falls steadily, because the step itself shapes it. To see the control loop, take the FFT of dy/dt."
did = "Modeled the flow loop as a first-order plant with integral control. Compared the FFT of the simulated response with theory."
broke = "Expected a peak at a \"flow frequency\". The spectrum of the response had no peak and fell steadily from 0&nbsp;Hz."
fixed = "Took the FFT of dy/dt instead. It matches the closed-loop frequency response T(jω) within 0.01&nbsp;% below 5&nbsp;Hz."
next = "Add what real firmware has: a 4&nbsp;ms control period, computation delay, and a sensor filter. Then compare with measured data."
+++

I wanted to know which frequencies a flow step contains, so I took the FFT of a simulated step response. The result had no peak. It was largest at 0&nbsp;Hz and fell steadily. This post explains why, and shows what to analyze instead: the derivative of the response, dy/dt.

## The model

I modeled the flow loop of a mass flow controller (MFC) in the simplest way:

- Plant: a first-order lag with a time constant τ = 33&nbsp;ms and a gain K = 1.
- Controller: I-PD. The integral term acts on the error. The P and D terms act only on the measured value.
- Goal: the response reaches 98&nbsp;% of the setpoint at 0.7&nbsp;s.

An experienced control engineer reviewed my plan. One suggestion was to start from the simplest controller that meets the goal: pure integral control. With Ki = 4.81, the response reaches 98&nbsp;% at exactly 0.7&nbsp;s.

| Property | Value |
|---|---|
| Integral gain Ki | 4.81 |
| Damping ratio | 1.26 (overdamped) |
| Closed-loop poles | 0.95&nbsp;Hz and 3.87&nbsp;Hz |
| −3&nbsp;dB bandwidth | 0.92&nbsp;Hz |
| Phase margin | 81° at 0.76&nbsp;Hz |
| Overshoot | None |
| Area under the error | 1/Ki = 0.208&nbsp;s |

## Why the spectrum has no peak

The Fourier transform of the response is the product of two parts:

> Y(jω) = T(jω) · R(jω)

T(jω) is the closed-loop frequency response. R(jω) is the transform of the command. For a unit step, R(jω) = 1/(jω).

So the step command alone falls at −20&nbsp;dB per decade, starting from 0&nbsp;Hz. The loop only bends this line down. After the first pole, the slope becomes −40&nbsp;dB per decade. After the second pole, it becomes −60&nbsp;dB per decade.

![The step command alone (dashed) and the step response (solid). Vertical lines mark the poles at 0.95 Hz and 3.87 Hz.](/images/step-spectrum.png)

The step command (dashed line) sets the shape. The closed loop (solid line) only bends the line down after each pole.

A peak appears only if T(jω) has a resonance. With an aggressive gain (Ki = 60), the phase margin drops to 39°, and |T| has a peak of 3.6&nbsp;dB at 5.9&nbsp;Hz. The reference design has no peak.

There is a second problem. A step response does not return to zero, so a finite record cuts it off at the end. The FFT of that record also includes the cut.

## Differentiate first

The derivative removes the step. Because y(0) = 0, the transform of dy/dt is the closed-loop frequency response itself:

> F{dy/dt} = T(jω)

dy/dt also decays to zero, so a finite record contains all of it.

![The FFT of dy/dt (dashed) lies on the theoretical closed-loop response (grey). The −3 dB point is at 0.92 Hz.](/images/dydt-spectrum.png)

The FFT of dy/dt (dashed line) lies on the theory (grey line). Below 5&nbsp;Hz, the largest difference is 0.007&nbsp;%.

The error e(t) = 1 − y(t) also decays to zero. Its transform is (1 − T(jω))/(jω). At 0&nbsp;Hz, this value equals the area under the error, which is 1/Ki = 0.208&nbsp;s for pure integral control. This area tells how much flow the step lost while the loop settled.

## Details that make the FFT match the theory

1. Scale the DFT by the sample period Ts. Then Ts · DFT approximates the continuous Fourier transform.
2. Correct for the jump at t = 0. A sum of samples is a rectangle rule. For a signal that starts with a jump, subtract Ts/2 times the first sample. This is the trapezoid rule.
3. Use a rectangular window and a record that is long enough for the signal to decay. I used 4&nbsp;s at 1&nbsp;kHz. At the end of the record, the error was about 5 × 10⁻¹¹. Do not use a window that changes the decay, such as an exponential window.
4. Do not expect zero padding to improve the resolution. I padded the record to 2¹⁶ points, so the FFT bins are 0.015&nbsp;Hz apart. The real resolution is still 1/T_record = 0.25&nbsp;Hz. Zero padding only interpolates between points.
5. Use the Fourier magnitude or the energy spectral density. Do not use the power spectral density. A transient has finite energy, and it does not continue forever.

## What the output FFT cannot tell you

Two other designs also reach 98&nbsp;% at 0.7&nbsp;s, with critical damping (damping ratio 1):

- Design A, with no D term: Kp = −0.450, Ki = 2.292
- Design B, with no P term: Ki = 4.167, Kd = 0.027

After normalization, both designs have the same closed-loop transfer function. The denominator is s² + 16.67s + 69.46, and the numerator is 69.46. So their step responses and their spectra are identical. The FFT of the output cannot tell them apart.

The two designs still behave differently. In I-PD control, the response to the setpoint and the response to a disturbance are two different transfer functions. To compare the designs, look at the valve command u(t), or at the response to a pressure disturbance.

## What I got wrong

- I expected a peak at the "frequency of the flow". A step response has no such peak unless the loop resonates.
- I mixed up phase margin and the frequency content of the signal. Phase margin measures the stability of the loop. Frequency content is a property of a signal. These are different questions.
- I thought that the response had energy up to 10 to 20&nbsp;Hz. That is true only for strict limits. 90&nbsp;% of the energy of dy/dt is below 2.5&nbsp;Hz, 99&nbsp;% is below 6.8&nbsp;Hz, and 99.9&nbsp;% is below 15.3&nbsp;Hz.

## Summary

- The FFT of a step response mostly shows the step: 1/(jω), which falls at −20&nbsp;dB per decade.
- To see the loop, take the FFT of dy/dt. It equals the closed-loop frequency response T(jω).
- The spectrum of the error at 0&nbsp;Hz is the area under the error: 1/Ki for pure integral control.
- The output alone cannot tell apart two controllers that have the same T(jω).

The script that produced these numbers and figures: [step_fft.py](/code/step_fft.py) (Python, with numpy, scipy, and matplotlib).

This model is ideal. In the next post on this topic, I will add what real firmware has: a 4&nbsp;ms control period, computation delay, and a sensor filter.
