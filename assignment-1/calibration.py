import cv2

image_path = 'assignment-1/images/calib-checkerboard.png' 
img = cv2.imread(image_path)

if img is not None:
    cv2.imshow('calib-checkerboard', img)
    cv2.waitKey(0)
else:
    print("Print error")