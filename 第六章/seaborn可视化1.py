import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill' , y = 'tip' , data = tips)
plt.show()