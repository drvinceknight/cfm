---
layout: post
title: "Mid module feedback and brief introduction to Combinatorics"
tags:
  - combinatorics
  - about
---

In class today carried out the mid module feedback and briefly introduced the
combinatorics chapter.

Thank you for engaging with this, I'll try and summarize the main points raised
and describe changes I will attempt to make.

You can see a recording of the class [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ef900a31-6934-417b-a1e0-b20c00f7d129)

## Mid module feedback

A number of you mentioned the structure, online class and use of my website as a positive
aspect of the course. Some of you also made some kind comments: thank you.

My speed during class continues to come up. I'll continue to try and do better
there.

One of the main things that a number of you raised that could be improved was
the Friday class. A number of you find the class "pointless".

In the class I explained that I do want to stick to the substructure of every
week where the Friday class is used to review the concepts. I will continue to
do this. **However** I would like to thank a couple of students who came up to
me at the end of class and made some great suggestions of how the Friday class
could be improved. My plan for the Friday class:

- I will start with the quiz as before **but** I will set a 10 minute timer. If
  we have not finished the quiz by then then we will just stop it.
- After this quiz I will solve the coursework like exercise from the handout.
- If there is still time I will solve questions from the exercise sections.

When I got back to my office I noticed I hadn't used the Q&A feature right on
Mentimeter and there were a few questions left:

- Q: Can we see the haircut?
- A: Sure.

- Q: Put the hat back on lil bro.
- A: Not a question but ok.

- Q: If a wood chucker could chuck wood how much wood could a wood chucker chuck if Riggins 'bark'ed?
- A: Easy: Riggins would bark.

- Q: when does this module end?
- A: At the end of next Semester.

- Q: If the moon imploded, would Riggins bark?
- A: Yes: the answer is always that he would bark.

- Q: If you jumped at the same time as Riggins, and Riggins jumped on you then initiated a double jump off of you, would the moon be in danger of a crash landing?
- A: Probably not but wouldn't try it (not because of the moon but because of needing to keep Riggs safe).

- Q: How often do you go out drinking? Of these occasions how often is it with Riggins?
- A: Incredibly rarely.

- Q: Were u her Romeo?
- A: No one called me that but yeah...

- Q: You are the Romeo to the Juliette.
- A: Not a question but: I was...

- Q: If you talk to a hawk could a hawk tuah if you talk tuah - Riggins 2024
- A: Ok?

- Q: If k = p+1 and p=k, in the same system, how does the existence of God not get proved directly??
- A:

```python
import sympy as sym
k = sym.Symbol("k")
p = sym.Symbol("p")
equation = sym.Eq(lhs=k, rhs=p + 1).subs({p: k})
sym.solves
```

- Q: is The Boys the best show?
- A: I haven't seen it...

- Q: just this week my eduroam wifi has been playing up a lot on my phone. pls help pls pls pls
- A: [Sounds like an IT problem.](https://www.cardiff.ac.uk/study/student-life/learning-support/it-services)

## Brief introduction to combinatorics

Here is the notebook I used in class:
[combinatorics.ipynb]({{site.baseurl}}/assets/nbs/2024-2025/combinatorics.ipynb)
