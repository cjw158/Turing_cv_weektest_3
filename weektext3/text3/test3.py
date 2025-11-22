import numpy as np

array = np.arange(1, 26).reshape(5, 5)
print(array)
print(array[1, :])
print(array[:, 2])
print(array[3:5, 3:5])

sum = np.sum(array)
print(sum)
for i in range(5):
    per = np.sum(array[i, :])
    print(per)
for i in range(5):
    per = np.sum(array[:, i])
    print(per)

mean = sum / 25
print(mean)
std = np.std(array)
print(std)
turn = array.T
print(turn)