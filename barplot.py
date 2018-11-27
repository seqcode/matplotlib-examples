import numpy as np	
from matplotlib import pyplot as plt

#simulate data
ys = np.random.uniform(0, 10, 5)

#start with a frameless plot (extra room on the left)
plt.subplot2grid((10,10), (0,0), 9, 10, frameon=False)

#label axes
plt.ylabel("magnitude", fontsize=14)

#define offsets
xs = range(len(ys))

xmin = min(xs)
xmax = max(xs)
x_range = xmax - xmin
x_start = xmin - x_range/15.	#bigger offset for bar plot
x_end = xmax + x_range/15.

ymin = 0
ymax = max(ys)
y_range = ymax - ymin
y_start = ymin - y_range/25.
y_end = ymax + y_range/25.

#plot data
plt.bar(xs, ys, width=0.4, bottom=y_start)

#define axes with offsets
plt.axis([x_start, x_end, y_start, y_end], frameon=False)

#plot axes (black with line width of 4)
plt.axvline(x=x_start, color="k", lw=4)
plt.axhline(y=y_start, color="k", lw=4)

#plot ticks
plt.xticks(xs, ("a", "b", "c", "d", "e"))
plt.tick_params(direction="out", top=False, right=False, length=12, width=3, pad=5, labelsize=12)

plt.savefig("bar")
plt.show()	
