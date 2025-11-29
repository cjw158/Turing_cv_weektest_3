import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y1 = x**2
y2 = x**3
y3 = 2**x

plt.plot(x, y1, 'r-', label="y = x²")# 红色实线
plt.plot(x, y2, 'b--', label="y = x³")# 蓝色虚线
plt.plot(x, y3, 'g:', label="y = 2^x")# 绿色点线

plt.title("数学函数对比")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.savefig("functions_plot.png", dpi=300)
plt.show()
