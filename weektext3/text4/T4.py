import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.family']=['STFangsong']
a = np.array(range(1,101))
plt.plot(a,a**2,label="y = x²",color="red",linestyle="-")
plt.plot(a,a**3,label = "y = x³",color="blue",linestyle="--")
plt.plot(a,2**a,label = "y = 2^x",color="green",linestyle=":")
plt.title('数学函数对比', fontsize=15)
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.grid(True, linestyle='-', color='gray', linewidth=0.5)
plt.legend(loc='upper left')
plt.show()