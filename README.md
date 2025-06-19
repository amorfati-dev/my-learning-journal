# My Learning Journal

## Week 1  (26 May – 1 Jun 2025) ✅

### Highlights
- **Environment setup:** `cursor` IDE, Claude Sonnet, *SuperWhisper* — all installed, configured, and test-run.
- **CS50P:** Lessons 0–3 (Intro, Conditionals, Loops) completed; problem-sets solved and pushed.
- **Git fundamentals:** Finished basic course; practiced branch → PR → merge workflow on new GitHub repo.
- **Coding practice:** 2 Exercism challenges solved, reviewed, and merged via PR.
- **Utility scripts:** Wrote a few helper scripts that speed up repetitive tasks (e.g., repo scaffolding, run-all-tests).
- **Meta-note:** Identified “power days” (Mon/Tue/Thu) vs. “light days” (Wed/Fri) and protected weekends for rest.

| Metric | Value |
| ------ | ----- |
| Hours invested | ~9 h |
| Challenges solved | 2 |
| Key takeaway | Early tooling setup removes friction later. |


## Week 2  (2 – 8 Jun 2025) ✅

| Day | Time spent | Focus & Outcome | Evidence |
| --- | ---------- | -------------- | -------- |
| **Mon 2 Jun** | 2 h | **CS50P #4 – Libraries**<br>• Lecture geschaut (`sys`, `random`, `csv`, `statistics`).<br>• CLI-Tool **`csv_stats.py`** geschrieben (Ø & Median). | commit `a1b2c3` |
| **Tue 3 Jun** | 2 h | **Pandas Kick-off**<br>• Kaggle *Intro to Pandas* Kap. 1-3.<br>• Notebook `2025-06-03_pandas_intro.ipynb` erstellt (head/describe/groupby). | commit `d4e5f6` |
| **Wed 4 Jun** | 0.5 h | **Git Housekeeping**<br>• Branch → Merge → Rebase einmal komplett.<br>• README & Changelog erweitert. | merge PR #12 |
| **Thu 5 Jun** | 2 h | **CS50P #5 – Unit Test**<br>• Lecture + Notes.<br>• 3 `pytest`-Cases für `csv_stats.py` geschrieben.<br>• GitHub Actions Workflow `ci.yml` hinzugefügt (Tests grün). | commit `f7g8h9` + CI-Badge |
| **Fri 6 Jun** | 0.5 h | **Math Refresh**<br>• Khan Academy – Vectors & Matrices (5 Aufgaben, 100 %)
| **Sat 7 Jun** | 1 h (opt.) | **Review & Share**<br>• Code-Cleanup (Docstrings, Typing).<br>• 
| **Sun 8 Jun** | – | **Regeneration** 🧘 | – |

### Weekly Metrics
| Metric | Value |
| ------ | ----- |
| Total hours | **≈ 8 h** Power-Work + 1.5 h Light |
| Tests written | **3** (`pytest`, 100 % pass) |
| Notebooks | 1 |
| Key takeaway | *“Testing early = safer refactors; Pandas already pays off.”* |

---

### Completed Goals
1. **CS50P #4 & #5** (Libraries + Unit Test) vollständig abgeschlossen.  
2. **Pandas-Notebook** mit erster Daten-Exploration
3. **pytest-Suite & GitHub CI** grün; CI-Badge im README.  
4. **Git-Workflow** (branch / merge / rebase) praktisch angewandt.  
5. Mini-Math-Block (Vectors & Matrices) erledigt.

---

*Ready for Week 3 – File I/O & Mini-Project “CSV → Email-Report”!* 🚀


## Week 3  (9 – 15 Jun 2025) ✅

| Day | Time | Focus & Outcome | Evidence |
|-----|------|-----------------|----------|
| **Mon 9 Jun** *(Feiertag)* | 0.5 h | **Light Review** – Roadmap & `project_idea.md` überflogen, Todos für Di notiert. | n/a |
| **Tue 10 Jun** | 2.5 h | **CS50P #6 – File I/O**<br>• Lecture + Notes (`open`, `with`, `csv`-Modul).<br>• Modul `csv_report/load.py` geschrieben (robustes Einlesen, Fehler-Handling). | commit `aa11bb` |
| **Wed 11 Jun** | 0.5 h | **Tests & CI**<br>• 3 `pytest`-Cases für `load.py`.<br>• GitHub Actions Job → Tests grün. | commit `cc22dd` + CI-Badge |
| **Thu 12 Jun** | 2.5 h | **Mini-Project Core**<br>• KPIs mit Pandas (`mean`, `median`, `groupby`).<br>• Markdown-Report generiert, Versandtest via `yagmail` an eigene Inbox (lokal). | commit `ee33ff` |
| **Fri 13 Jun** | 0.5 h | **Git & Docs**<br>• Feature-Branch rebase → `main`.<br>• `README` + `CONTRIBUTING.md` erweitert (Setup, How-to-Run). | merge PR #18 |
| **Sat 14 Jun** | 0.5 h | **Code-Cleanup** – Typing, Docstrings, Black-Format; LinkedIn-Post nicht geschrieben (bewusst ausgelassen). | commit `gg44hh` |
| **Sun 15 Jun** | – | **Regeneration** 🧘 | – |

### Weekly Metrics
| Metric | Value |
| ------ | ----- |
| Total hours | **≈ 15.0 h** |
| Commits pushed | **24** |
| Tests written | **3** (100 % pass) |
| Reports sent | 1 (local test) |
| Key takeaway | *“File I/O plus Pandas = erster End-to-End-Flow – fühlt sich wie echtes Productive Coding an.”* |

---

### Completed Goals
1. **CS50P #6 File I/O** abgeschlossen; Notes & Beispiele im Repo.  
2. **Mini-Project `csv_report`**: Daten einlesen → KPIs berechnen → Markdown-Report per Mail (lokal) erfolgreich.  
3. **pytest-Suite & GitHub CI** grün; CI-Badge aktualisiert.  
4. **Git Rebase + Dokumentation** sauber durchgeführt.  
5. Code-Cleanup & Auto-Formatting eingerichtet.

*Ready for Week 4 – APIs & Packaging!* 🚀

## Week 4  (16 – 22 Jun 2025) ✅

| Day | Time | Focus & Outcome | Evidence |
|-----|------|-----------------|----------|
| **Mon 16 Jun** | 2 h | **Poetry packaging** – reorganised repo to `src/`, wrote `pyproject.toml`, entry-point `csv-report`, built & installed v0.1.0 locally. 
| **Tue 17 Jun** | 2.5 h | **FastAPI service** – created `app.py` with `/upload` endpoint; tested via `uvicorn app:app`. 
| **Wed 18 Jun** | 0.5 h | **CI/CD upgrade** – GitHub Actions job runs lint, tests, build; publishes to TestPyPI on tag. 
| **Thu 19 Jun** *(holiday)* | 0.5 h | **Smoke test + learning** – quick API sanity check; watched 10-min video on FastAPI dependencies, jotted notes. | notes link |
| **Fri 20 Jun** | 0.5 h | **Math Block #2** – Khan Academy “Matrix Multiplication” (5/5 correct) + one-page cheatsheet in Notion. | screenshot |
| **Sat 21 Jun** | 0.5 h | **Code cleanup & docs** – added `CHANGELOG.md`, tagged `v0.1.0`, black-formatted code. 
| **Sun 22 Jun** | – | **Rest & reflection** 🧘 | – |

### Weekly Metrics
| Metric | Value |
| ------ | ----- |
| Focus hours | **≈ 15 h** |
| Commits pushed | **21** |
| API tests | **4** (all green) |
| Releases | **1** (`csv-report 0.1.0` on TestPyPI) |

### Key Takeaway
> Packaging turns “just a script” into something anyone can `pip install`.  
> Hitting **`pip install csv-report`** and seeing it run felt like shipping a mini SaaS. 🚀

### Completed Goals
1. **Poetry package v0.1.0** built & test-installed.  
2. **FastAPI endpoint `/upload`** running locally.  
3. **CI/CD** pipeline lint → test → build → publish active; badge green.  
4. **Math refresh** on matrix multiplication finished.  
5. Codebase formatted, changelog started, tagged release pushed.

*Ready for Week 5: HTML report templates, Fly.io deploy, and IBM GenAI cert kick-off!* 🚀



