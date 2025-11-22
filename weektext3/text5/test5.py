import numpy as np
import matplotlib.pyplot as plt
import cv2

img_path = r"image.jpg"
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imwrite('pertreatment.jpg', img_gaussian)

img_canny = cv2.Canny(img_gaussian, 60, 160)

kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
img_closed = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel_close)

kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
img_open = cv2.morphologyEx(img_closed, cv2.MORPH_OPEN, kernel_open)

ret, _ = cv2.findContours(img_open, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

area_array = []
boxes = []

for res in ret:
    area = cv2.contourArea(res)
    x, y, w, h = cv2.boundingRect(res)
    if 800 < area < 60000 and 0.3 < w / h < 3.5:
        area_array.append(area)
        boxes.append((x, y, w, h))

if len(area_array) == 0:
    area_array = np.array([0])
else:
    area_array = np.array(area_array)

mean_area = np.mean(area_array)
std_area = np.std(area_array)
min_area = np.min(area_array)
max_area = np.max(area_array)

for idx, (x, y, w, h) in enumerate(boxes):
    area = area_array[idx]
    if area > mean_area:
        color = (0, 0, 255)
    else:
        color = (0, 255, 0)
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    cv2.putText(img, str(idx+1), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

cv2.imwrite("traffic_detected.jpg", img)

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(cv2.imread("image.jpg"), cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(2,2,2)
plt.imshow(img_canny, cmap='gray')
plt.title("Canny")

plt.subplot(2,2,3)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Detected")

plt.subplot(2,2,4)
plt.hist(area_array, bins=10)
plt.title("Area Distribution")

plt.tight_layout()
plt.savefig("traffic_analysis_report.png")
plt.close()

print(f"Vehicles: {len(area_array)}\n")
print(f"Min area: {min_area}\n")
print(f"Max area: {max_area}\n")
print(f"Mean: {mean_area}\n")
print(f"Std: {std_area}\n")
