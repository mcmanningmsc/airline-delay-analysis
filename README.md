# Airline Delay Analysis

## Overview
This project analyzes U.S. commercial flight delays using publicly available datasets from the U.S. Department of Transportation’s On-Time Performance (OTP) data. 
The goal is to identify patterns in delays across months, airlines, airports, and delay causes using an interactive Power BI dashboard.

This version of the project uses the full 2015 flight-level dataset (approximately 5.8 million records) obtained from Kaggle, which mirrors the original DOT/BTS On-Time Performance data. The final dashboard includes trend analysis, airline and airport comparisons, and a drill-down page with dynamic filters.

## Data Source
All data used in this project was obtained from Kaggle’s publicly available “US Flight Delays (2015)” dataset. This dataset contains real U.S. domestic flight records for 2015 and originates from the U.S. Department of Transportation’s On-Time Performance (OTP) data.

The dataset includes:
- Flight-level details
- Arrival and departure delays
- Cancellation status
- Airline and airport identifiers
- Delay cause minutes:
  - AIRLINE_DELAY
  - WEATHER_DELAY
  - AIR_SYSTEM_DELAY
  - LATE_AIRCRAFT_DELAY
  - SECURITY_DELAY
 
This Kaggle dataset consolidates the full 2015 flight year into a single CSV file and is suitable for large-scale delay analysis.

## Data Preparation
The full 2015 Kaggle dataset was imported into Power BI and prepared using Power Query. Steps included:

- Cleaning and standardizing column names
- Removing unused fields
- Creating custom DAX measures for KPIs

Example snippet:
```DAX
Avg Arrival Delay = AVERAGE(flights_2015[ARRIVAL_DELAY])
Avg Departure Delay = AVERAGE(flights_2015[DEPARTURE_DELAY])
Total Flights = COUNTROWS(flights_2015)

% Flights Delayed =
DIVIDE(
    COUNTROWS(FILTER(flights_2015, flights_2015[ARRIVAL_DELAY] > 15)),
    COUNTROWS(flights_2015)
)

% Flights Cancelled =
DIVIDE(
    COUNTROWS(FILTER(flights_2015, flights_2015[CANCELLED] = 1)),
    COUNTROWS(flights_2015)
)
``` 
Additional measures were created to analyze total delay minutes by cause.
A unified data model supports drill-down analysis, cross-filtering, airline/airport comparisons, and month-over-month trends.

## Exploratory Analysis

Initial analysis focused on:

### Monthly Delay Trends
- Arrival vs. departure delay patterns
- Seasonal variation
- Correlation between departure and arrival delays

### Airline Performance
- Average delays by carrier
- Flight volume differences
- Delay type contributions

### Airport Insights
- Average delays at major origin and destination airports
- Filtering out small airports with fewer than 5,000 flights

### Delay Type Analysis
- Total delay minutes by cause
- Late aircraft and airline-related delays as the largest contributors

## Visualization (Power BI)

Overview:
<img width="1273" height="715" alt="overview " src="https://github.com/user-attachments/assets/f5dfe7d0-6a6a-4481-8123-3d152d05836b" />

Airlines & Airports:
<img width="1274" height="716" alt="Airlines   Airport Insights" src="https://github.com/user-attachments/assets/d720fb6f-4067-4016-94dc-f249ec3de136" />

Drilldown Explorer:
<img width="1275" height="714" alt="Interactive Delay Explorer" src="https://github.com/user-attachments/assets/56d30e87-1042-4480-b54a-c55679c6ef79" />


## Key Insights
- 18% of flights in 2015 arrived more than 15 minutes late
- 2% of flights were cancelled
- Late Aircraft Delay was the largest delay contributor
- Delta (DL) and Alaska (AS) showed the strongest on-time performance
- Major hubs such as ORD, EWR, and SFO had higher average delays
- Delays follow clear seasonal patterns, with spikes in winter

## Tools Used
- Power BI Desktop
  - Data modeling
  - DAX calculations
  - Power Query transformations
- CSV Data (Kaggle)
  - Full 2015 dataset
- GitHub
  - Repository hosting and documentation

## Outcome
A complete, interactive Power BI dashboard built from a real 5.8M-row dataset.
Demonstrates ETL, DAX, data modeling, dashboard design, and analytic storytelling.


## Author
**Michael Manning**  
Data Analyst | SQL • Python • Power BI • Data Visualization  

**GitHub:** [https://github.com/mcmanningmsc](https://github.com/mcmanningmsc)  
**LinkedIn:** [https://linkedin.com/in/michael-manning-5a8380385](https://linkedin.com/in/michael-manning-5a8380385)
