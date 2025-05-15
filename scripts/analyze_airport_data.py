import pandas as pd

# Load data
df_counter = pd.read_csv("data/counter_usage.csv")
df_flow = pd.read_csv("data/passenger_flow.csv", parse_dates=["datetime"])
df_slots = pd.read_csv("data/slot_adherence.csv", parse_dates=["scheduled_time", "actual_time"])

# -------------------------
# 1. COUNTER USAGE ANALYSIS
# -------------------------
# Clean time_slot if needed
df_counter["occupancy_status"] = df_counter["occupancy_status"].str.strip()

# Calculate occupancy %
counter_summary = (
    df_counter.groupby(["date", "counter_id"])["occupancy_status"]
    .apply(lambda x: (x == "Occupied").mean() * 100)
    .reset_index(name="occupancy_percent")
)

avg_occupancy = counter_summary["occupancy_percent"].mean()
print(f"📊 Average counter occupancy: {avg_occupancy:.2f}%")

# -------------------------
# 2. PASSENGER FLOW ANALYSIS
# -------------------------
# Add time-of-day and capacity check
df_flow["hour"] = df_flow["datetime"].dt.hour
df_flow["is_peak"] = df_flow["hour"].between(7, 19)

# Define arbitrary zone capacities
zone_capacity = {"A": 150, "B": 130, "C": 140}
df_flow["capacity"] = df_flow["zone"].map(zone_capacity)
df_flow["over_capacity"] = df_flow["passenger_count"] > df_flow["capacity"]

overcap_rate = df_flow["over_capacity"].mean() * 100
print(f"🚨 Percent of zone-hour periods over capacity: {overcap_rate:.2f}%")

# -------------------------
# 3. SLOT ADHERENCE ANALYSIS
# -------------------------
df_slots["delay_min"] = (df_slots["actual_time"] - df_slots["scheduled_time"]).dt.total_seconds() / 60
on_time_rate = (df_slots["status"] == "On-Time").mean() * 100
avg_delay = df_slots["delay_min"].mean()

print(f"✈️ On-time flight rate: {on_time_rate:.2f}%")
print(f"⏱️ Average flight delay: {avg_delay:.1f} minutes")

# Optionally export summaries
counter_summary.to_csv("data/summary_counter_usage.csv", index=False)
df_flow.to_csv("data/cleaned_passenger_flow.csv", index=False)
df_slots.to_csv("data/cleaned_slot_adherence.csv", index=False)