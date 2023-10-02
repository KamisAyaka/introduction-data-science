import numpy as np
from matplotlib import pyplot as plt
import csv
from datetime import datetime

filename = 'tips.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    total_bills, tips = [], []
    for row in reader:
        try:
            total_bill = float(row[0])
            tip = float(row[1])
        except ValueError:
            print(total_bill)
        else:
            total_bills.append(total_bill)
            tips.append(tip)

s = (20 * np.random.rand(244)) ** 2
# 随机颜色
colors = np.random.randn(244) * 244
plt.scatter(total_bills, tips, s, c=colors, cmap="viridis")
plt.show()
