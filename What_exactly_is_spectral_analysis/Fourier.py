import numpy as np
import matplotlib.pyplot as plt

# Generate a simple signal
t = np.linspace(0, 1, 1000, endpoint=False)  # 1 second time interval
f1 = 5  # 5 Hz frequency
signal = np.sin(2 * np.pi * f1 * t)

# Apply Fourier Transform
fourier_transform = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

# Plot the original signal
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Plot the Fourier Transform
plt.subplot(122)
plt.plot(frequencies, np.abs(fourier_transform))
plt.title('Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim(-10, 10)  # Limit the x-axis for better visualization
plt.tight_layout()
plt.show()
