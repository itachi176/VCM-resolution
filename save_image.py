from read_frame import *
import cv2

frames = YUV_read_frame('./data/BQMall_832x480_60.yuv',(480, 832))
for i, frame in enumerate(frames):
    cv2.imwrite("../mAP/input/images-optional/{}.jpg".format(str(i)), frame)