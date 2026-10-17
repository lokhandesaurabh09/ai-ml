import csv
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

valid_rows = []

try:
    with open("data/messy.csv", newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            marks = row["marks"]

            if not marks:
                logging.warning(f"Line {line_no}: missing marks for {row['name']}, skipped")
                continue

            try:
                marks = int(marks)
            except ValueError:
                logging.warning(f"Line {line_no}: invalid marks '{marks}' for {row['name']}, skipped")
                continue

            valid_rows.append({"name": row["name"], "marks": marks})

except FileNotFoundError:
    logging.exception("messy.csv not found")
else:
    logging.info(f"{len(valid_rows)} valid rows processed")
    print(f"{len(valid_rows)} valid rows processed")