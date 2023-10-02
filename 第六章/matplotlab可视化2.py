import numpy as np
from matplotlib import pyplot as plt
import csv
from datetime import datetime

filename = 'tips.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    x = [0, 0, 0, 0, 0]
    for row in reader:
        try:
            total_bill = float(row[0])
        except ValueError:
            print(total_bill)
        else:
            if total_bill <= 10:
                x[0] = x[0] + 1
            elif total_bill <= 20:
                x[1] = x[1] + 1
            elif total_bill <= 30:
                x[2] = x[2] + 1
            elif total_bill <= 40:
                x[3] = x[3] + 1
            else:
                x[4] = x[4] + 1

labels = ["0-10", '10-20', '20-30', '30-40', '40-50']
plt.pie(x, labels=labels, autopct='%.2f%%')
plt.show()
