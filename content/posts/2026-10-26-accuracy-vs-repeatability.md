+++
title = 'Accuracy vs repeatability: why a fab picks repeatability'
date = 2026-10-26T05:00:00+09:00
draft = false
categories = ["Process"]
tags = ["MFC", "Metrology", "Specifications"]
summary = "A flow meter can be biased and still be useful, if it is biased the same way every time. This post fixes the terms, ranks the four classic targets from a process point of view, and reads a real MFC spec at low flow."
result = "MARU7000 spec at a 2&nbsp;% setpoint: ±12.5&nbsp;% of reading. A constant bias is corrected once; scatter never"
+++

A process engineer can correct a bias once, but can never correct scatter. So for a mass flow controller (MFC) in a fab, repeatability comes before accuracy. This post fixes the terms and ranks the classic targets from the process side. Then it adds two dimensions that the targets leave out, and reads a real MFC spec at low flow.

It starts from a good introduction by Bronkhorst, [Understanding Flow Meter Accuracy & Repeatability](https://www.bronkhorst.com/knowledge-base/flow-meters-accuracy-repeatability/). I redrew its figures and extended them.

## The terms

The International Vocabulary of Metrology (VIM) separates three ideas that people often mix:

| Term | Meaning | Error type |
|---|---|---|
| Trueness ([VIM 2.14](https://jcgm.bipm.org/vim/en/2.14.html)) | How close the average of many readings is to the reference | Systematic error (bias) |
| Precision ([VIM 2.15](https://jcgm.bipm.org/vim/en/2.15.html)) | How close repeated readings are to each other | Random error (scatter) |
| Accuracy ([VIM 2.13](https://jcgm.bipm.org/vim/en/2.13.html)) | How close one reading is to the true value | Both |

Precision depends on the conditions. Under repeatability conditions, everything stays the same: the same procedure, operator, system, and place, over a short time ([VIM 2.20](https://jcgm.bipm.org/vim/en/2.20.html)). Under reproducibility conditions, the location, operator, or measuring system changes ([VIM 2.24](https://jcgm.bipm.org/vim/en/2.24.html)).

The VIM warns that "accuracy" should not be used for trueness. The Bronkhorst article does exactly that in one figure. It labels scattered shots around the center as "accurate". In VIM terms, those shots are true on average, but imprecise.

## Four targets, ranked by a process engineer

![Four targets. 1: tight group in the center. 2: tight group away from the center. 3: loose group around the center. 4: loose group away from the center.](/images/charts/targets.png)

A metrologist ranks the first target best and calls the other three bad. A process engineer ranks them differently, because a recipe can correct a constant bias:

| Target | What the recipe can do | Rank for a process |
|---|---|---|
| True + precise | Nothing to correct | 1 |
| Biased + precise | Correct the bias once, for example with a step time of 10.2&nbsp;s instead of 10&nbsp;s | 2 |
| True on average + imprecise | Nothing. Each run is different | 3 |
| Biased + imprecise | Nothing | 4 |

The second target beats the third. This is the same idea as in [An MFC’s job](/posts/2026-10-23-what-an-mfc-is-for/): the user does not need zero error, but the same error every time. Bronkhorst makes the same point from the metrology side: high repeatability is possible without high accuracy, but not the other way around.

## Two dimensions the targets leave out

Each classic target shows one unit at one moment. A fab cares about two more dimensions.

![Left: one unit over a year. Its tight group moves away from the center from month 1 to month 12. Right: three units on one day. Each unit has a tight group, but in a different place.](/images/charts/drift-targets.png)

- **Time.** A unit can be precise every day, but its group moves over months. The VIM calls this instrumental drift ([VIM 4.21](https://jcgm.bipm.org/vim/en/4.21.html)). The recipe absorbed the bias of month 1, so in month 12 the bias is new, and nobody has corrected it.
- **Units.** Ten units of the same model can each be precise, with ten different biases. When one unit replaces another, the recipe breaks. This is why industry named interchangeability as the most important MFC requirement ([NIST SP 400-101](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication400-101.pdf)).

So a bias is correctable only while it stays constant. Drift turns bias into scatter on a slow time scale. Unit-to-unit differences turn bias into scatter across a fleet of tools.

## Full scale and reading

An accuracy spec is a percentage of something. A percentage of reading (Rd) scales with the flow. A percentage of full scale (F.S.) is a fixed amount of flow, so it becomes large compared with a small flow.

The MARU7000 series from MKP specifies:

- ±1&nbsp;% of reading at 25&nbsp;% F.S. and above
- ±0.25&nbsp;% F.S. below 25&nbsp;% F.S.

The two limits meet at 25&nbsp;% F.S., where 0.25&nbsp;% F.S. equals 1&nbsp;% of reading. Below that, the limit in % of reading is 0.25 / setpoint × 100:

![The error limit in percent of reading against the setpoint. It is 1 % from 25 to 100 % F.S., and rises to 2.5 % at 10 % F.S., 5 % at 5 % F.S., and 12.5 % at 2 % F.S.](/images/charts/spec-error.png)

| Setpoint | Error limit |
|---|---|
| 25 to 100&nbsp;% F.S. | ±1&nbsp;% of reading |
| 10&nbsp;% F.S. | ±2.5&nbsp;% of reading |
| 5&nbsp;% F.S. | ±5&nbsp;% of reading |
| 2&nbsp;% F.S. | ±12.5&nbsp;% of reading |

These are pamphlet values, and they are limits, not typical errors.

Bronkhorst explains the F.S. form as a habit from mechanical dials. There is also a physical reason. The zero offset and the noise of a flow sensor are fixed amounts of flow, in sccm. They do not shrink when the setpoint shrinks. So at low flow, the error naturally takes the F.S. form. For example, a zero shift of 0.045&nbsp;% F.S. caused a 1.1&nbsp;% flow error at a 4&nbsp;% setpoint in one field case ([Brooks Instrument](https://www.crossco.com/wp-content/uploads/2020/03/brooks-instrument-whitepaper-a-new-class-of-mfcs-with-embedded-flow-diagnostics.pdf), 2016).

This is why a better signal-to-noise ratio and a more stable zero extend the usable range downward. They shrink the F.S. term, which dominates at low flow.

One note on the original figure: the Bronkhorst error chart labels its vertical axis 15, −10, 5, 0, −5, 10, −15. The signs are mixed up, although the curves are right. My redrawn chart shows the limit as a positive ± value.

## Repeatability of the transient

A spec sheet states repeatability for steady flow. But the wafer feels each step as a dose, including the missing area of the transient ([previous analysis](/posts/2026-10-23-step-response-spectrum/)).

So each shot on the target can also be one step's dose. If the missing area changes by ±10&nbsp;% from run to run, an 8&nbsp;s step changes by ±0.26&nbsp;% ([DARC analysis](/posts/2026-10-23-darc-mfc-transient/)). That scatter appears on no spec sheet, and no recipe can correct it.

## How to test each property

| Property | Test | Report |
|---|---|---|
| Repeatability | One unit, the same setpoint and conditions, N repeated readings within a short time | Standard deviation, % of reading |
| Drift | The same test, repeated over weeks or months | Change of the mean over time |
| Unit to unit | Several units of the same model, the same reference, the same day | Spread of the unit means |
| Accuracy | Readings against a reference flow standard | Error, plus the uncertainty of the reference |
| Transient repeatability | N identical steps | Spread of the missing area |

I do not have these measurements yet. The next post on this topic will report them for real units.

## What I got wrong

- I used "accuracy" for the average error and "repeatability" for everything else. The VIM terms are cleaner: trueness for bias, precision for scatter, accuracy for both.
- I thought that a precise unit is enough. It is enough only while its bias stays constant over time and across units.

## Summary

- Trueness is about bias. Precision is about scatter. Accuracy needs both.
- A process can correct a constant bias once, but never scatter. So repeatability comes first.
- Drift and unit-to-unit differences turn bias into scatter, over time and across tools.
- An F.S. spec grows fast at low flow: the MARU7000 limit is ±12.5&nbsp;% of reading at a 2&nbsp;% setpoint. The sensor zero and noise set that limit.

Figures: [accuracy_figures.py](/code/accuracy_figures.py).
