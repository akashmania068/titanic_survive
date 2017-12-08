import pandas as pd

dataset = pd.read_csv(filepath_or_buffer="Dataset/train.csv", sep=',', header=0, usecols=[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11])

x = dataset.iloc[:, 2:12].values
y = dataset.iloc[:, 1].values

print(y)
