import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

x1 = np.linspace(0, 10, 100)
x2 = np.linspace(0, 10, 100)
x3 = np.linspace(0, 10, 100)
y1 = x1 ** 2
y2 = x2 ** 3
y3 = 2 ** x3
plt.title("数学函数对")
plt.plot(x1, y1, label='y = x²', color='r', ls='-')
plt.plot(x2, y2, label='y = x³', color='b', ls='--')
plt.plot(x3, y3, label='y = 2^x', color='g', ls=':')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig('functions_plot.png')
plt.show()
