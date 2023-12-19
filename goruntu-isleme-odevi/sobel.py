import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)


edges = np.sqrt(sobel_x**2 + sobel_y**2)


fig, axes = plt.subplots(1, 4, figsize=(15, 5))


axes[0].imshow(image, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Original Image')

# Sobel x
axes[1].imshow(np.abs(sobel_x), cmap='gray')
axes[1].axis('off')
axes[1].set_title('Sobel X')

# Sobel y
axes[2].imshow(np.abs(sobel_y), cmap='gray')
axes[2].axis('off')
axes[2].set_title('Sobel Y')

# Kenar tespiti sonucu
axes[3].imshow(edges, cmap='gray')
axes[3].axis('off')
axes[3].set_title('kenar tespiti')


plt.show()
