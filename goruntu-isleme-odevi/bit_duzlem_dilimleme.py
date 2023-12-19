import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'image1.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

height, width = image.shape

bit_planes = np.zeros((height, width, 8), dtype=np.uint8)

for i in range(8):
    bit_planes[:, :, i] = (image >> i) & 1

fig, axes = plt.subplots(1, 8, figsize=(16, 2))
for i in range(8):
    axes[i].imshow(bit_planes[:, :, i], cmap='gray')
    axes[i].axis('off')
    axes[i].set_title('Bit-{}'.format(7 - i))

plt.show()
