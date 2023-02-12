from read_frame import *

from faster_RCNN import *
import os

QP_List = [21, 28, 35, 42]

video_list = ['BasketballPass_416x240_50_ds75', "BlowingBubbles_416x240_50_ds75", "BQSquare_416x240_60_ds75", "RaceHorses_416x240_30_ds75"]

for videoname in video_list:
    frames = YUV_read_frame(f"./data/{videoname}.yuv", (180, 312))
    nums_frame = len(frames)

    num_sequence = int(nums_frame / 32)

    for num in range(num_sequence):
        path1 = f'../map/input/predict/{videoname}/'
        if not os.path.isdir(path1):
            os.mkdir(path1)
        
        path2 = f'../map/input/predict/{videoname}/{videoname}_{num}/'
        if not os.path.isdir(path2):
            os.mkdir(path2)

        for QP in QP_List:
            print(f"{QP} video {num} ......")
            Frames = YUV_read_frame(f'./data/encode_upscale_video/{videoname}_{num}/{videoname}_QP{QP}_upscale.yuv',(240, 416))

            path3 = f'../map/input/predict/{videoname}/{videoname}_{num}/{videoname}_QP{QP}/'
            if not os.path.isdir(path3):
                os.mkdir(path3)
            
            for k, frame in enumerate(Frames):

                labels, loc, scores = RCNN(frame) 
                f =  open(path3+str(k)+'.txt', 'w')
                for i in range(len(labels)):
                    f.writelines(labels[i] + " " + str(scores[i]) + " " + str(int(loc[i][0])) + " " + str(int(loc[i][1])) + " " + str(int(loc[i][2])) + " " + str(int(loc[i][3])) + '\n')
                f.close()
