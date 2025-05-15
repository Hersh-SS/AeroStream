import pandas as pd
import sqlite3

# Load cleaned data
df_counter = pd.read_csv("data/summary_counter_usage.csv")
df_flow = pd.read_csv("data/cleaned_passenger_flow.csv")
df_slots = pd.read_csv("data/cleaned_slot_adherence.csv")

# Create in-memory SQLite DB
conn = sqlite3.connect(":memory:")
df_counter.to_sql("counter_usage", conn, index=False, if_exists="replace")
df_flow.to_sql("passenger_flow", conn, index=False, if_exists="replace")
df_slots.to_sql("slot_adherence", conn, index=False, if_exists="replace")

# 1. Counters with avg occupancy > 85%
query1 = """
SELECT counter_id, AVG(occupancy_percent) as avg_occupancy
FROM counter_usage
GROUP BY counter_id
HAVING avg_occupancy > 85
"""
print("🔴 High-Occupancy Counters:\n", pd.read_sql(query1, conn))

# 2. Peak passenger hours per zone
query2 = """
SELECT zone, strftime('%H', datetime) as hour, AVG(passenger_count) as avg_count
FROM passenger_flow
GROUP BY zone, hour
ORDER BY avg_count DESC
LIMIT 6
"""
print("\n🔵 Peak Passenger Periods:\n", pd.read_sql(query2, conn))

# 3. Airlines with highest average delay
query3 = """
SELECT airline, AVG(delay_min) as avg_delay
FROM slot_adherence
GROUP BY airline
ORDER BY avg_delay DESC
LIMIT 5
"""
print("\n✈️ Airlines With Most Delay:\n", pd.read_sql(query3, conn))

pd.read_sql(query2, conn).to_csv("data/sql_peak_passenger_times.csv", index=False)

conn.close()