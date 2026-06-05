# Bluestock Fintech — Mutual Fund Analytics Platform
### Capstone Project | 7 Days | Data Engineering + Analytics + Dashboard

---

## Project Overview
A full-stack Mutual Fund Analytics Platform built using publicly available
Indian mutual fund data from AMFI India and mfapi.in.

---

## Tech Stack
| Tool | Purpose |
|---|---|
| Python 3.10+ | Data processing, analytics |
| Pandas / NumPy | ETL, cleaning, metrics |
| Matplotlib / Seaborn | Visualisation |
| SQLite + SQLAlchemy | Database |
| Power BI Desktop | Interactive dashboard |
| Git + GitHub | Version control |
| mfapi.in | Live NAV API |

---

## Datasets Used
| File | Rows | Description |
|---|---|---|
| 01_fund_master.csv | 40 | 40 real AMFI schemes |
| 02_nav_history.csv | 46,000 | Daily NAV 2022-2026 |
| 08_investor_transactions.csv | 32,778 | 5,000 investors |
| 10_benchmark_indices.csv | 8,050 | Nifty50/100/BSE |
| 04_monthly_sip_inflows.csv | 48 | Real AMFI SIP data |
| 03_aum_by_fund_house.csv | 90 | Quarterly AUM |

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run ETL Pipeline
python scripts/data_ingestion.py
python scripts/etl_pipeline.py

### 3. Fetch Live NAV
python scripts/live_nav_fetch.py

### 4. Get Fund Recommendations
python scripts/recommender.py

### 5. Open Dashboard
Open dashboard/bluestock_mf_dashboard.pbix in Power BI Desktop

---

## Key Findings
1. SIP inflows hit all-time high of Rs.31,002 Cr in Dec 2025
2. SBI MF leads with Rs.12.5 Lakh Crore AUM
3. Industry folios doubled from 13.26 Cr to 26.12 Cr (2022-2025)
4. Mid Cap funds delivered highest 3Y alpha vs benchmark
5. T30 cities account for 65% of total transactions
6. 26-35 age group has highest SIP penetration
7. Mirae Asset and Kotak funds top the composite scorecard

---

## Author
Intern - Bluestock Fintech Pvt. Ltd.
Capstone Project | June 2026

---

## Disclaimer
All data sourced from AMFI India, mfapi.in, NSE/BSE public records.
For educational purposes only. Not financial advice.