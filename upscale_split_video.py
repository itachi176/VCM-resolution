import cv2 
from read_frame import *
import os 
import natsort 

# path = './data/encode_downscale_video/'
QP_List = [ 21, 28, 35, 42 ]
video_list = ['BasketballPass_416x240_50_ds75', "BlowingBubbles_416x240_50_ds75", "BQSquare_416x240_60_ds75", "RaceHorses_416x240_30_ds75"]
fr = [50, 50, 60, 30]
# for sequence in list_file:
#     if not os.path.isdir('./data/upscale_75_bilinear/'+ sequence):
#         os.mkdir('./data/upscale_75_bilinear/'+ sequence)

#     list_sub_sequence = os.listdir(path+sequence)
#     list_sub_sequence = natsort.natsorted(list_sub_sequence)

#     tok = sequence.split('_')
#     size = tok[1]
#     width = size.split('x')[0]
#     down_width = int(int(width)*0.75)
#     height = size.split('x')[1]
#     down_height = int(int(height)*0.75)

#     fr = tok[2]

#     for sub_sequence in list_sub_sequence:
#         name_sub_sequence = sub_sequence.split('.')[0]
#         path1 = f'./data/upscale_75_bilinear/{sequence}/'+name_sub_sequence
#         if not os.path.isdir(path1):
#             os.mkdir(path1)
        
#         for QP in QP_List:
#             command_encode = f'E:/codec/data/ffmpeg.exe -s:v {down_width}x{down_height} -sws_flags bilinear -r {fr} -i E:/codec/data/decode_downscale_75_bilinear/{sequence}/{name_sub_sequence}/{name_sub_sequence}_{QP}.yuv -vf scale={width}x{height} -c:v rawvideo  E:/codec/data/upscale_75_bilinear/{sequence}/{name_sub_sequence}/{name_sub_sequence}_{QP}_upscale.yuv'
#             os.system(command_encode)

for x, videoname in enumerate(video_list):
    start = 0 
    frames = YUV_read_frame(f"./data/{videoname}.yuv", (180, 312))
    nums_frame = len(frames)

    num_sequence = int(nums_frame / 32)
    print(num_sequence)

    for i in range(num_sequence):
        path = f'./data/encode_upscale_video/{videoname}_{i}'
        if not os.path.isdir(path):
            os.mkdir(path)

        for QP in QP_List:

            #encode video
            command_encode = f'E:/codec/data/ffmpeg.exe -s:v 312x180  -r {fr[x]} -i E:/codec/data/encode_downscale_video/{videoname}_{i}/{videoname}_QP{QP}.yuv -vf scale=416x240 -c:v rawvideo  E:/codec/data/encode_upscale_video/{videoname}_{i}/{videoname}_QP{QP}_upscale.yuv'
            os.system(command_encode)
