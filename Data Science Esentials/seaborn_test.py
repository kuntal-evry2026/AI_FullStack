import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

data = np.random.rand(5,5)
sb.heatmap(data, annot=True, cmap="coolwarm")
plt.title ("HeatMAP")
plt.show()