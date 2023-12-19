import cv2
import numpy as np
import matplotlib.pyplot as plt


def segment_image(image_path, lower_bound, upper_bound):

    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: resim acilmiyior '{image_path}'")
        return


    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    mask = cv2.inRange(img_rgb, np.array(lower_bound), np.array(upper_bound))


    segmented_image = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)


    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Segmentation Mask')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(segmented_image)
    plt.title('Segmented Image')
    plt.axis('off')

    plt.show()



segment_image('image.jpg', [0, 0, 0], [100, 100, 100])
