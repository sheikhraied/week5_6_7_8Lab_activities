import cv2
image = cv2.imread('image.png')
copy = image.copy()
cv2.circle(copy, (100, 100), 50, (0, 0, 255), 2)
cv2.imshow('Circle Image', copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
