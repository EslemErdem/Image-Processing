import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(image, cv2.CV_64F)


fig, axes = plt.subplots(1, 2, figsize=(10, 5))


axes[0].imshow(image, cmap='gray')
axes[0].axis('off')
axes[0].set_title('orijinal resim')


axes[1].imshow(laplacian, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Laplace sonucu (Blurring-Like efekti)')


plt.show()
