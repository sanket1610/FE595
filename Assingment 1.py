import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.plot(x,y)
ax2.plot(x,z)
ax1.set_title("Sine Function")
ax2.set_title("Cosine Function")
plt.show()