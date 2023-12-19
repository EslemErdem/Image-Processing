import cv2
import numpy as np
import matplotlib.pyplot as plt

def opening_closing_example(image_path, kernel_size_opening, kernel_size_closing):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: Couldn't open or read the image file at '{image_path}'")
        return


    kernel_opening = np.ones((kernel_size_opening, kernel_size_opening), np.uint8)
    img_opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_opening)


    kernel_closing = np.ones((kernel_size_closing, kernel_size_closing), np.uint8)
    img_closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_closing)


    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img_opened, cmap='gray')
    plt.title(f'Opening (Kernel Size: {kernel_size_opening})')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(img_closed, cmap='gray')
    plt.title(f'Closing (Kernel Size: {kernel_size_closing})')
    plt.axis('off')

    plt.show()


opening_closing_example('image.jpg', kernel_size_opening=5, kernel_size_closing=5)
