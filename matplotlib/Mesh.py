import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: np.sin(x) + np.cos(x+y)

x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
# print(x)
x, y = np.meshgrid(x, y)
# print(x)
z = f(x, y)

plt.figure( "Blue -> Green (BuGn)")
axes = plt.axes(projection="3d")
# axes.plot_surface(x, y, z)                  # Color map bleutée
# axes.plot_surface(x, y, z, cmap="plasma")
# axes.plot_surface(x, y, z, cmap="RdGy")
axes.plot_surface(x, y, z, cmap="BuGn")

plt.figure( "coolwarm")
axes = plt.axes(projection="3d")
axes.plot_surface(x, y, z, cmap="coolwarm")

plt.show()
