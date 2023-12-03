import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('image.jpg')

# Görüntünün başarıyla yüklenip yüklenmediğini kontrol et
if image is None:
    print("Görüntü yüklenemedi. Lütfen dosya yolunu kontrol edin.")
else:
    # Kontrast artırma faktörü
    contrast_factor = 1.5

    # Piksel değerlerini genişletmek için dönüşüm matrisi oluştur
    contrast_matrix = np.array([[contrast_factor, 0, 0],
                               [0, contrast_factor, 0],
                               [0, 0, contrast_factor]])

    # Kontrast artırma işlemi
    contrasted_image = cv2.transform(image, contrast_matrix)

    # Sonuçları göster
    cv2.imshow('Original Image', image)
    cv2.imshow('Contrasted Image', contrasted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
