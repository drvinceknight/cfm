# Engagement records for the group project

The individual contribution score \(I\) is derived from the minutes each
group hands in at the contact hour. A student's score is the fraction of
the five meeting weeks (4, 5, 8, 9 and 10) at which the minutes record
them as having engaged, scaled to 100. The assessment page sets out the
rule; this directory holds the machinery for applying it.

Everything the machinery reads and writes lives in `data/`, which is
gitignored. That matters more here than in most repositories: the site is
deployed with `actions/upload-pages-artifact` from the repository root, so
a tracked file is a published file. `python main.py check` confirms that
nothing under `data/` has been tracked by accident.

## Importing the roster

We download the group membership export from the VLE and import it once:

```bash
cd marking
python main.py roster data/<export>_groupmembers.csv
```

This writes `data/roster.csv`, a normalised list of student id, username,
name and group. The VLE substitutes `_gc_` for a space in some group
names, which the import undoes. Re-run the import whenever groups change;
engagement is recorded against the student, not the group, so a student
who moves group keeps their record.

## Recording a week

We record one meeting week at a time:

```bash
python main.py record --week 4
```

The minutes come back in no particular order, so the tool opens on a
search rather than a fixed walk through the groups. We type the first few
letters of the group identifier on the sheet in front of us and the list
narrows as we type:

```
 Week 4   12/52 groups recorded   (all groups)

 group: lovel

 > Ada Lovelace
```

Pressing enter opens that group and lists its members. The query also
matches member names, which is what we want when a sheet is filled in
badly enough that the group identifier is not obvious. Tab hides the
groups already recorded, so what is left on screen is what is left to do.

With a group open we type one code per member, in the order listed:

```
   1. Sophie Cherry                  e
   2. Cai Neilens                    e
   3. Roseanna Trendell              p
   4. Megan Tribe                    a

 codes: eepa
```

Enter on an empty line records every member as engaged, which is the
common case and one keystroke. The codes are `e` engaged, `c` caught up
afterwards, `p` present but not engaging and `a` absent, and `x` on its
own records that the group handed in no minutes at all. We distinguish
`p` from `a` because the assessment rewards meaningful participation
rather than attendance, and `c` from `a` because a member who was unwell
but caught up through the minutes is recorded as engaged. Only `e` and
`c` count towards \(I\).

Anything other than all engaged prompts for a short note, which is what
we have to hand if a mark is later questioned. Escape steps back, and
escape on an empty query leaves the tool.

The file is saved as each group is committed, so the session can be
interrupted and resumed. Opening a group that already has a record
prefills its codes and note, so corrections are made the same way as the
original entry.

For a sequential walk through every group at a plain prompt, without the
search, pass `--plain`. That is also the mode `--group <name>` uses.

## Keeping on top of it

```bash
python main.py report
```

reports how many groups have been recorded for each week, how many handed
in no minutes, the spread of engagement so far, and a list of students
engaged at fewer than half the weeks recorded. That last list is the one
to act on during term, while there is still time for a student to recover
a week.

```bash
python main.py group "Ada Lovelace"
```

prints one group's grid with the notes, which is what we want open during
a contact hour or when a group asks where it stands.

## Exporting

```bash
python main.py export
```

writes `data/engagement-marks.csv`: one row per student with the status
for each week, the number of weeks engaged, and \(I\). Once the group
marks are known, a CSV with `group,quality` columns gives the final mark
as well:

```bash
python main.py export --quality data/quality.csv
```

The final mark is the geometric mean \(\sqrt{I \times Q}\), as described
on the assessment page.
