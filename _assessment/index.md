---
layout: default
tag: assessment
---

# Individual tests (20%)

A series of 6 individual tests. Each test contributes 1/6 of the 20%
test mark.

- Test 1: [Algebra]({{ site.baseurl }}/topics/algebra.html) and [Calculus]({{ site.baseurl }}/topics/calculus.html).
- Test 2: [Combinatorics]({{ site.baseurl }}/topics/combinatorics.html) and [Probability]({{ site.baseurl }}/topics/probability.html).
- Test 3: [Matrices]({{ site.baseurl }}/topics/matrices.html) and [Sequences]({{ site.baseurl }}/topics/sequences.html).
- Test 4: [Statistics]({{ site.baseurl }}/topics/statistics.html) and [Differential Equations]({{ site.baseurl }}/topics/differential-equations.html).
- Test 5: [Variables, conditional statements and while loops]({{ site.baseurl }}/topics/variables-conditional-statements-and-while-loops.html) and [Functions and data structures]({{ site.baseurl }}/topics/functions-and-data-structures.html).
- Test 6: [Object Oriented Programming]({{ site.baseurl }}/topics/object-oriented-programming.html) and [Using a terminal and an editor]({{ site.baseurl }}/topics/using-a-terminal-and-an-editor.html).

You can complete each test as soon as it is released. The deadline for
completing all of them is at the end of the module.

**I recommend you do each quiz as the corresponding content is covered.**
Tests 1–4 cover the tools half of the module; tests 5 and 6 cover the
group-project half. You can attempt each quiz as many times as you wish;
your last attempt is the one that counts.

# Individual coursework (20%)

A mock coursework is available:
[here]({{site.baseurl}}/assets/assessment/mock/mock.ipynb).

Solutions to the mock are [here]({{site.baseurl}}/assets/assessment/mock/mock_solutions.ipynb).

## [Marking criteria](#marking-criteria-individual)

The coursework has 8 questions, each worth 5 marks, for 40 marks in
total. That raw mark is then scaled to the 20% of the module mark that
this component contributes.

+ **3 marks** are awarded for the quality of the **analysis**: This means the correctness and the appropriateness of the code.
  - *0 marks*: Code that does not answer the question
  - *1 marks*: Code that partly answers the question correctly
  - *2 marks*: Code that mostly answers the question correctly
  - *3 marks*: Code that answers the question correctly
+ **2 marks** are awarded for the quality of the **communication**: this means the narrative and story given by words (if appropriate for the question), and the clarity of the code including using sensible variable names.
  - *0 marks*: No narrative given
  - *1 marks*: An attempt at some narrative and readable code
  - *2 marks*: Clear narrative, clear code with descriptive variable names


The coursework for 2025/2026 can be downloaded available [here]({{site.baseurl}}/assets/assessment/ind/assignment.ipynb).



# Group project (60%)

In a small group you build a Python library that provides tools for a
mathematical problem of your choice. A 'problem related to mathematics'
is a deliberately broad brief: every example in the
[Example Group Projects]({{ site.baseurl }}/assessment/example-projects/)
listing is one valid answer, and your own project does not need to look
like any of them. Every component is graded; you do not need to be the
strongest coder in the group to earn full marks on the project, since
the paper, the documentation, the tests, and the meeting minutes are
all marked too.

In one sentence: 60% of your project mark comes from the marking
criteria below (split as Communication 30%, Scope 50%, Research 20%),
and the geometric mean with your engagement record then ties your
individual mark to both your contribution and the group's output.

## [Marking scheme](#marking-scheme)

We combine two distinct components using a geometric mean:

\[\text{Final mark} = \sqrt{M \times E}\]

where \(M \in [0, 100]\) is the individual **measurable contribution
score** (in plain English, your engagement record: being present *and*
contributing to the meeting, as evidenced by the minutes), and
\(E \in [0, 100]\) is the shared **effective contribution score** (in
plain English, the mark your group's submission gets). Both dimensions
must be strong for a high final mark to be possible. A student who
attends consistently but whose group produces weak work, or who
free-rides on a strong group, cannot receive full credit.

### Component 1: Measurable contribution score (M)

M is individual, derived from the engagement record in each week's
meeting minutes. The group submits one set of minutes per week during
the contact hour; a different member acts as secretary each week (the
group agrees the rota at its first meeting). The minutes record both
who was present and what each member contributed, so M rewards
**meaningful participation**, not just attendance: turning up without
engaging does not score, and a member who was unwell but caught up
through the week's minutes and asynchronous contributions can still
be recorded as engaged.

A student's score is the fraction of the five group meeting weeks
(Weeks 6 to 10) at which the minutes record them as having engaged:

\[M = \frac{\text{number of meetings at which the student is recorded as engaged}}{5} \times 100\]

The minutes template for each week is linked in the schedule.

### Component 2: Effective contribution score (E)

E is shared equally among all group members. It is the mark awarded to
the group project submission, assessed against the criteria below.

### [Marking scenarios](#marking-scenarios)

Three [group-project marking scenarios]({{ site.baseurl }}/assessment/geometric-mean/)
(the free rider, the conscientious student in a struggling group, and
a well-functioning group) are on a dedicated page; they are the
clearest way to see why both \(M\) and \(E\) matter.

#### [Marking criteria](#marking-criteria)

The various components of the submission should aim to demonstrate how the
following aspects of the work have been addressed:

##### Communication (both paper and presentation) (30%)

- **Summary**: Has a clear description of the high-level functionality and
  purpose of the software for a diverse, non-specialist audience been
  provided?
- **A statement of need**: Do the authors clearly state what problems the
  software is designed to solve and who the target audience is?
- **Quality of writing**: Is the paper well written (i.e., it does not
  require editing for structure, language, or writing quality)?
- **Functionality**: Have the functional claims of the software been
  confirmed?
- **Presentation**: Was the presentation format used appropriately? Were the
  visual aids appropriate?

Typical description of mark:

- Below 40%

  Difficult to read and lacks a logical train of thought or argument. Very poor
  organisation and communication of work.

- Between 40 and 49%

  Poor style of writing with some parts difficult to follow. Poor organisation
  and presentation of material.

- Between 50 and 59%

  Satisfactorily written and presented with adequate technical content.

- Between 60 and 69%

  Well organised and clearly written with sound technical content. Results
  analysed and clearly presented.

- Above 70%

  Very well organised and clearly written with good technical content. Results
  assessed critically and arguments very well presented and supported. At
  the *exemplary* end of this band the paper would not look out of place in
  a Journal of Open Source Software submission, and the presentation lands
  the high-level idea, the design choices, and the limitations in 15 minutes
  without rushing.

##### Scope (50%)

- **Documentation**: Does the documentation have a Tutorial, How to section,
  Reference and Explanation section? Is it clear? Is the source code clear?
- **Modularity**: Is the code written in a modular way?
- **Testing**: Have tests been written for all functionality of the software?

Typical description of mark:

- Below 40%

  The work does not correspond to the project description.

- Between 40 and 49%

  The library includes documentation, some modular functionality and an attempt
  at automatic testing.

- Between 50 and 59%

  The documentation follows the Diataxis framework although it is poorly
  written. The code is modular but has a number of areas of improvement. The
  tests have been written and test some functionality of the code.

- Between 60 and 69%

  The documentation is clear. The code is written in a modular way with few
  areas of improvement. The tests confirm most functionality of the code and
  the documentation.

- Above 70%

  Well written documentation, code is modular and follows all conventions and
  guidelines covered in the course. The tests cover all functionality of the
  code and the documentation. At the *exemplary* end of this band the test
  suite includes edge cases that the tutorial does not exercise, and the
  README would be usable by someone outside the group with no extra help.

##### Research (20%)

- **State of the field**: Do the authors describe how this software compares
  to other commonly used packages?
- **References**: Is the list of references complete, and is everything
  cited appropriately that should be cited (e.g., papers, datasets,
  software)? Do references in the text use the proper citation syntax?

Typical description of mark:

- Below 40%

  No state of the field or references included.

- Between 40 and 49%

  An inaccurate state of the field included. Some poor references included.

- Between 50 and 59%

  An accurate state of the field included. Good references included but with
  little to no context and/or explanation.

- Between 60 and 69%

  A well written state of the field and good references with context and depth.

- Above 70%

  Outstanding state of the field demonstrating a great understanding not only
  of the library but of the already existing tools. The references are all of
  high quality and a thorough demonstration of understanding is given. At
  the *exemplary* end of this band the references are integrated into the
  prose, not relegated to a bibliography that the body never refers back to.

Note that this assessment has some overlap with the review criteria for the
Journal of Open Source Software
<https://joss.readthedocs.io/en/latest/review_checklist.html>. Some examples
of papers written for that journal that can be helpful are:

- Matching: A Python library for solving matching games
  <https://joss.theoj.org/papers/10.21105/joss.02169>
- Nashpy: A Python library for the computation of Nash equilibria
  <https://joss.theoj.org/papers/10.21105/joss.00904>

## Groups

Groups of four are in place by the time the group-project half of the
module begins. Groups are **self-selecting**: form a group of four with
people you want to work with and register it before the deadline. Any
student who has not joined a self-selected group by the deadline is
randomly assigned to a group with the other unassigned students. The
incentive is straightforward: a self-selected group is one in which
every member has chosen to engage, while a randomly assigned group is
likely to contain other students who have not yet committed to the
project.

At the first meeting the group agrees the **secretary rota**: a different
member is secretary each of the five meeting weeks (Weeks 6 to 10),
which spreads the minute-taking workload and gives each member a turn at
documenting the work.

If a group member is unresponsive or disengaged for two consecutive
meetings, raise it at the next meeting and record it in the minutes;
the geometric mean already penalises lack of engagement, but flagging
it early gives the rest of the group time to redistribute work and
gives the disengaged member a chance to re-engage.

## Submission

Your final submission should include the following **7** files. Every
component is graded, so a strong submission needs strong work across
all of them; you do not need to be the most experienced coder in the
group to earn full marks if you have written the paper, drafted the
README, or built out the test suite.

1. A `main.tex` file: the source file for a 3 page paper written in
   [LaTeX]({{ site.baseurl }}/topics/latex.html).
2. A `main.pdf` file: the pdf file for a 3 page paper written in
   [LaTeX]({{ site.baseurl }}/topics/latex.html).
3. A `<library>.py` file: the
   [source file for your Python library]({{ site.baseurl }}/topics/modularisation-of-code.html).
4. A `test_<library>.py` file:
   [the test files for your Python library]({{ site.baseurl }}/topics/testing-of-code.html).
5. A `README.md` file:
   [the documentation for your Python library]({{ site.baseurl }}/topics/documentation-of-code.html).
6. A `presentation.mp4` (or similar file format): the video recording of
   [your 15 minute presentation]({{ site.baseurl }}/topics/presenting-mathematics.html).
7. A `contribution.md` file: a file describing the contributions of every
   member of your group.

The submission deadline is confirmed by the end of Week 2 of the module
and posted on the schedule.

## [Example projects](#example-projects)

A set of [worked example projects]({{ site.baseurl }}/assessment/example-projects/)
is available. Each one is a small
Python library with the same files as your submission (library, tests,
`README.md`, and a short paper). They are written at the **'good'**
level of the marking scheme, not the 'exemplary' level: read them as a
model of what a strong submission looks like, not as a ceiling.

## [Use of Code Generation Tools](#use-of-code-generation-tools)


Code generation tools (for example Large Language Models such as ChatGPT or
Google Gemini) are increasingly capable of producing working programming code.
These tools can sometimes generate high-quality solutions, but they can also
produce incorrect, inefficient, or unsafe code.

**The purpose of this module is for you to develop your own programming,
problem-solving, and debugging skills.**

For this coursework, you must submit your own original work.

You must not:

- Submit code that you do not fully understand
- Submit code generated wholly or partially by automated code generation tools
- Use code generation tools to complete assessed programming tasks

You may:

- Use lecture materials, textbooks, and official documentation
- Discuss general programming ideas with others (but not share code)
- Use standard debugging tools
- Ask a language model to explain an error message you have already
  read yourself, or to explain a concept from the textbook in different
  words. The line is between **understanding** and **generating**:
  generating any part of the submitted work with a tool is not allowed,
  but learning faster with one is the same as learning faster with a
  classmate

Automated code generation often produces recognisable artefacts. Where there is
reasonable evidence that submitted work was generated using such tools, the
submission may be treated as an academic integrity violation and penalties may
apply.

**This policy exists to ensure you develop the skills required for later modules
and professional programming practice.**

