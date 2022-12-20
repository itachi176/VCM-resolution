from read_frame import *

from faster_RCNN import *
import os

QP_List = [3, 6, 10, 14, 16, 21, 22, 27, 28, 35, 42, 47]

videoname = 'BQTerrace_1920x1080_60'
frames = YUV_read_frame(f"./data/{videoname}.yuv", (1080, 1920))
nums_frame = len(frames)

num_sequence = int(nums_frame / 100)

for num in range(num_sequence):
    path1 = f'../map/input/predict/{videoname}_{num}/'
    if not os.path.isdir(path1):
        os.mkdir(path1)

    for QP in QP_List:
        print(f"{QP} video {num} ......")
        Frames = YUV_read_frame(f'./data/encode_downscale_video/{videoname}_{num}/{videoname}_QP{QP}.yuv',(1080, 1920))

        path2 = f'../map/input/predict/{videoname}_{num}/{videoname}_QP{QP}/'
        if not os.path.isdir(path2):
            os.mkdir(path2)
        
        for k, frame in enumerate(Frames):

            labels, loc, scores = RCNN(frame) 
            f =  open(path2+str(k)+'.txt', 'w')
            for i in range(len(labels)):
                f.writelines(labels[i] + " " + str(scores[i]) + " " + str(int(loc[i][0])) + " " + str(int(loc[i][1])) + " " + str(int(loc[i][2])) + " " + str(int(loc[i][3])) + '\n')
            f.close()
