import csv

with open("data/students.csv", newline = "") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['marks']}")

#--------------------------------------------------

import csv

with open("data/students.csv", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["marks"] = int(row["marks"])

topper = max(rows, key=lambda r: r["marks"])
average = sum(r["marks"] for r in rows) / len(rows)

print(f"Topper: {topper['name']} ({topper['marks']})")
print(f"Average: {average}")

#-------------------------------------------------------

import csv

def get_grade(marks):
    if marks >= 90:
        return "0"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    return "Fail"

with open("data/students.csv", newline="") as f:
    rows = list(csv.DictReader(f))

with open("data/results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames = ["name", "marks", "grade"])
    writer.writeheader()
    for row in rows:
        marks = int(row["marks"])
        writer.writerow({"name": row["name"], "marks": marks, "grade": get_grade(marks)})

print("results.csv written")
