import cv2
image = cv2.imread('image.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(hsv)
cv2.imshow('Hue', hue)
cv2.imshow('Saturation', saturation)
cv2.imshow('Value', value)
cv2.waitKey(0)
cv2.destroyAllWindows()
