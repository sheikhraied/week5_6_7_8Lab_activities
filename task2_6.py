import cv2
image = cv2.imread('image.png')
print(f"Pixel value at (50, 50): {image[50, 50]}")
image[50, 50] = [255, 255, 255]
cv2.imwrite('modified.png', image)
cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
