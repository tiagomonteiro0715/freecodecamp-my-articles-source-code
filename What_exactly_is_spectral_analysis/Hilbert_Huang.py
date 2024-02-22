import numpy as np
import matplotlib.pyplot as plt
from PyEMD import EMD

# Generate sample data
t = np.linspace(0, 1, 1000)
s = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)

# Perform Empirical Mode Decomposition (EMD)
emd = EMD()
imfs = emd(s, t)

# Plot the original signal and its IMFs
plt.figure(figsize=(10, 6))
plt.subplot(211)
plt.plot(t, s, label='Original signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(212)
for i, imf in enumerate(imfs):
    plt.plot(t, imf, label=f'IMF {i+1}')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()
