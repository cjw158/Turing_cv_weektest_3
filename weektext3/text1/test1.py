import cv2
import matplotlib.pyplot as plt

img_path = r"image.jpg"

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
w, h, d = img.shape
print(w, h, d)
print(img.dtype)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(gray, cmap='gray')
plt.savefig('subplot.png')
plt.show()

