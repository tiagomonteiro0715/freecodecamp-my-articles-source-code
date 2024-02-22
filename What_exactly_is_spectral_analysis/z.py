import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define a simple discrete-time signal (e.g., exponential decay)
n = np.arange(0, 10)
x = np.exp(-0.2 * n)

# Compute the Z-transform
z, p, _ = signal.tf2zpk([1], [1, -np.exp(-0.2)])
z_transform = np.abs(z)

# Plot the original signal
plt.stem(n, x, basefmt=' ', use_line_collection=True)
plt.title('Original Signal')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.figure()

# Plot the Z-transform
plt.scatter(z_transform.real, z_transform.imag, marker='o', color='r')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(0, color='black', linestyle='--')
plt.title('Z-transform')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.axis('equal')
plt.show()
