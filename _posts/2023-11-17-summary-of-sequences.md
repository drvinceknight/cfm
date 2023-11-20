---
layout: post
title: "Summary of Sequences"
tags:
  - sequences
---

In class today I we went over the Sequences chapter.

You can see a recording of the class [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=1ec057b2-65ed-4d4d-89bc-b0b800c651b5)

Here is the notebook I used in class:
[sequences.ipynb]({{site.baseurl}}/assets/nbs/2023-2024/sequences.ipynb)

We started with the quiz which was won by Vincent

- Daf: 2 wins
- Anthony: 1 win
- Ben: 1 win
- Joe: 1 win
- Millie: 1 win
- Tom: 1 win
- Vincent: 1 win

During the quiz we spent some time looking at this function which is defined
recursively:

```python
def get_sequence(n):
    """
    ...
    """
    if n == 4:
        return 1
    if n in [1, 2, 3]:
        return n
    return get_sequence(n - 2) + get_sequence(n - 1)
```

During the discussion about what `get_sequence(n=7)` gives I drew the following
on the board:

![]({site.baseurl}/assets/nbs/2023-2024/get_sequence.png)

If we work back from the end points of that image we get:

- `get_sequence(n=3)=3`
- `get_sequence(n=4)=1`

Which in turn gives:

- `get_sequence(n=5)=get_sequence(n=3) + get_sequence(n=4) = 3 + 1 = 4`

Which in turn gives:

- `get_sequence(n=6)=get_sequence(n=4) + get_sequence(n=5) = 4 + 1 = 5`

Which in turn gives:

- `get_sequence(n=7)=get_sequence(n=5) + get_sequence(n=6) = 5 + 4 = 9`
