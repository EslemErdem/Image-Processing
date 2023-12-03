import cv2
import numpy as np
from matplotlib import pyplot as plt

# Resmi yükle
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Resmi RGB formatına dönüştür

# Max filter uygulama
max_filtered = cv2.blur(img, (5, 5))  # 5x5 boyutunda bir max filter

# Box filter uygulama
box_filtered = cv2.boxFilter(img, -1, (5, 5))  # 5x5 boyutunda bir box filter

# Sonuçları gösterme
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Orijinal Resim')

plt.subplot(1, 3, 2)
plt.imshow(max_filtered)
plt.title('Max Filter')

plt.subplot(1, 3, 3)
plt.imshow(box_filtered)
plt.title('Box Filter')

plt.tight_layout()
plt.show()
