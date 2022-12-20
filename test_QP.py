from read_frame import *

from faster_RCNN import *
import os
QP_list = [14, 21, 28, 35, 42, 47]
# QP_list = [47, 50]
# QP_list = [16, 6, 3]


videoname = 'PeopleOnStreet_2560x1600_30_ds25'
for qp in QP_list:

     
    frames = YUV_read_frame(f'./data/encode_upscale_video/{videoname}_QP{qp}_upscale.yuv',(1600, 2560))
   
    
    path = f'../map/input/predict/{videoname}_QP{qp}/'
    if not os.path.isdir(path):
        os.mkdir(path)

    for k, frame in enumerate(frames):

        labels, loc, scores = RCNN(frame) 
        f =  open(path+str(k)+'.txt', 'w')
        for i in range(len(labels)):
            f.writelines(labels[i] + " " + str(scores[i]) + " " + str(int(loc[i][0])) + " " + str(int(loc[i][1])) + " " + str(int(loc[i][2])) + " " + str(int(loc[i][3])) + '\n')
        f.close()


 