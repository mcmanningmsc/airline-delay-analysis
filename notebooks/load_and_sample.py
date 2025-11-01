import duckdb
from pathlib import Path

csv_path = Path("../data/raw/flights.csv")

con = duckdb.connect(database=':memory:')

con.execute(f"""
CREATE TABLE flights AS
SELECT * FROM read_csv_auto('{csv_path}', SAMPLE_SIZE=-1);
""")

# Sample 5 rows
print("Sample rows:")
print(con.execute("""
SELECT YEAR, MONTH, DAY, AIRLINE, ORIGIN_AIRPORT, DESTINATION_AIRPORT,
       DEPARTURE_DELAY, ARRIVAL_DELAY
FROM flights
LIMIT 5
""").fetchdf())

# Top 10 airlines by average arrival delay
print("\nTop 10 airlines by average arrival delay:")
print(con.execute("""
SELECT AIRLINE, ROUND(AVG(ARRIVAL_DELAY),2) AS avg_arr_delay, COUNT(*) AS total_flights
FROM flights
GROUP BY AIRLINE
ORDER BY avg_arr_delay DESC
LIMIT 10;
""").fetchdf())

# Top 10 origin airports by average departure delay
print("\nTop 10 origin airports by average departure delay:")
print(con.execute("""
SELECT ORIGIN_AIRPORT, ROUND(AVG(DEPARTURE_DELAY),2) AS avg_dep_delay, COUNT(*) AS total_flights
FROM flights
GROUP BY ORIGIN_AIRPORT
ORDER BY avg_dep_delay DESC
LIMIT 10;
""").fetchdf())

# Monthly aggregates (for Power BI)
con.execute("""
CREATE TABLE monthly_delays AS
SELECT YEAR, MONTH, AIRLINE,
       ROUND(AVG(DEPARTURE_DELAY),2) AS avg_dep_delay,
       ROUND(AVG(ARRIVAL_DELAY),2) AS avg_arr_delay,
       COUNT(*) AS total_flights
FROM flights
GROUP BY YEAR, MONTH, AIRLINE
ORDER BY YEAR, MONTH, AIRLINE
""")

# Export to CSV for Power BI
con.execute("""
COPY monthly_delays TO '../data/raw/monthly_delays.csv' (HEADER, DELIMITER ',');
""")
print("\nMonthly aggregate CSV created at data/raw/monthly_delays.csv")