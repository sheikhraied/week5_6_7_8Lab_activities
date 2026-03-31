import cv2
image = cv2.imread('image.png')
inverted_image = 255 - image
cv2.imshow('Original Image', image)
cv2.imshow('Inverted Image', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
