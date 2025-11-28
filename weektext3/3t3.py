import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
print("该数组:\n",arr)
print("第2行的所有元素:",arr[1])
print("第3列的所有元素:",arr[:, 2])
print("右下角的2x2子数组:",arr[3:, 3:])
print("整个数组的总和:",arr.sum())
print("每一行的和:",arr.sum(axis=1))
print("每一列的和:",arr.sum(axis=0))
avg = arr.sum()/25
print("均值:", avg)
jvalue = np.sqrt(np.sum((arr - avg) ** 2)/25)
print("标准差:",jvalue)
print("转置\n",np.transpose(arr))
