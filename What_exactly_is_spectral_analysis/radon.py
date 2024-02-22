import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon, iradon

# Generate a sample image
image = np.zeros((100, 100))
image[20:80, 40:60] = 1

# Perform Radon transform
theta = np.linspace(0., 180., max(image.shape), endpoint=False)
sinogram = radon(image, theta=theta)

# Perform inverse Radon transform (backprojection)
reconstructed_image = iradon(sinogram, theta=theta)

# Display the results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

ax1.set_title('Original Image')
ax1.imshow(image, cmap=plt.cm.Greys_r)

ax2.set_title('Sinogram')
ax2.set_xlabel('Projection Angle (degrees)')
ax2.set_ylabel('Projection Position (pixels)')
ax2.imshow(sinogram, cmap=plt.cm.Greys_r, extent=(0, 180, 0, sinogram.shape[0]))

ax3.set_title('Reconstructed Image')
ax3.imshow(reconstructed_image, cmap=plt.cm.Greys_r)

plt.show()
