import numpy as np
import matplotlib.pyplot as plot

plot.figure(num="Une période de la fonction sinus")

xValues = np.arange(-np.pi, np.pi+0.1, 0.1);
yValues = np.sin(xValues)

plot.plot(xValues, yValues)
plot.grid(True, which="both")
plot.title("Une période de la fonction sinus")
plot.xlabel("x \u2208 [-\u03c0, \u03c0]")
plot.ylabel("y = sin(x)")

plot.show()

