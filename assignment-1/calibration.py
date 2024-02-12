import cv2
import numpy as np

image_path = 'assignment-1/images/calib-checkerboard.png' 
img = cv2.imread(image_path)

if img is not None:
    cv2.imshow('calib-checkerboard', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Print error")


points = []

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4: 
            points.append((x, y))
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow('calib-checkerboard', img)

cv2.setMouseCallback('calib-checkerboard', mouse_click)

while len(points) < 4:
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

if len(points) == 4:
    checkerboard_size = (10, 7)


    objp = np.zeros((checkerboard_size[0]*checkerboard_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)

    square_width = np.linalg.norm(np.array(points[0]) - np.array(points[1])) / (checkerboard_size[0] - 1)
    square_height = np.linalg.norm(np.array(points[0]) - np.array(points[2])) / (checkerboard_size[1] - 1)

    chessboard_points = []
    for i in range(checkerboard_size[1]):
        for j in range(checkerboard_size[0]):
            point_x = points[0][0] + j * square_width
            point_y = points[0][1] + i * square_height
            chessboard_points.append((point_x, point_y))

    chessboard_points = np.array(chessboard_points, dtype=np.float32)
else:
    print("Not enough points selected")
