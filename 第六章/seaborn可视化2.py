import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.stripplot(x="day",y="total_bill",data=tips)
plt.show()