import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('stats for csv.csv')

W = data.Player
Y = data.ShotAverage
print(W)
print(Y)

plt.scatter(data.Shots,data.ShotAverage)
plt.show()
