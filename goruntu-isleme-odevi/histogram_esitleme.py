import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))


axes[0].imshow(image, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Original Image')


axes[1].imshow(equalized_image, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Equalized Image')


plt.show()
