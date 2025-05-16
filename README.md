# AeroStream

Simulated Airport Operations Monitoring & Process Improvement Platform

AeroStream is a simulated analytics project that reflects the core responsibilities of an airport operations analyst or coordinator. Built for a fictional terminal, it integrates data cleaning, dashboarding, process redesign, and stakeholder communication to identify inefficiencies in check-in counter usage, passenger flow, and slot adherence — and proposes actionable improvements.

---

## Project Objectives

- Analyze and visualize check-in counter usage
- Identify peak congestion in terminal zones
- Monitor flight slot adherence (scheduled vs actual)
- Model process inefficiencies in current workflows
- Recommend improvements using real-time analytics

---

## Tech Stack

| Component        | Toolset Used                                    |
|------------------|-------------------------------------------------|
| Data Cleaning    | Python (Pandas, NumPy)                          |
| Dashboarding     | Power BI                                        |
| SQL Queries      | SQLite (via Pandas integration)                 |
| Process Mapping  | diagrams.net (draw.io)                          |
| Documentation    | Microsoft Word & PowerPoint                     |
| Version Control  | Git + GitHub                                    |

---

## Key Features

### Mock Data Generation
Simulated datasets for:
- Airline counter usage (`counter_usage.csv`)
- Passenger counts by zone (`passenger_flow.csv`)
- Flight slot adherence (`slot_adherence.csv`)

### Data Cleaning & KPI Analysis
- Calculated average occupancy per counter
- Flagged overcapacity zones based on thresholds
- Measured on-time performance and average delays

### Dashboard Visuals (Power BI)
- Heatmap: Counter occupancy by day
- Line Chart: Passenger flow over time per zone
- Donut Chart: Flight status (On-Time, Early, Late)
- Bar Chart: Avg delay by airline
- KPI Cards: On-Time % and OverCapacity %

### SQL Integration
Using SQLite and Pandas:
- Counters with >85% occupancy
- Peak congestion hours per zone
- Airlines with highest average delays

### Process Mapping
- As-Is: Manual counter assignment with no real-time visibility
- To-Be: Automated, dashboard-guided allocation with live monitoring

---

## Project Output

- `scripts/generate_mock_data.py` – Generate simulated CSVs
- `scripts/analyze_airport_data.py` – Clean and analyze KPIs
- `scripts/sql_queries.py` – Run operations-focused SQL queries
- Power BI Dashboard – Visual exploration of key metrics
- Process Maps – PDF diagrams showing workflow improvement
- Word Report – Full stakeholder summary
- PowerPoint – Executive summary presentation

---

## File Structure
AeroStream/
├── data/ # Generated CSVs
├── scripts/ # Python scripts
├── dashboards/ # Power BI .pbix file
├── diagrams/ # As-Is and To-Be process maps (PDF)
├── reports/ # Stakeholder report (Word)
├── presentations/ # Final presentation (PPTX)
└── README.md # You're here

---

## Insights & Recommendations

- Redistribute load from overused counters (A3, A10, A7 all >77% occupancy)
- Improve flight scheduling to address low 15.5% on-time rate
- Use dashboards to enable proactive reallocation based on real-time data
- Replace spreadsheet tracking with centralized, live dashboards

---

## Outcome

AeroStream showcases a full pipeline of data-driven operations analysis — from ingestion to stakeholder communication — and models the transformation of reactive airport workflows into optimized, insight-led processes.

---