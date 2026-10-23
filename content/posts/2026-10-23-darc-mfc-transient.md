+++
title = 'DARC on PECVD: where the MFC transient lands'
date = 2026-10-23T15:00:00+09:00
draft = false
categories = ["Process"]
tags = ["MFC", "PECVD", "DARC", "Semiconductor process"]
summary = "Our MFC runs on Wonik IPS GEMINI PECVD tools. In a short DARC step, the MFC transient can change both the dose and the gas ratio. This post estimates how much, and what tool makers and fabs want from an MFC because of it."
result = "8&nbsp;s DARC step, plasma on with the flow: the transient costs 2.6&nbsp;% of the SiH₄ dose, and 15&nbsp;% of the film grows at the wrong gas ratio"
+++

Our MFC runs on the GEMINI PECVD system from Wonik IPS. GEMINI deposits anti-reflective coatings, hardmasks, and dielectric films, and it is used for double and quadruple patterning hardmasks in DRAM and logic ([The Elec](https://www.thelec.kr/news/articleView.html?idxno=3265)).

One of those films is the dielectric anti-reflective coating (DARC). It is thin, and its deposition step is short. So the transient of the MFC, which is harmless in a long step, can reach the film. This post estimates how much, explains when it does not matter, and lists what users want from an MFC because of it.

## What DARC is

DARC is a thin silicon oxynitride (SiON) layer under the photoresist. It cancels the light that the layers below would reflect into the resist. To do that, it needs the right thickness and the right optical constants: the refractive index n and the extinction coefficient k.

The gas ratio sets n and k. A higher share of silane (SiH₄) gives a film richer in silicon, with a higher k ([US7144824B2](https://patents.google.com/patent/US7144824B2/en); [US20080132085A1](https://patents.google.com/patent/US20080132085A1/en)).

A public patent gives one example recipe ([US20080132085A1](https://patents.google.com/patent/US20080132085A1/en)). It is not the GEMINI recipe, but it shows the scale:

| Parameter | Example value |
|---|---|
| Gases | SiH₄ 207, N₂O 96, He 1900 (units not stated) |
| Temperature, pressure, RF power | 400&nbsp;°C, 5.5&nbsp;Torr, 120&nbsp;W |
| Deposition time | 8&nbsp;s |
| Thickness | 30&nbsp;nm |

An 8&nbsp;s step is short. For comparison, my MFC loop model settles to 98&nbsp;% in 0.7&nbsp;s.

## Effect 1: the dose

In my [model of the flow loop](/posts/2026-10-23-step-response-spectrum/), the missing area of a step is 1/Ki = 0.208&nbsp;s of flow. I explained why the wafer feels this area in [An MFC’s job](/posts/2026-10-23-what-an-mfc-is-for/).

If the plasma is on from the moment the flow starts, an 8&nbsp;s step loses 0.208/8 = 2.6&nbsp;% of its SiH₄. On a 30&nbsp;nm film, that is about 0.8&nbsp;nm.

A constant loss is not the real problem. The recipe can absorb it with a slightly longer step. The problem is variation. If the missing area changes by ±10&nbsp;% from run to run, the dose changes by ±0.26&nbsp;%, and no recipe can correct that.

## Effect 2: the gas ratio

DARC uses two reactive gases, so it uses two MFCs. Each one has its own transient. Different gases, ranges, and models settle at different speeds. While one gas is ahead of the other, the gas ratio is wrong, and n and k are wrong too.

I simulated two MFCs with these assumptions:

- Gas A settles to 98&nbsp;% in 0.7&nbsp;s. Gas B settles in 1.4&nbsp;s.
- The plasma is on from the flow command, and the step lasts 8&nbsp;s.
- The deposition rate follows the flow of gas A.

![Top: gas A rises faster than gas B. Bottom: the ratio of A to B starts near 1.8 and reaches the target band of ±2 % after about 1.4 s.](/images/charts/darc-ratio.png)

The ratio comes within ±2&nbsp;% of the target only after 1.4&nbsp;s. Under these assumptions, 15&nbsp;% of the film grows while the ratio is off by more than 2&nbsp;%. If gas A is SiH₄, the bottom of the film is richer in silicon than the rest, with a higher n and k than designed.

So for a two-gas film, the speed of each MFC matters less than the match between them. Two MFCs that are slow by the same amount keep the ratio. One fast MFC next to one slow MFC does not.

The script for both effects: [darc_transient.py](/code/darc_transient.py).

## When the transient does not matter

Many single-film PECVD recipes use a stabilization step. The gases flow first, and the plasma turns on only after the flows are stable. Then the transient stays outside the film.

| Recipe style | Does the transient reach the film? |
|---|---|
| Single film with a stabilization step | No, if the step is longer than the slowest MFC |
| Stack switched with the plasma on | Yes, at every switch |
| ALD and short etch steps | Yes. The transient is part of the process |

A stabilization step has a cost. It adds seconds to every wafer, and a tool runs thousands of wafers. So the faster and more predictable the MFCs are, the shorter the stabilization step can be.

## Thermal and pressure-based MFCs

The two main types measure flow in different ways, so they are good at different things.

| | Thermal MFC | Pressure-based MFC |
|---|---|---|
| How it measures | Heat carried by gas through a heated capillary | Pressure before (and after) a fixed restriction, plus temperature |
| Raw sensor speed | Slow: about 5 to 7&nbsp;s to settle; about 1&nbsp;s with model-based compensation | Fast, because pressure sensors are fast |
| Upstream pressure change | Can cause flow spikes far above or below the setpoint, unless compensated | Measured directly, so the controller can correct it |
| Operating condition | Works over a wide pressure range | The critical-flow type needs an inlet pressure above about twice the outlet pressure |
| Gas dependence | Needs gas correction factors | Needs gas data for the flow equation |

Sources: [MKS technical note](https://api.p1.mks.com/mam/celum/celum_assets/resources/TechZ134.pdf) for the thermal sensor; [US5669408A](https://patents.google.com/patent/US5669408A) for the critical-flow pressure type.

In short, a thermal MFC is a good fit for steady flows in long steps, with a stabilization step in front. A pressure-based MFC is a good fit when flows switch often or the supply pressure moves. Many MFCs now add an internal pressure sensor to correct for supply pressure. Our MFC has one.

## What users want

The tool maker and the fab do not buy flow. They buy films that come out the same. From the analysis above and from the industry reports, this is what they ask for:

- **The same transient every time.** One thermal MFC was stepped from 0 to 50&nbsp;% 150 times. Its overshoot ranged from 7 to 17&nbsp;%, and its settling time from 0.7 to 2.85&nbsp;s ([Solid State Technology](https://sst.semiconductor-digest.com/?p=31263), 2011).
- **Matched transients between gases and between units.** Then the gas ratio holds during the transient, and a replaced MFC does not change the film. Industry named interchangeability, for transient flows too, as the most important MFC requirement ([NIST SP 400-101](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication400-101.pdf)).
- **Immunity to pressure changes.** Other channels and chambers share the gas supply.
- **A reading that tells the truth.** In the same 2011 report, an MFC delivered about 5&nbsp;% too little, while its own reading looked normal.
- **A shorter stabilization step.** Fast, matched, repeatable MFCs let the tool maker cut seconds from every wafer.

## What I do not know yet

- The GEMINI DARC recipe: its step time, and whether the plasma turns on with the flow or after a stabilization step.
- How the deposition rate really depends on each gas. My model assumes that it follows one gas.
- The real step responses of the MFCs on each gas line. My model uses an ideal loop.

The next step is a bench test. I will measure the step responses of two MFCs with the real gases and ranges, and compute the ratio error from the data.

## Summary

- DARC is thin, and its step is short. So the MFC transient can reach the film, unless a stabilization step keeps it out.
- In an 8&nbsp;s step with the plasma on from the start, the transient costs 2.6&nbsp;% of the dose.
- The bigger risk is the gas ratio. Two mismatched MFCs grow the first part of the film with the wrong n and k.
- Users want MFCs whose transients are repeatable and matched, so that they can shorten the stabilization step and still get the same film.
