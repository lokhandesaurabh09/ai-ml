import json

data = {"name": "Saurabh", "skills": ["Python", "Git"]}

with open("data/profile.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data/profile.json", "r") as f:
    loaded = json.load(f)

print(loaded)

#-----------------------------------------------------------

import csv
import json

with open("data/students.csv", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["marks"] = int(row["marks"])

with open("data/students.json", "w") as f:
    json.dump(rows, f, indent=4)

print("students.json written with", len(rows), "records")
