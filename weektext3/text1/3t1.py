import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\1\Downloads\image.jpg")
h, w, c = img.shape
print("图像高度（height）：", h)
print("图像宽度（width）：", w)
print("通道数（channels）：", c)
print("图像数据类型（dtype）：", img.dtype)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1)
plt.title("original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

# subplot 2: 灰度图
plt.subplot(1, 2, 2)
plt.title("gray")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.show()

# 5. 保存灰度图
cv2.imwrite("gray_image.jpg", gray)

