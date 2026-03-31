import cv2
image = cv2.imread('image.png')
print(f"Type of the image: {type(image)}")
print(f"Shape of the image array: {image.shape}")
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
