import os
import csv

DATA_DIR = "./data"
NEW_DATA = "./valuable-data.csv"

with open(NEW_DATA, mode='w') as output_file:
    writer = csv.writer(output_file)

    header = ["sales", "date", "region"]
    writer.writerow(header)

    for filename in os.listdir(DATA_DIR):
        with open(f"{DATA_DIR}/{filename}", mode="r") as input_file:
            reader = csv.reader(input_file)

            row_index = 0
            for row in reader:
                if row_index > 0:
                    product = row[0]
                    raw_price = row[1]
                    quantity = row[2]
                    date = row[3]
                    region = row[4]
                    if product == "pink morsel":
                        price = float(raw_price[1:])
                        sales = price * int(quantity)

                        output_row = [sales, date, region]
                        writer.writerow(output_row)
                row_index += 1
print('done')

