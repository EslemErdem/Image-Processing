import cv2
import numpy as np


image = cv2.imread('image.jpg')


if image is None:
    print("Görüntü yüklenemedi. Lütfen dosya yolunu kontrol edin.")
else:

    height, width = image.shape[:2]


    fx = 1.5
    fy = 1.5


    transformation_matrix = np.float32([[fx, 0, 0], [0, fy, 0]])


    stretched_image = cv2.warpAffine(image, transformation_matrix, (int(width * fx), int(height * fy)))


    cv2.imshow('Original Image', image)
    cv2.imshow('Stretched Image', stretched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
