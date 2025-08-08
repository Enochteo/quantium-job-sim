import os
import csv
from datetime import datetime

DATA_DIR = "./data"
NEW_DATA = "./valuable-data.csv"

rows = []
for filename in os.listdir(DATA_DIR):
    with open(f"{DATA_DIR}/{filename}", mode="r") as input_file:
        reader = csv.reader(input_file)

        next(reader)
        for row in reader:
            product = row[0]
            raw_price = row[1]
            quantity = row[2]
            date = row[3]
            region = row[4]
            if product == "pink morsel":
                price = float(raw_price[1:])
                sales = price * int(quantity)
                rows.append([sales, date, region])
rows.sort(key=lambda x: datetime.strptime(x[1], "%Y-%m-%d"))

with open(NEW_DATA, mode='w') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["sales", "date", "region"])
    for row in rows:
        writer.writerow(row)

print('done')