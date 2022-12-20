import cv2 
import os 
from read_frame import *

QP_list = [21, 28, 35, 42]
# QP_list = [42]

videoname = 'BQMall_832x480_60_ds75'

for qp in QP_list:
    path = f'./BGR/{videoname}_QP{qp}'

    if not os.path.isdir(path):
        os.mkdir(path)

    frames = YUV_read_frame_gray(f'./data/encode_upscale_video/{videoname}_QP{qp}_upscale.yuv',(480, 832))
    for i, frame in enumerate(frames):
        cv2.imwrite(path+'/'+str(i)+'.jpg', frame)
    print(f"done QP {qp}")
