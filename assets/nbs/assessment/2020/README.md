# Coursework

This coursework is written to be used with
[nchkr](https://nbchkr.readthedocs.io/en/stable/).

`main.ipynb` is the source document.

To generate the release:

```bash
$ python -m nbchkr release --source main.ipynb --output assignment.ipynb
```

## Notes

Here are specific notes made during the marking of this coursework for specific
files and sampled files.

### Files with mismatched tags

Using

    $ grep "False" data.csv

4 files did not have matching tags:

#### submissions/Coursework_c1902827_attempt_2020-12-17-13-19-20_c1902827.ipynb

This submission was the mock coursework.

#### submissions/Coursework_c2008716_attempt_2020-12-17-11-47-43_c2008716.ipynb

This submission was the mock coursework.

#### submissions/Coursework_c2058903_attempt_2020-12-17-21-13-19_C2058903.ipynb

This submission included some minor errors where instructions were not followed
and/or the wrong calculation was made.

#### submissions/Coursework_c2060061_attempt_2020-12-21-23-22-07_c2060061.ipynb

This submission was the mock coursework.

### Files with below 50% mark

Using:

    import pandas as pd
    df = pd.read_csv("data.csv")
    for _, row in df[(df["Score"] < 18) & df["Tags match"]].iterrows():
        print(row["Submission filepath"])

#### submissions/Coursework_c2009938_attempt_2020-12-22-23-02-18_C2009938.ipynb

This submission was empty. The mark is correct.

#### submissions/Coursework_c2034522_attempt_2020-12-22-04-32-14_c2034522.ipynb

A number of questions were not attempted in this submission. The mark is
correct.

#### submissions/Coursework_c21011314_attempt_2020-12-17-22-01-26_C21011314.ipynb

A number of clumsy mistakes in this submission which lead to syntax errors.

The first question did not use the functions defined.

Using `np.cos` on a symbolic variable will not work.

The last question did not output as asked.

The mark is correct.

### A random sample of files

Using:

    import pandas as pd
    df = pd.read_csv("data.csv")
    for _, row in df.sample(n=10, rand m_state=0).iterrows():
        print(row["Submission filepath"])

#### submissions/Coursework_c1923953_attempt_2020-12-17-14-49-49_c1923953.ipynb

The mark is correct.

#### submissions/Coursework_c1934417_attempt_2020-12-17-11-50-43_C1934417.ipynb

The mark is correct.

#### submissions/Coursework_c2035987_attempt_2020-12-17-11-32-34_c2035987.ipynb

The mark is correct.

#### submissions/Coursework_c2038098_attempt_2020-12-17-21-56-20_c2038098.ipynb

Some minor errors. For example not using the recursive function to create the
function leads to a small error.

The mark is correct.

#### submissions/Coursework_c2039154_attempt_2020-12-21-15-10-52_c2039154.ipynb

The mark is correct.

#### submissions/Coursework_c2050594_attempt_2020-12-17-18-10-18_C2050594.ipynb

This submission had an error in the submitted code for q4-a. As a result all of
the marks for this question were essentially lost.

The mark is correct.

#### submissions/Coursework_c2059801_attempt_2020-12-18-15-13-43_c2059801.ipynb

The mark is correct.

#### submissions/Coursework_c2067461_attempt_2020-12-17-17-30-20_C2067461.ipynb

The mark is correct.

#### submissions/Coursework_c21011314_attempt_2020-12-17-22-01-26_C21011314.ipynb

This was considered above as a submission with a mark below 50% (mark is
correct).

#### submissions/Coursework_c21012303_attempt_2020-12-16-16-57-36_c21012303.ipynb

The mark is correct.

### Analysis

Analysis done with:

    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv("data.csv")
    df["Mark"] = df["Score"] * 100 / df["Maximum score"].max()
    print(df["Mark"].describe())

    plt.figure()
    plt.hist(df["Mark"], bins=20, label="frequency")
    median = df["Mark"].median()
    plt.vlines(median, ymin=0, ymax=100, label=f"median={round(median,3)}")
    plt.legend()
    plt.xlabel("mark")
    plt.savefig("main.pdf")
