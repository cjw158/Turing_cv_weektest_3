# 题目1：OpenCV 图像读取与显示

## 任务要求

请编写一个Python程序，完成以下基础图像操作：

1. 读取一张图像文件 `image.jpg`
2. 打印输出图像的基本信息：
   - 图像的高度、宽度和通道数
   - 图像的数据类型
3. 将图像转换为灰度图
4. 使用 matplotlib 分别显示原始彩色图像和灰度图像（使用subplot，1行2列排列）
5. 将灰度图像保存为 `gray_image.jpg`

## 准备工作

请准备一张测试图片 `image.jpg`，放在题目文件夹中。

## 要求

- 使用 OpenCV (cv2) 库读取和处理图像
- 使用 Matplotlib 显示图像
- 代码要有清晰的注释

## 提示

- 使用 `cv2.imread()` 读取图像
- 图像的形状可以通过 `.shape` 属性获取
- 使用 `cv2.cvtColor()` 进行颜色空间转换
- OpenCV 读取的图像是 BGR 格式，matplotlib 显示需要转换为 RGB 格式
- 使用 `plt.subplot()` 和 `plt.imshow()` 显示图像
- 使用 `cv2.imwrite()` 保存图像
