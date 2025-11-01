import duckdb
from pathlib import Path

# --- Paths ---
# CSV input
csv_path = Path(__file__).parent.parent / 'data' / 'raw' / 'flights.csv'

# Output folder
output_dir = Path(__file__).parent.parent / 'data' / 'raw'
output_dir.mkdir(parents=True, exist_ok=True)  # Ensure folder exists

# --- Connect to DuckDB ---
con = duckdb.connect(database=':memory:')  # in-memory DB

# --- Load flights CSV ---
con.execute(f"""
CREATE TABLE flights AS
SELECT * FROM read_csv_auto('{csv_path}', SAMPLE_SIZE=-1)
""")

print("Flights table loaded.")

# --- Top Airlines by delays ---
con.execute("""
CREATE TABLE top_airlines AS
SELECT AIRLINE,
       ROUND(AVG(DEPARTURE_DELAY),2) AS avg_dep_delay,
       ROUND(AVG(ARRIVAL_DELAY),2) AS avg_arr_delay,
       ROUND(AVG(WEATHER_DELAY),2) AS avg_weather_delay,
       ROUND(AVG(AIRLINE_DELAY),2) AS avg_airline_delay,
       ROUND(AVG(LATE_AIRCRAFT_DELAY),2) AS avg_late_aircraft_delay,
       ROUND(AVG(AIR_SYSTEM_DELAY),2) AS avg_air_system_delay,
       COUNT(*) AS total_flights
FROM flights
GROUP BY AIRLINE
ORDER BY avg_arr_delay DESC
""")

con.execute(f"COPY top_airlines TO '{output_dir}/top_airlines.csv' (HEADER, DELIMITER ',')")
print("CSV exported: top_airlines.csv")

# --- Top Origin Airports ---
con.execute("""
CREATE TABLE top_origin_airports AS
SELECT ORIGIN_AIRPORT,
       ROUND(AVG(DEPARTURE_DELAY),2) AS avg_dep_delay,
       COUNT(*) AS total_flights
FROM flights
GROUP BY ORIGIN_AIRPORT
ORDER BY avg_dep_delay DESC
LIMIT 20
""")

con.execute(f"COPY top_origin_airports TO '{output_dir}/top_origin_airports.csv' (HEADER, DELIMITER ',')")
print("CSV exported: top_origin_airports.csv")

# --- Top Destination Airports ---
con.execute("""
CREATE TABLE top_dest_airports AS
SELECT DESTINATION_AIRPORT,
       ROUND(AVG(ARRIVAL_DELAY),2) AS avg_arr_delay,
       COUNT(*) AS total_flights
FROM flights
GROUP BY DESTINATION_AIRPORT
ORDER BY avg_arr_delay DESC
LIMIT 20
""")

con.execute(f"COPY top_dest_airports TO '{output_dir}/top_dest_airports.csv' (HEADER, DELIMITER ',')")
print("CSV exported: top_dest_airports.csv")

# --- Monthly Aggregates ---
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

con.execute(f"COPY monthly_delays TO '{output_dir}/monthly_delays.csv' (HEADER, DELIMITER ',')")
print("CSV exported: monthly_delays.csv")

# --- Delay Causes ---
con.execute("""
CREATE TABLE delay_causes AS
SELECT AIRLINE,
       ROUND(AVG(WEATHER_DELAY),2) AS avg_weather,
       ROUND(AVG(AIRLINE_DELAY),2) AS avg_airline,
       ROUND(AVG(LATE_AIRCRAFT_DELAY),2) AS avg_late_aircraft,
       ROUND(AVG(AIR_SYSTEM_DELAY),2) AS avg_air_system
FROM flights
GROUP BY AIRLINE
ORDER BY avg_airline DESC
""")

con.execute(f"COPY delay_causes TO '{output_dir}/delay_causes.csv' (HEADER, DELIMITER ',')")
print("CSV exported: delay_causes.csv")

print("All tables created and CSVs exported successfully!")