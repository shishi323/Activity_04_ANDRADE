import cv2
filePath = 'shishi.jpg'
windowTitle = 'Andrade'
readCvImage = cv2.imread(filePath,1)
cv2.imshow(windowTitle,readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindow()