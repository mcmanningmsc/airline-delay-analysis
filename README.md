# Airline Delay Analysis (In Progress)

## Overview
This project analyzes U.S. commercial flight delays using publicly available datasets from the U.S. Bureau of Transportation Statistics (BTS).
The goal is to identify patterns in delays across months, airlines, airports, and delay causes.
This version of the project uses sample and aggregated datasets created during the early development phase to establish the dashboard structure and analytical framework.

A full-year BTS dataset will be added in the next phase to produce industry-accurate insights.


## Data Source
All data originates from the U.S. Bureau of Transportation Statistics (BTS), specifically the On-Time Performance dataset (OTP). These data include:

- Flight-level information
- Arrival and departure delays
- Cancellation status
- Airline and airport identifiers
- Delay type minutes (aircraft, weather, air system, security, airline)

Sample data used in this phase were derived from:
- flights_sample.csv
- monthly_delays.csv
- top_airlines.csv
- top_origin_airports.csv
- top_dest_airports.csv

These files represent subsets or aggregations of the original BTS dataset and are used here for rapid prototyping and dashboard architecture design.

## Data Preparation
Imported multiple CSV files into Power BI containing:

- Flight-level details (flights_sample.csv)
- Pre-aggregated airline metrics (top_airlines.csv)
- Pre-aggregated airport metrics (top_origin_airports.csv, top_dest_airports.csv)
- Monthly trends (monthly_delays.csv)

Cleaned column names and standardized field types (integer, decimal, categorical).

Created analytical measures to support KPI calculations:
**Example snippet:**
```python
Avg Arrival Delay = AVERAGE(flights_sample[ARRIVAL_DELAY])
Avg Departure Delay = AVERAGE(flights_sample[DEPARTURE_DELAY])
Total Flights = COUNTROWS(flights_sample)

% Flights Delayed =
DIVIDE(
    COUNTROWS(FILTER(flights_sample, flights_sample[ARRIVAL_DELAY] > 15)),
    COUNTROWS(flights_sample)
)

% Flights Cancelled =
DIVIDE(
    COUNTROWS(FILTER(flights_sample, flights_sample[CANCELLED] <> 0)),
    COUNTROWS(flights_sample)
)
```
Developed a unified data model to support:
- Drill-down analysis
- Cross-filtering
- Airline-level and airport-level comparison
- Month-over-month performance analysis

## Exploratory Analysis
Using the prototype dataset, initial analysis focused on:

1. Monthly Delay Trends
- Arrival vs. departure delay patterns across months
- Degree of correlation between departure delay and arrival delay
- Variation between early-year, mid-year, and late-year performance

2. Airline Performance
- Ranking airlines by average delay
- Flight volume comparisons
- Delay-by-cause patterns (airline, weather, air system, late aircraft, security)

3. Airport Insights
- Top origin airports by average departure delay
- Top destination airports by average arrival delay
- Airports with unusually high delays relative to flight volume

4. Delay Type Analysis
- Contribution of each delay type to total delay minutes
- Heavy influence of late aircraft and airline-related delays
- These exploratory findings enabled the design of a structured dashboard for deeper interactive analysis.


## Visualization (Power BI)
(Power BI dashboard coming)

## Key Insights
TBD


## Tools Used
- **Power BI Desktop:** Data cleaning and preprocessing (pandas, matplotlib, re)
  - Data modeling
  - ETL through Power Query
  - DAX calculations
  - Dashboard layout
- **CSV data (BTS-based):** Flight-level and aggregated subsets
- **Python / DuckDB (future steps):** Planned for combining 12 monthly BTS datasets into a single analytical dataset
- **GitHub:** Portfolio hosting  


## Outcome
In Progress 

## Author
**Michael Manning**  
Data Analyst | SQL • Python • Power BI • Data Visualization  

**GitHub:** [https://github.com/mcmanningmsc](https://github.com/mcmanningmsc)  
**LinkedIn:** [https://linkedin.com/in/michael-manning-5a8380385](https://linkedin.com/in/michael-manning-5a8380385)
