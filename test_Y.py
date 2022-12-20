import cv2 
import os 
from natsort import natsorted
from faster_RCNN import *

# from test_QP import QP_list 

QP_list = [14, 21, 28, 35]
# QP_list = [42]

# QP_list = [21]
videoname = 'BlowingBubbles_416x240_50_ds75'

for qp in QP_list:
    path = f'./BGR/{videoname}_QP{qp}'

    path1 = f'../map/input/predict/{videoname}_QP{qp}_gray/'
    if not os.path.isdir(path1):
        os.mkdir(path1)

    frames = os.listdir(path)
    frames = natsorted(frames)

    for k, frame_path in enumerate (frames):
        frame_path = path + '/' + frame_path
        frame = cv2.imread(frame_path)
        labels, loc, scores = RCNN(frame) 
        f =  open(path1+str(k)+'.txt', 'w')
        for i in range(len(labels)):
            f.writelines(labels[i] + " " + str(scores[i]) + " " + str(int(loc[i][0])) + " " + str(int(loc[i][1])) + " " + str(int(loc[i][2])) + " " + str(int(loc[i][3])) + '\n')
        f.close()