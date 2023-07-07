# Visualize the n-dimensional data using contour plots.

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)

X,Y=np.meshgrid(x,y)

Z=np.cos(2*X)*np.sin(2*Y)

fig=plt.figure()
ax=plt.axes(projection="3d")
# ax.contour(X,Y,Z,cmap="coolwarm")
ax.contour(X,Y,Z,cmap="viridis")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Contor plot")
