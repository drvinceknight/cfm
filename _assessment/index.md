---
layout: default
tag: assessment
---

# Individual coursework (50%)

**The individual coursework is available:
[here]({{site.baseurl}}/assets/assessment/2023-2024/assignment.ipynb) ([cy]({{site.baseurl}}/assets/assessment/2023-2024/cy/assignment.ipynb)).**

A mock coursework is available:
[here]({{site.baseurl}}/assets/assessment/mock/assignment.ipynb).

The topics for the individual coursework for the past few years have been:

- 2023-2024 [here]({{site.baseurl}}/assets/assessment/2023-2024/ind/assignment.ipynb) ([cy]({{site.baseurl}}/assets/assessment/2023-2024/ind/cy/assignment.ipynb)) ([solution]({{site.baseurl}}/assets/assessment/2023-2024/ind/assignment.ipynb))
  1. [Differential equations]({{ site.baseurl }}/topics/differential-equations.html)
  2. [Algebra]({{ site.baseurl }}/topics/algebra.html)
  3. [Sequences]({{ site.baseurl }}/topics/sequences.html)
  4. [Matrices]({{ site.baseurl }}/topics/matrices.html)
- 2022-2023:
  1. [Sequences]({{ site.baseurl }}/topics/sequences.html)
  2. [Probability]({{ site.baseurl }}/topics/probability.html)
  3. [Algebra]({{ site.baseurl }}/topics/algebra.html)
  4. [Matrices]({{ site.baseurl }}/topics/matrices.html)
- 2021-2022:
  1. [Matrices]({{ site.baseurl }}/topics/matrices.html)
  2. [Sequences]({{ site.baseurl }}/topics/sequences.html)
  3. [Matrices]({{ site.baseurl }}/topics/matrices.html)
  4. [Calculus]({{ site.baseurl }}/topics/calculus.html)
- 2020-2021:
  1. [Probability]({{ site.baseurl }}/topics/probability.html)
  2. [Combinatorics]({{ site.baseurl }}/topics/combinatorics.html)
  3. [Calculus]({{ site.baseurl }}/topics/calculus.html)
  4. [Sequences]({{ site.baseurl }}/topics/sequences.html)
- Mock [here]({{site.baseurl}}/assets/assessment/mock/assignment.ipynb):
  1. [Arithmetic]({{ site.baseurl }}/topics/using-notebooks.html)
  2. [Algebra]({{ site.baseurl }}/topics/algebra.html)
  3. [Matrices]({{ site.baseurl }}/topics/matrices.html)
  4. [Probability]({{ site.baseurl }}/topics/probability.html)

# Group project (50%)

Build a Python library to provide tools for a problem related to mathematics.

You will evidence your progress with 2 mediums:

2. A 2 page paper
3. A 15 minute recorded presentation

Your final submission should include the following **7** files:

1. A `main.tex` file: the source file for a 2 page paper written in [LaTeX](({{ site.baseurl }}/topics/latex.html)
   ).
2. A `main.pdf` file: the pdf file for a 2 page paper written in [LaTeX](({{ site.baseurl }}/topics/latex.html)
   ).
3. A `<library>.py` file: the [source file for your Python library]({{ site.baseurl }}/topics/modularisation-of-code.html)
4. A `test_<library>.py` file: [the test files for your Python library]({{ site.baseurl }}/topics/testing-of-code.html)
5. A `README.md` file: [the documentation for your Python library]({{ site.baseurl }}/topics/documentation-of-code.html)
6. A `presentation.mp4` (or similar file format): the video recording of [your 15 minute presentation]({{ site.baseurl }}/topics/presenting-mathematics.html)
7. A `contribution.md` file: a file describing the contributions of every member of your group.

## [Marking criteria](#marking-criteria)

The various components of the submission should aim to demonstrate how the following
aspects of the work have been addressed:

- **Summary**: Has a clear description of the high-level functionality and
  purpose of the software for a diverse, non-specialist audience been
  provided?
- **A statement of need**: Do the authors clearly state what problems the
  software is designed to solve and who the target audience is? [10%]
- **State of the field**: Do the authors describe how this software compares
  to other commonly used packages?
- **Quality of writing**: Is the paper well written (i.e., it does not
  require editing for structure, language, or writing quality)?
- **References**: Is the list of references complete, and is everything
  cited appropriately that should be cited (e.g., papers, datasets,
  software)? Do references in the text use the proper citation syntax?
- **Functionality**: Have the functional claims of the software been
  confirmed?
- **Documentation**: Does the documentation have a Tutorial, How to section,
  Reference and Explanation section? Is it clear? Is the source code clear?
- **Modularity**: Is the code written in a modular way?
- **Testing**: Have tests been written for all functionality of the software?
- **Presentation**: Was the presentation format used appropriately? Were the
  visual aids appropriate?

A suggestion would be to use the paper for the **summary**, **statement of need** and **state
of the field** whereas the presentation can be used for the **functionality**, **documentation**, **modularity**
and **testing**.

Note that this marking criteria has some overlap with the review criteria
for the Journal of Open Source Software
<https://joss.readthedocs.io/en/latest/review_checklist.html>. Some examples
of papers written for that journal that can be helpful are:

- Matching: A Python library for solving matching games <https://joss.theoj.org/papers/10.21105/joss.02169>
- Nashpy: A Python library for the computation of Nash equilibria <https://joss.theoj.org/papers/10.21105/joss.00904>

## [Past group projects](#past-group-projects)

A list of titles of past projects:

{% for year in site.data.projects %}

### {{ year.year }}

{% for title in year.titles %}

- {{ title }}
  {% endfor %}
  {% endfor %}

## [Log of past relevant classes](#log-of-past-relevant-classes)

{% for post in site.posts %}
{% if post.tags contains page.tag %}
[{{post.date | date: "%D"}}: {{ post.title }}]({{site.baseurl}}{{post.url}})
{{ post.excerpt }}
{% endif %}
{% endfor %}
