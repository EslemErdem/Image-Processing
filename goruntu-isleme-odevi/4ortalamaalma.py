import cv2
import numpy as np
from matplotlib import pyplot as plt

# Resmi yükle
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Resmi RGB formatına dönüştür

# Ortalama alma filtresi uygulama
filtered_img = cv2.blur(img, (5, 5))  # 5x5 boyutunda bir ortalama alma filtresi

# Sonuçları gösterme
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Orijinal Resim')

plt.subplot(1, 2, 2)
plt.imshow(filtered_img)
plt.title('Ortalama Alma Filtresi')

plt.tight_layout()
plt.show()
