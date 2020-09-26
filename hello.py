import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 200)
plt.figure()
plt.plot(x, np.cos(x))
plt.show()