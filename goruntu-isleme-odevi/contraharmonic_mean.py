import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image_path, kernel_size, q):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: Couldn't open or read the image file at '{image_path}'")
        return


    noisy_image = np.clip(img + np.random.normal(0, 25, img.shape), 0, 255).astype('uint8')


    plt.imshow(noisy_image, cmap='gray')
    plt.title('Noisy Image')
    plt.axis('off')
    plt.show()


    filtered_image = cv2.filter2D(noisy_image.astype(np.float32), -1, np.ones((kernel_size, kernel_size), np.float32)/(kernel_size**2))
    filtered_image = np.divide(np.sum(np.power(filtered_image, q+1), axis=(0, 1)), np.sum(np.power(filtered_image, q), axis=(0, 1)))
    filtered_image = np.clip(filtered_image, 0, 255).astype('uint8')


    print(filtered_image.shape)
    plt.imshow(filtered_image, cmap='gray')
    plt.title(f'Contraharmonic Mean Filter (q={q})')
    plt.axis('off')
    plt.show()


contraharmonic_mean_filter('image.jpg', kernel_size=3, q=1.5)
