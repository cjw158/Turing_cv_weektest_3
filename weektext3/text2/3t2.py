import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(r"C:\Users\1\Downloads\image.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

scaled = cv2.resize(img_rgb, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)# 缩放50%

h, w = img_rgb.shape[:2]# 旋转 45 度
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)

k = np.sqrt(2) / 2#避免被裁剪
new_w = int(h * k + w * k)
new_h = int(h * k + w * k)

M[0, 2] += (new_w - w) / 2# 调整旋转中心
M[1, 2] += (new_h - h) / 2

rotated = cv2.warpAffine(img_rgb, M, (new_w, new_h))

flipped = cv2.flip(img_rgb, 1)# 水平翻转

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(scaled)
plt.title("Scaled 50%")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(rotated)
plt.title("Rotated 45°")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(flipped)
plt.title("Flipped Horizontal")
plt.axis("off")

plt.tight_layout()
plt.show()

rotated_bgr = cv2.cvtColor(rotated, cv2.COLOR_RGB2BGR)#转回 BGR
cv2.imwrite("rotated_image.jpg", rotated_bgr)

print("旋转后的图像已保存为 rotated_image.jpg")
