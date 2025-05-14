import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

os.makedirs("data", exist_ok=True)

# --------------------------
# 1. Counter Usage Dataset
# --------------------------
counters = [f"A{i}" for i in range(1, 11)]
airlines = ["Air Canada", "WestJet", "Delta", "United", "American", "Porter"]

counter_logs = []
for day in pd.date_range("2023-07-01", "2023-07-07"):
    for hour in range(5, 23):  # 5 AM to 10 PM
        for counter in counters:
            entry = {
                "counter_id": counter,
                "date": day.date(),
                "time_slot": f"{hour:02d}:00",
                "airline": random.choice(airlines),
                "occupancy_status": random.choices(["Occupied", "Vacant"], weights=[0.75, 0.25])[0]
            }
            counter_logs.append(entry)

df_counter = pd.DataFrame(counter_logs)
df_counter.to_csv("data/counter_usage.csv", index=False)

# --------------------------
# 2. Passenger Flow Dataset
# --------------------------
zones = ["A", "B", "C"]
passenger_flow = []

for day in pd.date_range("2023-07-01", "2023-07-07", freq="H"):
    for zone in zones:
        entry = {
            "datetime": day,
            "zone": zone,
            "passenger_count": np.random.poisson(lam=120 if 7 <= day.hour <= 19 else 40)
        }
        passenger_flow.append(entry)

df_flow = pd.DataFrame(passenger_flow)
df_flow.to_csv("data/passenger_flow.csv", index=False)

# --------------------------
# 3. Slot Adherence Dataset
# --------------------------
slot_data = []
for i in range(1, 201):
    airline = random.choice(airlines)
    sched = datetime(2023, 7, random.randint(1, 7), random.randint(5, 22), 0)
    delay = random.choice([-10, -5, 0, 5, 10, 15, 20])
    actual = sched + timedelta(minutes=delay)
    status = "On-Time" if delay == 0 else ("Early" if delay < 0 else "Late")
    slot_data.append({
        "flight_id": f"{airline[:2].upper()}{1000+i}",
        "airline": airline,
        "scheduled_time": sched,
        "actual_time": actual,
        "status": status
    })

df_slots = pd.DataFrame(slot_data)
df_slots.to_csv("data/slot_adherence.csv", index=False)

print("Mock data generated in /data")