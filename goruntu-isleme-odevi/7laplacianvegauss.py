import cv2
import numpy as np
from matplotlib import pyplot as plt

# Resmi oku
img = cv2.imread('image.jpg', 0)
# Laplacian işlemi
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Laplacian sonucunu görselleştir
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Orjinal Resim'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.show()
# Gauss işlemi
gaussian = cv2.GaussianBlur(img, (5, 5), 0)  # Gauss filtresi boyutunu ve standart sapmayı ayarlayabilirsiniz

# Gauss sonucunu görselleştir
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Orjinal Resim'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(gaussian, cmap='gray')
plt.title('Gaussian'), plt.xticks([]), plt.yticks([])

plt.show()
