import cv2
image = cv2.imread('image.png')
image2 = cv2.imread('image.png')
image2 = cv2.resize(image2, (image.shape[1], image.shape[0]))
blended = cv2.addWeighted(image, 0.6, image2, 0.4, 0)
cv2.imshow('Blended Image', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
