import numpy as np
from matplotlib import pyplot as plt
import csv
from datetime import datetime

filename = 'tips.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    total_bills = []
    for row in reader:
        try:
            total_bill = float(row[0])
        except ValueError:
            print(total_bill)
        else:
           total_bills.append(total_bill)

plt.hist(total_bills)
plt.xlabel("total_bill")
plt.ylabel("number")
plt.show()
