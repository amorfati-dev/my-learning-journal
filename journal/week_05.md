🚀 Week 5 Recap – 23.–29. Juni 2025
Branch: main  Commit: journal/2025-06-29-week05

✅ Abgeschlossene Tasks
Tag	Aufgabe	Ergebnis
Mo	HTML-Report-Template (Jinja2 + Bootstrap)	Template rendert lokal mit Dummy-Daten (templates/report.html)
Di	Premailer-Inlining & Test-E-Mails	Render OK in Gmail + Outlook (Screenshots im Ordner docs/screens)
Mi	Code-Health Sprint	ruff + black laufen sauber – CI grün
Do	Dockerfile & Fly.io Deploy	Health-Route erreichbar: https://csv-report.fly.dev/healthz
Fr	Khan Academy Prob-Quiz	100 % Score
Sa	IBM GenAI Engineering – Modul 1 abgeschlossen
So	Familienzeit	✅

📚 Key Learnings dieser Woche
Template Engines: Jinja2 trennt Logik & Layout – macht spätere Anpassungen super einfach.

E-Mail-Rendering ist tückisch (Outlook!) – Inlining via Premailer spart viel Trouble.

Fly.io: Kinderleichter Free-Tier-Deploy, aber Health-Checks unbedingt definieren (Port 8080).

LLM-Grundlagen (IBM GenAI Modul 1)

Unterschied “base LLM” vs. “task-specific LLM”

Prompt-Stack: System → Context → User

Erste Demo mit watsonx Playground – Latency < 2 s bei 8 B-Model ✨

🧠 Reflexion
Time-Budget: 8 h Power + 2 h Light + 0.5 h Weekend → 10.5 h → Plan erfüllt.

Security-Mindset: Schon jetzt gemerkt, dass Docker-Images ohne --no-cache groß werden & unnötige Pakete Angriffsfläche bieten → nächste Woche slim weiter optimieren.

Flow-Moment der Woche: Als das Fly-Deploy nach 1-click wirklich live war 🙌