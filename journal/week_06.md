# Week 06 | 30 Jun – 6 Jul 2025

**Branch:** `main`  **Commit:** `journal/2025-07-06-week06`

---

## ✅ Abgeschlossene Tasks

| Tag  | Aufgabe                                                     | Ergebnis                                                      |
|------|-------------------------------------------------------------|---------------------------------------------------------------|
| Mo   | `models.py` + `db_init.py` erstellt                          | `run.db` wird beim ersten Aufruf automatisch angelegt         |
| Di   | CLI erweitert: CSV-Runs in DB schreiben & `show-runs` cmd    | `show-runs` listet ≥ 2 Einträge korrekt auf                  |
| Mi   | CS50P Lecture 7 & pset 7 (“Movies”) abgeschlossen            | Regex-Übungen gelöst, pset 7 eingereicht                      |
| Do   | CI/CD Pipeline: lint → tests → Docker build → Fly deploy tag | GH Action grün → `v0.2.0` live auf Fly.io                     |
| Fr   | Exercism-Python Challenge gelöst                            | Aufgabe in `/exercism/` committet                             |
| Sa   | IBM “Intro to AI” Videos & Quizzes abgeschlossen              | Kursfortschritt ≈ 100 %                                        |
| So   | Familienzeit                                                 | –                                                              |

---

## 📚 Key Learnings

1. **Daten-Persistenz:** Mit SQLModel und SQLite ist das Anlegen einer lokalen DB in wenigen Zeilen erledigt und erlaubt langfristiges Tracking.  
2. **CLI-Design:** Einfache Filter-Flags (`--min-kpi`) und zusätzliche Commands (`show-runs`) machen das Tool flexibler.  
3. **CI/CD-Flow:** GitHub Actions + Fly.io-Deploy per Tag-Trigger automatisieren den Workflow und geben sofortes Feedback.  
4. **Python-Übungen:** Exercism-Challenges stärken Routine und Code-Stilsicherheit.  
5. **AI-Grundlagen:** IBM “Intro to AI” vermittelt greifbare Use Cases, ideal um später tiefer in ML einzusteigen.

---

## 🧠 Reflexion

- **Fokus & Effizienz:** Durch klares Task-Slicing konnte ich in 10,5 h alle geplanten Ziele abarbeiten – trotz Python-“Newbie”-Status fühle ich mich zunehmend sicherer.  
- **Motivation:** Seeing the database persist runs and the live deploy succeed gave a great confidence boost.  
- **Balance:** Exercism als kurzes Daily-Workout hilft, den Kopf frei zu halten und nicht in Tutorial-Hell zu geraten.


---

## ⌨️ Git-Commit-Vorlage

```bash
git add journal/week_06.md
git commit -m "docs: add week06 learning journal (2025-07-06)"
git push origin main
