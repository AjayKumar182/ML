# 1	Visualize the n-dimensional data using 3D surface plots.
import numpy as np
import matplotlib.pyplot as plt

x=np.outer(np.linspace(-1,1,100),np.ones(100))
y=x.T
z=x**2+y**2

fig=plt.figure()
ax=plt.axes(projection="3d")
ax.plot_surface(x,y,z,cmap="viridis")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Surface plot")

plt.show()
