"""Engagement records for the group project.

We read the minutes each group hands in at the contact hour and record, for
every member, whether they engaged that week.  The individual contribution
score $I$ is the fraction of the five meeting weeks at which a student is
recorded as having engaged, scaled to 100.

Run ``python main.py --help`` from this directory for the available commands.
"""

import argparse
import csv
import curses
import locale
import statistics
import subprocess
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
ROSTER_PATH = DATA_DIR / "roster.csv"
ENGAGEMENT_PATH = DATA_DIR / "engagement.csv"

MEETING_WEEKS = (4, 5, 8, 9, 10)

ROSTER_FIELDS = ("student_id", "username", "first_name", "last_name", "group")
ENGAGEMENT_FIELDS = ("week", "group", "student_id", "status", "note")

STATUS_FOR_CODE = {
    "e": "engaged",
    "c": "caught-up",
    "p": "present",
    "a": "absent",
}
CODE_FOR_STATUS = {status: code for code, status in STATUS_FOR_CODE.items()}
NO_MINUTES = "no-minutes"

COUNTING_STATUSES = frozenset({"engaged", "caught-up"})


def tidy_group_name(name):
    """Undo the ``_gc_`` the VLE substitutes for a space in some group names."""
    return name.replace("_gc_", " ").strip()


def read_csv(path, encoding="utf-8"):
    with open(path, newline="", encoding=encoding) as handle:
        return list(csv.DictReader(handle))


def write_csv(path, fieldnames, rows):
    """Write ``rows`` to ``path`` through a temporary file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_name(path.name + ".tmp")
    with open(temporary_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    temporary_path.replace(path)


def load_roster():
    if not ROSTER_PATH.exists():
        sys.exit(
            f"No roster at {ROSTER_PATH}.\n"
            "Import the group export first: python main.py roster <export.csv>"
        )
    return read_csv(ROSTER_PATH)


def load_engagement():
    if not ENGAGEMENT_PATH.exists():
        return []
    return read_csv(ENGAGEMENT_PATH)


def save_engagement(records):
    ordered = sorted(
        records, key=lambda row: (int(row["week"]), row["group"], row["student_id"])
    )
    write_csv(ENGAGEMENT_PATH, ENGAGEMENT_FIELDS, ordered)


def members_by_group(roster):
    """Group the roster by group name, members sorted by last name."""
    groups = {}
    for student in roster:
        groups.setdefault(student["group"], []).append(student)
    for members in groups.values():
        members.sort(key=lambda student: (student["last_name"], student["first_name"]))
    return dict(sorted(groups.items()))


def full_name(student):
    return f"{student['first_name']} {student['last_name']}"


def counted_weeks(records_for_student):
    return sum(1 for row in records_for_student if row["status"] in COUNTING_STATUSES)


def individual_score(records_for_student):
    """Return $I$, the engagement score out of 100."""
    return 100 * counted_weeks(records_for_student) / len(MEETING_WEEKS)


def records_by_student(records):
    by_student = {}
    for row in records:
        by_student.setdefault(row["student_id"], []).append(row)
    return by_student


def recorded_groups(records, week):
    return {row["group"] for row in records if int(row["week"]) == week}


def command_roster(arguments):
    """Import a group membership export from the VLE."""
    source_rows = read_csv(arguments.export, encoding="utf-8-sig")
    required = {"Group Code", "User Name", "Student Id", "First Name", "Last Name"}
    missing = required - set(source_rows[0])
    if missing:
        sys.exit(f"The export is missing the columns: {', '.join(sorted(missing))}")

    roster = [
        {
            "student_id": row["Student Id"].strip(),
            "username": row["User Name"].strip(),
            "first_name": row["First Name"].strip(),
            "last_name": row["Last Name"].strip(),
            "group": tidy_group_name(row["Group Code"]),
        }
        for row in source_rows
    ]
    roster.sort(key=lambda student: (student["group"], student["last_name"]))
    write_csv(ROSTER_PATH, ROSTER_FIELDS, roster)

    groups = members_by_group(roster)
    sizes = sorted({len(members) for members in groups.values()})
    print(f"Wrote {len(roster)} students in {len(groups)} groups to {ROSTER_PATH}.")
    print(f"Group sizes: {', '.join(str(size) for size in sizes)}.")

    existing = load_engagement()
    group_for_student = {student["student_id"]: student["group"] for student in roster}
    moved = [
        row
        for row in existing
        if row["student_id"] in group_for_student
        and row["group"] != group_for_student[row["student_id"]]
    ]
    if moved:
        print(
            f"\nNote: {len(moved)} existing record(s) were made under a different "
            "group. The records are kept against the student, not the group."
        )


PROMPT_HELP = """
  <enter>  every member engaged
  ecpa     one code per member, in the order listed
             e engaged   c caught up afterwards (counts)
             p present but not engaging   a absent
  x        no minutes handed in by this group
  s        skip this group for now
  u        undo the previous group
  q        save and quit
  ?        show this help
"""


def parse_codes(line, member_count):
    """Turn a line of status codes into a list of statuses, or None."""
    codes = line.replace(" ", "")
    if len(codes) != member_count or any(code not in STATUS_FOR_CODE for code in codes):
        return None
    return [STATUS_FOR_CODE[code] for code in codes]


def describe_existing(members, records_for_group):
    status_for_student = {row["student_id"]: row["status"] for row in records_for_group}
    if not status_for_student:
        return None
    if all(status == NO_MINUTES for status in status_for_student.values()):
        return "no minutes"
    codes = [
        CODE_FOR_STATUS.get(status_for_student.get(member["student_id"], ""), "?")
        for member in members
    ]
    return "".join(codes)


def replace_group_records(records, week, group_name, members, statuses, note):
    """Return ``records`` with this group's week replaced by ``statuses``."""
    kept = [
        row
        for row in records
        if not (int(row["week"]) == week and row["group"] == group_name)
    ]
    for member, status in zip(members, statuses, strict=True):
        kept.append(
            {
                "week": str(week),
                "group": group_name,
                "student_id": member["student_id"],
                "status": status,
                "note": note,
            }
        )
    return kept


def statuses_for_line(line, member_count):
    """Turn a typed line into a list of statuses, or None if it is not valid."""
    if line == "":
        return ["engaged"] * member_count
    if line == "x":
        return [NO_MINUTES] * member_count
    return parse_codes(line, member_count)


def record_plain(arguments, week, groups, records):
    """Walk through the groups in order, one prompt per group."""
    if arguments.group:
        matches = [name for name in groups if arguments.group.lower() in name.lower()]
        if len(matches) != 1:
            sys.exit(f"'{arguments.group}' matches {len(matches)} groups: {matches}")
        group_names = matches
    else:
        already = recorded_groups(records, week)
        group_names = [
            name for name in groups if arguments.redo or name not in already
        ]
        if already and not arguments.redo:
            print(f"Resuming: {len(already)} of {len(groups)} groups already recorded.")

    if not group_names:
        print(f"Every group already has a record for week {week}.")
        return

    print(f"\nRecording engagement for week {week}. Type ? for the key.\n")

    position = 0
    while position < len(group_names):
        group_name = group_names[position]
        members = groups[group_name]
        existing = [
            row
            for row in records
            if int(row["week"]) == week and row["group"] == group_name
        ]
        summary = describe_existing(members, existing)

        print(f"[{position + 1}/{len(group_names)}] {group_name}")
        for index, member in enumerate(members, start=1):
            print(f"    {index}. {full_name(member)}")
        if summary:
            print(f"    (currently recorded as: {summary})")

        try:
            line = input("  > ").strip().lower()
        except EOFError:
            print()
            break

        if line == "?":
            print(PROMPT_HELP)
            continue
        if line == "q":
            break
        if line == "s":
            position += 1
            print()
            continue
        if line == "u":
            position = max(0, position - 1)
            print()
            continue

        statuses = statuses_for_line(line, len(members))
        if statuses is None:
            print(
                f"  Expected {len(members)} codes from "
                f"{''.join(STATUS_FOR_CODE)}, or one of x s u q ?.\n"
            )
            continue

        note = ""
        if any(status != "engaged" for status in statuses):
            try:
                note = input("  note (enter to skip): ").strip()
            except EOFError:
                note = ""

        records = replace_group_records(
            records, week, group_name, members, statuses, note
        )
        save_engagement(records)
        position += 1
        print()

    recorded = recorded_groups(load_engagement(), week)
    print(f"Saved. Week {week}: {len(recorded)} of {len(groups)} groups recorded.")
    outstanding = [name for name in groups if name not in recorded]
    if outstanding:
        print(f"Still outstanding: {len(outstanding)} group(s).")
        if len(outstanding) <= 10:
            for name in outstanding:
                print(f"  {name}")


def match_groups(query, groups, outstanding_only, already_recorded):
    """Rank the groups against a typed query.

    A group matches if the query is part of its name or of a member's name.
    Groups whose name starts with the query come first, since that is what
    we are typing when we read the identifier off a sheet of minutes.
    """
    candidates = [
        name
        for name in groups
        if not outstanding_only or name not in already_recorded
    ]
    if not query:
        return candidates

    needle = query.lower()
    starts_with, contains, member_match = [], [], []
    for name in candidates:
        lowered = name.lower()
        if lowered.startswith(needle):
            starts_with.append(name)
        elif needle in lowered:
            contains.append(name)
        elif any(needle in full_name(member).lower() for member in groups[name]):
            member_match.append(name)
    return starts_with + contains + member_match


def safe_addstr(screen, row, column, text, attribute=0):
    """Write ``text`` without running off the edge of a small terminal."""
    height, width = screen.getmaxyx()
    if not 0 <= row < height or column >= width:
        return
    screen.addstr(row, column, text[: width - column - 1], attribute)


def draw_search(screen, state):
    """Draw the group search: a query line above the matching groups."""
    groups = state["groups"]
    recorded = recorded_groups(state["records"], state["week"])
    scope = "outstanding only" if state["outstanding_only"] else "all groups"
    header = (
        f" Week {state['week']}   "
        f"{len(recorded)}/{len(groups)} groups recorded   ({scope})"
    )
    safe_addstr(screen, 0, 0, header.ljust(screen.getmaxyx()[1] - 1), curses.A_REVERSE)
    safe_addstr(screen, 2, 1, f"group: {state['query']}", curses.A_BOLD)
    safe_addstr(screen, 2, 8 + len(state["query"]), "\u2588")

    height = screen.getmaxyx()[0]
    rows_available = max(1, height - 7)
    matches = state["matches"]
    first = max(
        0,
        min(state["selection"] - rows_available + 1, len(matches) - rows_available),
    )
    for offset, name in enumerate(matches[first : first + rows_available]):
        index = first + offset
        members = groups[name]
        existing = [
            row
            for row in state["records"]
            if int(row["week"]) == state["week"] and row["group"] == name
        ]
        summary = describe_existing(members, existing) or ""
        selected = index == state["selection"]
        marker = ">" if selected else " "
        line = f" {marker} {name:<34} {summary}"
        attribute = curses.A_REVERSE if selected else 0
        padded = line.ljust(screen.getmaxyx()[1] - 1)
        safe_addstr(screen, 4 + offset, 0, padded, attribute)

    if not matches:
        safe_addstr(screen, 4, 3, "no group matches that")

    footer = height - 2
    if state["message"]:
        safe_addstr(screen, footer - 1, 1, state["message"], curses.A_BOLD)
    safe_addstr(
        screen,
        footer,
        1,
        "type to search   up/down move   enter open   tab outstanding only   "
        "esc clear, then quit",
    )


def draw_entry(screen, state):
    """Draw one group: its members, the code line, and the note."""
    group_name = state["group_name"]
    members = state["groups"][group_name]
    header = f" Week {state['week']}   {group_name}"
    safe_addstr(screen, 0, 0, header.ljust(screen.getmaxyx()[1] - 1), curses.A_REVERSE)

    statuses = statuses_for_line(state["codes"], len(members))
    for index, member in enumerate(members):
        status = statuses[index] if statuses else None
        shown = CODE_FOR_STATUS.get(status, "x" if status == NO_MINUTES else " ")
        label = f"   {index + 1}. {full_name(member):<30} {shown}"
        if status is not None and status not in COUNTING_STATUSES:
            safe_addstr(screen, 2 + index, 0, label, curses.A_BOLD)
        else:
            safe_addstr(screen, 2 + index, 0, label)

    codes_row = 3 + len(members)
    safe_addstr(screen, codes_row, 1, f"codes: {state['codes']}", curses.A_BOLD)
    if state["mode"] == "codes":
        safe_addstr(screen, codes_row, 8 + len(state["codes"]), "\u2588")
    else:
        safe_addstr(screen, codes_row + 1, 1, f"note:  {state['note']}")
        safe_addstr(screen, codes_row + 1, 8 + len(state["note"]), "\u2588")

    height = screen.getmaxyx()[0]
    if state["message"]:
        safe_addstr(screen, height - 3, 1, state["message"], curses.A_BOLD)
    if state["mode"] == "codes":
        help_text = (
            "enter all engaged   e engaged  c caught up  p present  a absent   "
            "x no minutes   esc back"
        )
    else:
        help_text = "type a note, enter to save, esc to go back to the codes"
    safe_addstr(screen, height - 2, 1, help_text)


def open_group(state, group_name):
    state["group_name"] = group_name
    state["mode"] = "codes"
    members = state["groups"][group_name]
    existing = [
        row
        for row in state["records"]
        if int(row["week"]) == state["week"] and row["group"] == group_name
    ]
    summary = describe_existing(members, existing)
    state["codes"] = "" if summary in (None, "eeee"[: len(members)]) else summary
    if summary == "no minutes":
        state["codes"] = "x"
    state["note"] = next((row["note"] for row in existing if row["note"]), "")
    state["message"] = ""


def commit_entry(state):
    """Save the group currently open and return to the search."""
    group_name = state["group_name"]
    members = state["groups"][group_name]
    statuses = statuses_for_line(state["codes"], len(members))
    state["records"] = replace_group_records(
        state["records"], state["week"], group_name, members, statuses, state["note"]
    )
    save_engagement(state["records"])
    state["mode"] = "search"
    state["query"] = ""
    state["selection"] = 0
    state["message"] = f"recorded {group_name}"


def handle_search_key(state, key):
    """Return False when the key asks to leave the tool."""
    matches = state["matches"]
    if key == 27:
        if state["query"]:
            state["query"] = ""
            state["selection"] = 0
            return True
        return False
    if key in (curses.KEY_BACKSPACE, 127, 8):
        state["query"] = state["query"][:-1]
        state["selection"] = 0
    elif key == curses.KEY_UP:
        state["selection"] = max(0, state["selection"] - 1)
    elif key == curses.KEY_DOWN:
        state["selection"] = min(max(0, len(matches) - 1), state["selection"] + 1)
    elif key == 9:
        state["outstanding_only"] = not state["outstanding_only"]
        state["selection"] = 0
    elif key in (10, 13, curses.KEY_ENTER):
        if matches:
            open_group(state, matches[state["selection"]])
    elif 32 <= key < 127:
        state["query"] += chr(key)
        state["selection"] = 0
    return True


def handle_codes_key(state, key):
    members = state["groups"][state["group_name"]]
    if key == 27:
        state["mode"] = "search"
        state["message"] = ""
        return
    if key in (curses.KEY_BACKSPACE, 127, 8):
        state["codes"] = state["codes"][:-1]
        state["message"] = ""
        return
    if key in (10, 13, curses.KEY_ENTER):
        statuses = statuses_for_line(state["codes"], len(members))
        if statuses is None:
            state["message"] = (
                f"{len(members)} codes needed, one per member, or x for no minutes"
            )
            return
        if all(status == "engaged" for status in statuses):
            commit_entry(state)
        else:
            state["mode"] = "note"
            state["message"] = ""
        return
    character = chr(key).lower() if 32 <= key < 127 else ""
    if character == "x" and not state["codes"]:
        state["codes"] = "x"
    elif (
        character in STATUS_FOR_CODE
        and state["codes"] != "x"
        and len(state["codes"]) < len(members)
    ):
        state["codes"] += character
    state["message"] = ""


def handle_note_key(state, key):
    if key == 27:
        state["mode"] = "codes"
        return
    if key in (curses.KEY_BACKSPACE, 127, 8):
        state["note"] = state["note"][:-1]
        return
    if key in (10, 13, curses.KEY_ENTER):
        commit_entry(state)
        return
    if 32 <= key < 127:
        state["note"] += chr(key)


def run_record_tui(screen, week, groups, records):
    """Search for a group by name, then record its week."""
    curses.set_escdelay(25)
    curses.curs_set(0)
    state = {
        "week": week,
        "groups": groups,
        "records": records,
        "query": "",
        "selection": 0,
        "mode": "search",
        "group_name": None,
        "codes": "",
        "note": "",
        "message": "",
        "outstanding_only": False,
        "matches": list(groups),
    }

    while True:
        if state["mode"] == "search":
            state["matches"] = match_groups(
                state["query"],
                groups,
                state["outstanding_only"],
                recorded_groups(state["records"], week),
            )
            state["selection"] = min(
                state["selection"], max(0, len(state["matches"]) - 1)
            )
        screen.erase()
        if state["mode"] == "search":
            draw_search(screen, state)
        else:
            draw_entry(screen, state)
        screen.refresh()

        try:
            key = screen.getch()
        except KeyboardInterrupt:
            break
        if key == curses.KEY_RESIZE:
            continue

        if state["mode"] == "search":
            if not handle_search_key(state, key):
                break
        elif state["mode"] == "codes":
            handle_codes_key(state, key)
        else:
            handle_note_key(state, key)

    return state["records"]


def command_record(arguments):
    """Record engagement for one meeting week."""
    week = arguments.week
    if week not in MEETING_WEEKS:
        weeks = ", ".join(str(number) for number in MEETING_WEEKS)
        sys.exit(f"Week {week} is not a meeting week. The meeting weeks are {weeks}.")

    roster = load_roster()
    groups = members_by_group(roster)
    records = load_engagement()

    if arguments.plain or arguments.group:
        record_plain(arguments, week, groups, records)
        return

    # ncurses needs the locale for the accents and apostrophes in the group
    # names, otherwise it miscounts columns and leaves stale text on screen.
    locale.setlocale(locale.LC_ALL, "")
    curses.wrapper(run_record_tui, week, groups, records)

    recorded = recorded_groups(load_engagement(), week)
    print(f"Week {week}: {len(recorded)} of {len(groups)} groups recorded.")
    outstanding = [name for name in groups if name not in recorded]
    if outstanding:
        print(f"Still outstanding: {len(outstanding)} group(s).")
        if len(outstanding) <= 10:
            for name in outstanding:
                print(f"  {name}")


def command_report(arguments):
    """Summarise where every student and every group stands."""
    roster = load_roster()
    groups = members_by_group(roster)
    records = load_engagement()
    by_student = records_by_student(records)

    print("Coverage by week")
    for week in MEETING_WEEKS:
        recorded = recorded_groups(records, week)
        missing_minutes = {
            row["group"] for row in records
            if int(row["week"]) == week and row["status"] == NO_MINUTES
        }
        line = f"  Week {week:>2}: {len(recorded):>2}/{len(groups)} groups recorded"
        if missing_minutes:
            line += f", {len(missing_minutes)} handed in no minutes"
        print(line)

    weeks_recorded = {int(row["week"]) for row in records}
    if not weeks_recorded:
        print("\nNo engagement recorded yet.")
        return

    weeks_so_far = len(weeks_recorded)
    if weeks_so_far == len(MEETING_WEEKS):
        scores = [
            individual_score(by_student.get(student["student_id"], []))
            for student in roster
        ]
        print(f"\nIndividual contribution score across {len(roster)} students")
        print(
            f"  mean {statistics.mean(scores):.1f}, "
            f"median {statistics.median(scores):.1f}"
        )
        for score in sorted({round(value) for value in scores}, reverse=True):
            count = sum(1 for value in scores if round(value) == score)
            print(f"  I = {score:>3}: {count:>3} students")
    else:
        print(f"\nEngagement so far, over the {weeks_so_far} week(s) recorded")
        tally = {}
        not_yet = 0
        for student in roster:
            student_records = by_student.get(student["student_id"], [])
            if not student_records:
                not_yet += 1
                continue
            tally[counted_weeks(student_records)] = (
                tally.get(counted_weeks(student_records), 0) + 1
            )
        for engaged in sorted(tally, reverse=True):
            label = f"{engaged} of {weeks_so_far} weeks:"
            print(f"  {label:<16}{tally[engaged]:>3} students")
        if not_yet:
            print(f"  {'no record yet:':<16}{not_yet:>3} students")
        print(f"  I is worked out over all {len(MEETING_WEEKS)} weeks at the end.")

    print("\nStudents to follow up")
    followed_up = 0
    for student in sorted(roster, key=lambda row: (row["group"], row["last_name"])):
        student_records = by_student.get(student["student_id"], [])
        if len(student_records) < len(weeks_recorded):
            continue
        if counted_weeks(student_records) * 2 >= len(student_records):
            continue
        followed_up += 1
        trail = " ".join(
            f"w{row['week']}:{CODE_FOR_STATUS.get(row['status'], 'x')}"
            for row in sorted(student_records, key=lambda row: int(row["week"]))
        )
        print(f"  {full_name(student):<28} {student['group']:<28} {trail}")
    if followed_up == 0:
        print("  None: every student has engaged at over half the recorded weeks.")


def command_group(arguments):
    """Print the full engagement grid for one group."""
    roster = load_roster()
    groups = members_by_group(roster)
    matches = [name for name in groups if arguments.name.lower() in name.lower()]
    if len(matches) != 1:
        sys.exit(f"'{arguments.name}' matches {len(matches)} groups: {matches}")
    group_name = matches[0]
    records = load_engagement()
    by_student = records_by_student(records)

    header = "  ".join(f"{'w' + str(week):<3}" for week in MEETING_WEEKS)
    print(f"\n{group_name}\n")
    print(f"  {'':<28} {header}     I")
    for member in groups[group_name]:
        student_records = by_student.get(member["student_id"], [])
        status_for_week = {int(row["week"]): row["status"] for row in student_records}
        cells = "  ".join(
            f"{CODE_FOR_STATUS.get(status_for_week.get(week, ''), '.'):<3}"
            for week in MEETING_WEEKS
        )
        score = individual_score(student_records)
        print(f"  {full_name(member):<28} {cells} {score:>5.1f}")

    notes = {
        (int(row["week"]), row["note"])
        for row in records
        if row["group"] == group_name and row["note"]
    }
    if notes:
        print("\n  Notes")
        for week, note in sorted(notes):
            print(f"    Week {week}: {note}")


def command_export(arguments):
    """Write one row per student with the engagement score."""
    roster = load_roster()
    by_student = records_by_student(load_engagement())

    quality_for_group = {}
    if arguments.quality:
        for row in read_csv(arguments.quality):
            quality_for_group[row["group"].strip()] = float(row["quality"])

    fieldnames = ["student_id", "username", "first_name", "last_name", "group"]
    fieldnames += [f"week_{week}" for week in MEETING_WEEKS]
    fieldnames += ["weeks_engaged", "individual_score"]
    if quality_for_group:
        fieldnames += ["quality_score", "final_mark"]

    rows = []
    for student in roster:
        student_records = by_student.get(student["student_id"], [])
        status_for_week = {int(row["week"]): row["status"] for row in student_records}
        row = {field: student[field] for field in ROSTER_FIELDS}
        for week in MEETING_WEEKS:
            row[f"week_{week}"] = status_for_week.get(week, "")
        row["weeks_engaged"] = counted_weeks(student_records)
        row["individual_score"] = round(individual_score(student_records), 1)
        if quality_for_group:
            quality = quality_for_group.get(student["group"])
            row["quality_score"] = "" if quality is None else quality
            row["final_mark"] = (
                "" if quality is None
                else round((row["individual_score"] * quality) ** 0.5, 1)
            )
        rows.append(row)

    write_csv(Path(arguments.output), fieldnames, rows)
    print(f"Wrote {len(rows)} rows to {arguments.output}.")
    if arguments.quality and not quality_for_group:
        print("No quality scores were read, so no final marks were written.")


def command_check(arguments):
    """Confirm that no file under data/ is tracked by git."""
    result = subprocess.run(
        ["git", "ls-files", "--", str(DATA_DIR)],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent,
    )
    tracked = [line for line in result.stdout.splitlines() if line]
    if tracked:
        print("These files carry student data and are tracked by git:")
        for path in tracked:
            print(f"  {path}")
        print("\nThe site is deployed from the repository itself, so a tracked")
        print("file is a published file. Remove them with git rm --cached.")
        sys.exit(1)
    print(f"Nothing under {DATA_DIR} is tracked by git.")


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    subparsers = parser.add_subparsers(dest="command", required=True)

    roster_parser = subparsers.add_parser(
        "roster", help="import a group membership export from the VLE"
    )
    roster_parser.add_argument("export", help="the CSV downloaded from the VLE")
    roster_parser.set_defaults(function=command_roster)

    record_parser = subparsers.add_parser(
        "record", help="record engagement for one meeting week"
    )
    record_parser.add_argument("--week", type=int, required=True)
    record_parser.add_argument("--group", help="record a single group only")
    record_parser.add_argument(
        "--redo", action="store_true", help="revisit groups already recorded"
    )
    record_parser.add_argument(
        "--plain",
        action="store_true",
        help="walk the groups in order at a plain prompt, without the search",
    )
    record_parser.set_defaults(function=command_record)

    report_parser = subparsers.add_parser("report", help="summarise where we are")
    report_parser.set_defaults(function=command_report)

    group_parser = subparsers.add_parser("group", help="show one group's record")
    group_parser.add_argument("name")
    group_parser.set_defaults(function=command_group)

    export_parser = subparsers.add_parser("export", help="write the marks out")
    export_parser.add_argument(
        "--output", default=str(DATA_DIR / "engagement-marks.csv")
    )
    export_parser.add_argument(
        "--quality", help="a CSV of group,quality to compute the final mark"
    )
    export_parser.set_defaults(function=command_export)

    check_parser = subparsers.add_parser("check", help="check nothing is tracked")
    check_parser.set_defaults(function=command_check)

    return parser


def main():
    arguments = build_parser().parse_args()
    arguments.function(arguments)


if __name__ == "__main__":
    main()
