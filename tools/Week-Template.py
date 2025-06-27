#!/usr/bin/env python3
from datetime import date, timedelta
import sys, pathlib, textwrap

base = pathlib.Path(__file__).parent.parent / "journal"
next_week = int(sys.argv[1])  # e.g. 05
start = date.today()
end   = start + timedelta(days=6)

content = textwrap.dedent(f"""
    ## Week {next_week:02d}  ({start:%-d %b} – {end:%-d %b %Y})

    | Day | Time | Focus & Outcome | Evidence |
    |-----|------|-----------------|----------|
    | **Mon** |  |  |  |
    | **Tue** |  |  |  |
    | **Wed** |  |  |  |
    | **Thu** |  |  |  |
    | **Fri** |  |  |  |
    | **Sat** |  |  |  |
    | **Sun** |  |  |  |

    ### Weekly Metrics
    | Metric | Value |
    | ------ | ----- |
    | Hours  |       |
    | Commits|       |

    ### Key Takeaway
    > …

    ### Completed Goals
    1. …

""").strip()

(base / f"week-{next_week:02d}.md").write_text(content)
print(f"Created journal/week-{next_week:02d}.md")


'''Usage:
bash python tools/new_week.py 05'''
