# Mini‑Projekt: CSV → Analyse → E‑Mail‑Report

## Projektidee in einem Satz

Aus einer hochgeladenen CSV-Datei Kennzahlen berechnen und als übersichtlichen E‑Mail‑Report versenden.

## Beispiel-Input

`transactions.csv`

| Spalte       | Typ        | Beschreibung       |
| ------------ | ---------- | ------------------ |
| date         | YYYY-MM-DD | Kaufdatum          |
| customer\_id | Integer    | ID des Kunden      |
| amount       | Float      | Bestellwert in EUR |
| ...          |            |                    |

## Gewünschte KPIs

* Gesamtumsatz
* Anzahl Bestellungen
* Ø Bestellwert
* Top‑5 Kunden nach Umsatz
* … (erweiterbar)

## Report‑Format

* HTML + Plain-Text Fallback
* Tabellarische KPI-Übersicht
* Automatisch generiertes Balkendiagramm (Matplotlib)

## Versand

* SMTP (z.B. Gmail) oder SendGrid API
* Konfigurierbar über `.env`

## Technologie‑Stack

* Python 3.12
* pandas, matplotlib
* jinja2 für HTML
* yagmail / sendgrid

## Ordnerstruktur (Vorschlag)

```
.
├── data/
│   └── raw/transactions.csv
├── src/
│   ├── etl.py
│   ├── kpi.py
│   ├── report.py
│   └── email.py
└── README.md
```

## Nächste Schritte

1. CSV‑Beispieldatei bereitstellen
2. KPI‑Berechnung prototypisch in Notebook
3. E‑Mail‑Versand testen (Sandbox)
4. CLI‑Interface aufbauen
5. Deployment (Docker) prüfen
