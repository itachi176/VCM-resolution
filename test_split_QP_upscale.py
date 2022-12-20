from read_frame import *

from faster_RCNN import *
import os

QP_List = [21, 28, 35, 42]
# video_list = ['BasketballPass_416x240_50_ds75', 'BlowingBubbles_416x240_50_ds75', 'BQSquare_416x240_60_ds75', 'RaceHorses_416x240_30_ds75']
video_list = ['BasketballDrill_832x480_50_ds75_fast_bilinear']

fr = [50]
for videoname in video_list:
    # videoname = 'BQMall_832x480_60_ds75'
    frames = YUV_read_frame(f"./data/{videoname}.yuv", (360, 624))
    nums_frame = len(frames)

    num_sequence = int(nums_frame / 100)

    for num in range(num_sequence):
        path1 = f'../map/input/predict/{videoname}_{num}_upscale/'
        if not os.path.isdir(path1):
            os.mkdir(path1)

        for QP in QP_List:
            print(f"{QP} video {num} ......")
            Frames = YUV_read_frame(f'./data/encode_upscale_video/{videoname}_{num}/{videoname}_QP{QP}_upscale.yuv',(480, 832))

            path2 = f'../map/input/predict/{videoname}_{num}_upscale/{videoname}_QP{QP}/'
            if not os.path.isdir(path2):
                os.mkdir(path2)
            
            for k, frame in enumerate(Frames):

                labels, loc, scores = RCNN(frame) 
                f =  open(path2+str(k)+'.txt', 'w')
                for i in range(len(labels)):
                    f.writelines(labels[i] + " " + str(scores[i]) + " " + str(int(loc[i][0])) + " " + str(int(loc[i][1])) + " " + str(int(loc[i][2])) + " " + str(int(loc[i][3])) + '\n')
                f.close()
    print(f"done video {videoname}!")