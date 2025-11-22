import cv2
import matplotlib.pyplot as plt

img_path = r"image.jpg"
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
m = cv2.getRotationMatrix2D(center, 45, 1.0)
img_rotation = cv2.warpAffine(img, m, (w, h))
img_flip = cv2.flip(img, 1)
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(img_small)
plt.subplot(2, 2, 3)
plt.imshow(img_rotation)
plt.subplot(2, 2, 4)
plt.imshow(img_flip)
plt.show()
plt.imsave("rotated_image.jpg", img_rotation)