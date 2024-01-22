import cv2
import numpy as np

img_path = r'C:\Users\user\Desktop\Python\Perspective Warp\Plate 1.jpg'
ori_img = cv2.imread(img_path)

src = []


# mouse callback handler
def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        img = ori_img.copy()

        src.append([x, y])

        for xx, yy in src:
            cv2.circle(img, (xx, yy), 5, (0, 255, 0), -1)

        cv2.imshow('Original Image - Car', img)

        # perspective transform
        if len(src) == 4:
            src_np = np.array(src, dtype=np.float32)
            print("original points : \n", src_np)


cv2.namedWindow('Original Image - Car')
cv2.setMouseCallback('Original Image - Car', mouse_handler)

cv2.imshow('Original Image - Car', ori_img)
if cv2.waitKey(0) == 32:
    cv2.destroyAllWindows()
