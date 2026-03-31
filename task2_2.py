import cv2
image = cv2.imread('image.png')
blue_channel, green_channel, red_channel = cv2.split(image)
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
