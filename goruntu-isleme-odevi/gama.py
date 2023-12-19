import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gamma_correction(image, gamma=1.0):

    corrected_image = np.power(image/255.0, gamma)
    corrected_image = (corrected_image * 255).astype(np.uint8)
    return corrected_image

image_path = 'image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


gamma_corrected_image = apply_gamma_correction(image, gamma=0.5)


fig, axes = plt.subplots(1, 2, figsize=(10, 5))


axes[0].imshow(image, cmap='gray')
axes[0].axis('off')
axes[0].set_title('orijinal resim')

axes[1].imshow(gamma_corrected_image, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Gamma uygulanmis resim (gamma=0.5)')


plt.show()
