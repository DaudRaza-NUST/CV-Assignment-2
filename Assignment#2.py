import math
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

og_img = cv.imread("image4.jpg")
img = og_img.copy()
# rotated_img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 1)
edges = cv.Canny(blur,50,150)
lines = cv.HoughLines(edges, 1, np.pi/120, 115, min_theta=np.pi/36, max_theta=np.pi-np.pi/36)
for line in lines:
    rho,theta = line[0]
    # skip near-vertical lines
    if abs(theta-np.pi/90) < np.pi/9:
        continue
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 10000*(-b))
    y1 = int(y0 + 10000*(a))
    x2 = int(x0 - 10000*(-b))
    y2 = int(y0 - 10000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),1)


plt.subplot(221),plt.imshow(og_img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges)
plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img,cmap = 'gray')
plt.title('Line Detection'), plt.xticks([]), plt.yticks([])
# plt.subplot(224),plt.imshow(fil_img)
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()