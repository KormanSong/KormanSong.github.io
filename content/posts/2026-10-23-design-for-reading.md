+++
title = 'Blog design: order, not decoration'
date = 2026-10-23T14:00:00+09:00
draft = false
categories = ["Writing"]
tags = ["Design", "Typography", "This blog"]
summary = "This blog was hard to read. I measured why, and studied Dieter Rams, Jony Ive, typographers, and the best technical sites. The lesson: design for reading, and bring order to complex content instead of decorating it."
result = "Line length cut from 83 to 67 characters (ideal: 66)"
+++

The design of a technical blog has one job: to make complex content easy to read. Decoration does not help. Order does. This post explains why my blog was hard to read. It also covers what great designers and typographers say, and the design values that I will follow.

## What great designers say

### Dieter Rams: less, but better

Dieter Rams designed products for Braun for decades. His [ten principles for good design](https://vitsoe.com/gb/about/good-design) are among the most quoted ideas in design. Five of them apply directly to a blog:

- **Good design makes a product useful.** A blog is used for reading. Everything else comes second.
- **Good design makes a product understandable.** At best, it is self-explanatory. The reader should never wonder where to look next.
- **Good design is unobtrusive.** The design should step back and let the content speak.
- **Good design is thorough down to the last detail.** In his words: "Nothing must be arbitrary or left to chance."
- **Good design is as little design as possible.** His summary is three words: "Less, but better."

### Jony Ive: simplicity is order

Jony Ive led design at Apple for many years. When he introduced iOS 7 in 2013, he described simplicity like this:

> "True simplicity is derived from so much more than just the absence of clutter and ornamentation."

He said that simplicity is about "bringing order to complexity" ([TechRadar](https://www.techradar.com/pro/quote-of-the-day-by-former-apple-design-chief-jony-ive-true-simplicity-is-derived-from-so-much-more-than-just-the-absence-of-clutter-and-ornamentation-laying-the-foundation-for-a-timeless-design-philosophy)).

This matters for a technical blog. My posts are about control loops, signals, and gas flow. I cannot make the content simple by removing parts of it. I can only put it in order: a clear path through the text, and each figure next to the paragraph that it explains.

In a 2025 conversation at [Stripe Sessions](https://stripe.com/sessions/2025/a-conversation-with-sir-jony-ive), Ive also talked about care. He described cabinet makers who finish the inside of a cabinet that nobody will see, and said: "A mark of how evolved we are as people is what we do when no one sees" (as recorded in [Jim Nielsen's notes](https://blog.jim-nielsen.com/2025/notes-from-interview-with-jony-ive/)). On a web page, the inside of the cabinet is the alt text, the line breaks, and the dark mode.

## What typographers say

Typography is the most important design decision for a site that people read. Two references give clear numbers:

| Measure | Matthew Butterick | Robert Bringhurst |
|---|---|---|
| Characters per line | 45 to 90 | 45 to 75, with 66 as the ideal |
| Text size on the web | 15 to 25 pixels | |
| Line spacing | 120 to 145&nbsp;% of the text size | |

Butterick's first rule is that "body text comes first": the quality of a document depends mostly on how its body text looks ([Practical Typography](https://practicaltypography.com/typography-in-ten-minutes.html)). Bringhurst's numbers come from *The Elements of Typographic Style* ([quoted here](https://webtypography.net/2.1.2)).

## What the best technical sites do

- **Bartosz Ciechanowski** writes long explanations of how things work, such as [GPS](https://ciechanow.ski/gps/). His interactive diagrams sit right next to the text that they explain.
- **Edward Tufte's** handouts are simple, with well-set text, notes in the margin, and charts that are part of the text. [Tufte CSS](https://github.com/edwardtufte/tufte-css) brings this style to the web.
- **Gwern Branwen's** site is built on minimalism, good typography, black and white, and notes in the margin. It also keeps archives of the pages it links to, so that its links keep working ([Design](https://gwern.net/design)).
- **Julia Evans** says honestly what she knows and what she does not know. She writes the post that she wished she had when she started ([Blogging principles](https://jvns.ca/blog/2017/03/20/blogging-principles/)).

None of these sites uses decoration. All of them use order: a strong column of text, and figures exactly where the reader needs them.

## What was wrong with this blog

I measured the post pages in a browser.

![The old design. A narrow date column sits on the left, and the text column starts far to the right. Three labels with summary text come before the article.](/images/design-before.png)

1. **The lines were too long.** On a wide screen, a line had 83 characters on average, and up to 89. That is above Bringhurst's range of 45 to 75.
2. **The text was off center.** A left column held only the date and the reading time. The text column started far to the right of the screen center.
3. **The summary was hard to read.** Its labels sat in a side column. On a phone, that left about 30 characters per line for the text. The summary also had the same visual weight as the article.
4. **Charts were too small and too bright.** They had the same width as the text, so their labels were small. In dark mode, they were bright white rectangles.

## My design values

1. **Reading comes first.** Every design decision starts with the body text.
2. **Order, not decoration.** One column, a clear hierarchy of headings, and each figure next to its paragraph.
3. **As little design as possible.** One typeface family, shades of grey, and one status color. No animation, and no JavaScript.
4. **Care in the details that nobody sees.** A number never breaks away from its unit. Every figure has a text description. Charts follow dark mode.
5. **Honesty.** Every number comes with its conditions. Each post says what I got wrong.
6. **Long life.** Plain HTML and CSS, and no design trends that will look old next year.

## The changes

I built a new layout, measured it, and applied it to this site:

![The new design. One centered column. The date sits above the title, and the summary labels sit above their text.](/images/design-after.png)

| | Before | After |
|---|---|---|
| Characters per line on a wide screen | 83 on average | 67 on average |
| Text size | 17 pixels | 18 pixels (17 on phones) |
| Layout | A date column and a text column | One centered column, with the date above the title |
| Summary | Labels in a side column | Labels above the text, with a thin line on the left |
| Charts | Text width, white in dark mode | Up to 46 rem wide, and inverted in dark mode |

Later, I plan two more changes. Sources will go into notes in the margin on wide screens, as Tufte and Gwern do. Charts will become SVG files, so that they follow the page colors exactly.

## What I got wrong

- I first set the line length for Korean text: about 36 Korean characters per line. When I rewrote the blog in English, I did not measure the line length again. The same width held 83 English characters.
- I designed the date column from an idea, a page in a lab notebook. I did not design it from the needs of a reader.

## Summary

- Design a technical blog for reading. Body text comes first.
- Simplicity is not removing things. It is bringing order to complex content.
- Use measured limits: about 45 to 75 characters per line, with 66 as the ideal.
- Care shows in the details that nobody sees.
