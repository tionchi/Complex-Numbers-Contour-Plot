import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 400) 
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y
magnitude = np.abs(np.cos(Z))

plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, magnitude, levels=100, cmap='viridis')
plt.colorbar(contour, label='|cos(z)|')
plt.title('Magnitude of cos(z) in the Complex Plane', fontsize=14)
plt.xlabel('Re(z)', fontsize=12)
plt.ylabel('Im(z)', fontsize=12)

plt.axhline(0, color='white', linewidth=0.7, linestyle="--")
plt.axvline(0, color='white', linewidth=0.7, linestyle="--")

plt.show()