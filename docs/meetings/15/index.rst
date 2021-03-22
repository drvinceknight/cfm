Writing
=======

First meeting
-------------

After this meeting students should:

- Understand how to use LaTeX
- Have access to guidance on writing


In class discussion
-------------------

Discuss how they already have seen an example a markup language: LaTeX.

In fact: they have already seen some LaTeX.

Open up a local editor (do not feel obliged to use VS Code) and show to a LaTeX
document can be compiled.

Then show that this is how they are expected to write their paper.

Specifically type the following::

    \documentclass[a4paper]{article}

    % Set up page size
    \usepackage[margin=1.5cm, includefoot, footskip=30pt]{geometry}

    % Nice way to display code
    \usepackage{minted}

    % Import images

    \title{The TSP Package}
    \author{Vince Knight}
    \date{}


    \begin{document}
    \maketitle

    \section{Introduction:The TSP}

    \end{document}

Open overleaf and show how this can be used to write LaTeX.

Show them the following two guidelines for writing:

- https://vknight.org/cfm/assets/pdf/writing-mathematics-guidelines/main.pdf
- https://vknight.org/cfm/assets/pdf/a-guide-to-writing-mathematics/main.pdf

Use breakout rooms/groups and ask students to spend 5/10 minutes finding
something specifically useful in there.

After breakout rooms ask all students to write down those things in a shared
medium (for example the class discord).

After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over automated writing mathematics. We discuss this
    from a technical point of view (how to use LaTeX) and I refer you to my
    notes on that: https://vknight.org/tex/

    We also discussed guidelines for better writing:

    - https://vknight.org/cfm/assets/pdf/writing-mathematics-guidelines/main.pdf
    - https://vknight.org/cfm/assets/pdf/a-guide-to-writing-mathematics/main.pdf

    On Friday the mathematics subject librarian will take the class to discuss
    finding good sources for your paper (which is specifically a point in the
    marking criteria).

    Please get in touch if I can assist with anything,
    Vince
