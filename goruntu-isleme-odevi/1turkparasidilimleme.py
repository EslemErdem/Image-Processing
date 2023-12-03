import cv2
import matplotlib.pyplot as plt

# Resmi yerel dosyadan al
file_path = 'turk-lirasi.jpg'
image_cv = cv2.imread(file_path)

# Eğer görüntü başarıyla yüklenmediyse hata mesajı ver ve çık
if image_cv is None:
    print(f"Resim yüklenemedi. Lütfen dosya yolunu kontrol edin: {file_path}")
    exit()

# Resmi gri tonlamaya dönüştür
gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

# Eşikleme işlemi uygula (örneğin, 150 eşik değeri kullanılabilir)
_, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

# Sonuçları göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))
plt.title('Orijinal Resim')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Gri Tonlama')

plt.subplot(1, 3, 3)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Eşiklenmiş Resim')

plt.tight_layout()
plt.show()
