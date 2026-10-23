+++
title = 'One talk, three versions: How to Speak in practice'
date = 2026-10-23T12:20:00+09:00
draft = false
categories = ["Writing"]
tags = ["Communication", "Presentations", "MFC"]
summary = "I built one talk about mass flow controllers three times, using the rules of Patrick Winston's How to Speak. The rules gave the talk its structure. The audience decided its final form."
result = "Slide text cut from about 207 to 77 characters; customer problems first"
+++

Patrick Winston taught a famous MIT lecture called [How to Speak](https://ocw.mit.edu/courses/res-tll-005-how-to-speak-january-iap-2018/). I used its rules to build one talk about mass flow controllers (MFCs), three times. The rules gave the talk a clear structure. The audience decided its final form.

## The rules I used

- **Start with a promise.** Tell the audience what they will know at the end that they do not know now.
- **Say the main point three times.** At any moment, part of the audience is not listening.
- **Build a fence.** Say what your idea is not, so that nobody confuses it with a similar idea.
- **Mark the structure out loud.** Then people who drifted away can come back.
- **Ask a question, and wait.** Winston suggests about seven seconds.
- **Keep slides light.** Slides show things. The speaker explains them. Use few words, large text, and never read the slides aloud.
- **Show that you have done something,** not only that you have an idea.
- **Make the idea memorable.** Winston's "star" has five parts: a symbol, a slogan, a surprise, a salient idea, and a story.
- **End with your contributions.** Do not end with "Thank you" or "Any questions?".

## Version 1: a pure Winston talk

The first version was in Korean and had 11 slides. Each slide had one picture and a few words. I planned to say everything else.

The talk followed one story in three parts:

1. The common definition of an MFC, and what the wafer actually feels.
2. Why the same dose matters: integration, repetition, the moments when users say "Huh?", overshoot, and the environment.
3. The answer: the split of work with the tool maker, four new spec lines, and a new definition.

I wrote this story as a post: [An MFC’s job: same command, same dose](/posts/2026-10-23-what-an-mfc-is-for/).

For example, the slide "What does the wafer feel?" showed only a chain of four boxes: MFC, pipe, chamber, and wafer. The point of the slide was in what I said.

## Version 2: Winston's structure in English

The second version was in English and had 23 slides. It used two of Winston's devices.

First, a slide called "The way forward" listed three hypotheses: the spec-sheet hypothesis, the wafer hypothesis, and the sameness hypothesis. The same slide came back near the end, so that the audience could see the whole path at once.

Second, the last slide listed the contributions:

- a definition of an MFC that the wafer would agree with
- four new lines for the spec sheet
- a short test for each line

This is how the talk used Winston's star:

| Part | In this talk |
|---|---|
| Symbol | Two posts and a beam: "accurate" and "fast" are the posts, "the same way" is the beam |
| Slogan | The same command, the same dose |
| Surprise | The wafer cannot tell an MFC that settles in 0.7&nbsp;s from one that settles in 0.3&nbsp;s |
| Salient idea | Sameness |
| Story | Three hypotheses, in the order that I found them |

## Version 3: the final talk for an equipment maker

The final version was in Korean and had 22 slides. The audience changed: engineers at an equipment maker who would decide whether to use our MFC. When I reviewed the first two versions with this audience in mind, I found these problems:

| Problem | What I changed |
|---|---|
| The tone sounded dramatic. | I used the tone of a Korean business report: short statements, bullet points, and numbers first. |
| The audience could not see which MFC was better for them. | I rebuilt the talk around four problems that customers have with MFCs. |
| The value of a better signal-to-noise ratio was not clear. | I connected it step by step to something the customer measures: the dose lost during a pressure change. |
| The number "2&nbsp;%" was misunderstood. | I added a fence slide that says what "2&nbsp;%" means and what it does not mean. |
| The slides had too many words. | The average slide went from about 207 characters to about 77. The rest moved into the speaker notes. |
| There was no picture of the equipment. | I added a simple layout of the tool, a diagram of the gas box, and a gas sequence from a public patent. |

The four customer problems were these:

1. After an MFC is replaced, the recipe must be tuned again.
2. The same step gives a different transient in each run.
3. Accuracy is poor at low flow.
4. When a nearby channel or chamber starts, the pressure changes, and the dose changes with it.

The fence slide was necessary. To one group, "2&nbsp;%" meant a settling band of ±2&nbsp;%. We meant something else: extending the control range below its usual lower limit of 2&nbsp;% of full scale.

## What stayed from Winston in the final version

The format changed, but Winston's rules for attention stayed:

- **Promise.** The talk opened with what the audience would be able to explain in numbers at the end.
- **Repetition.** A three-line summary came at the start and again at the end, in the same words.
- **Fence.** One slide fixed the meaning of "2&nbsp;%".
- **Something done.** One slide was kept for measured data. The measurements were still in progress.
- **A question and a pause.** Before the low-flow chart, I planned to ask: "At 2&nbsp;% of full scale, how large is the error compared with the setpoint?" Then I would wait a few seconds.
- **One hard slide.** One slide had the equations, to show the depth behind the simple slides.
- **The last slide.** The conclusion stayed on the screen during the questions.

From the business report format, I kept five rules:

- Each slide title is a full sentence that states the point.
- Each slide has one message.
- Sources go in a footnote at the bottom of the slide.
- Details go in an appendix.
- What I say goes in the speaker notes, not on the slide.

## What I got wrong

- I thought that a good definition would persuade the audience on its own. The customer first needed to see their own problems.
- I thought that "2&nbsp;%" was clear. It meant two different things to two groups.
- I put too many words on my first slides. When I cut them, I had to decide exactly what I would say.

## Summary

- Winston's rules are about attention: a promise, repetition, a fence, a pause, and an ending on contributions. They work in any format.
- The order and the tone must fit the audience. The first version was about my insight. The final version was about the customer's problem, with the same facts.
- When a number can be read in two ways, build a fence for it.

This blog uses the same rules. Each post states its main idea first, repeats it in the summary list and at the end, and includes what I got wrong.
