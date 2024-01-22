import cv2
import numpy as np
import keyboard
import os

img_path = r'C:\\Users\\user\\Desktop\\Python\\Perspective Warp\\Plate 1.jpg'
ori_img = cv2.imread(img_path)

src = []
src.append([102, 215])
src.append([129, 264])
src.append([108, 292])
src.append([86, 237])

src_np = np.array(src, dtype=np.float32)

width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
height = max(np.linalg.norm(src_np[0] - src_np[3]), np.linalg.norm(src_np[1] - src_np[2]))

width_ratio = (width / height)
height_ratio = 1

dst_np = np.array([[0, 0],
                   [int(height_ratio * 300), 0],
                   [int(width_ratio * 350), int(height_ratio * 350)],
                   [0, int(height_ratio * 350)]
                   ], dtype=np.float32)

M = cv2.getPerspectiveTransform(src_np, dst_np)
result = cv2.warpPerspective(ori_img, M, (400, 300))
print("Perspective Transformation :\n", M)

cv2.imshow('img', ori_img)

print("Press the space bar to get 4 matching points on the license plate.")

if cv2.waitKey(0) == ord(' '):
    for xx, yy in src:
        cv2.circle(ori_img, (xx, yy), 5, (0, 255, 0), -1)
cv2.imshow('img', ori_img)
print("original points : \n", src_np)

if cv2.waitKey(0) == ord(' '):
    cv2.imshow('result', result)
    print("\ndestination points : \n", dst_np)

if cv2.waitKey(0) == ord(' '):
    cv2.destroyAllWindows()

# Image Saving

image_path = r'C:\Users\user\Desktop\Python\Perspective Warp\Plate 1.jpg'

directory = r'C:\Users\user\Desktop\Python\Perspective Warp'


os.chdir(directory)

print("Before saving image:")
print(os.listdir(directory))

filename = 'savedImage.jpg'

cv2.imwrite(filename, result)

print("After saving image:")
print(os.listdir(directory))

print('Successfully saved')
