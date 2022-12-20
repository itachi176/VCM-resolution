import cv2 
from read_frame import *
import os 
import natsort 

path = './data/downscale_75_bilinear/'
QP_List = [ 21, 28, 35, 42 ]
# video_list = ['BasketballPass_416x240_50_ds75', 'BlowingBubbles_416x240_50_ds75', 'BQSquare_416x240_60_ds75', 'RaceHorses_416x240_30_ds75']
# fr = [50]
# video_list = ['BasketballDrill_832x480_50']

# for videoname in video_list:
list_file = os.listdir(path)
for sequence in list_file:
    if not os.path.isdir('./data/encode_downscale_75_bilinear/'+ sequence):
        os.mkdir('./data/encode_downscale_75_bilinear/'+ sequence)

    list_sub_sequence = os.listdir(path+sequence)
    list_sub_sequence = natsort.natsorted(list_sub_sequence)

    tok = sequence.split('_')
    size = tok[1]
    width = size.split('x')[0]
    down_width = int(int(width)*0.75)
    height = size.split('x')[1]
    down_height = int(int(height)*0.75)

    fr = tok[2]
    for sub_sequence in list_sub_sequence:
        name_sub_sequence = sub_sequence.split('.')[0]
        path1 = f'./data/encode_downscale_75_bilinear/{sequence}/'+name_sub_sequence
        path2 = f'./data/decode_downscale_75_bilinear/{sequence}/'+name_sub_sequence

        if not os.path.isdir(f'./data/encode_downscale_75_bilinear/{sequence}/'):
            os.mkdir(f'./data/encode_downscale_75_bilinear/{sequence}/')

        if not os.path.isdir(f'./data/decode_downscale_75_bilinear/{sequence}/'):
            os.mkdir(f'./data/decode_downscale_75_bilinear/{sequence}/')

        if not os.path.isdir(path1):
            os.mkdir(path1)
        if not os.path.isdir(path2):
            os.mkdir(path2)

        for QP in QP_List:

            # #encode
            # command_encode = f'E:/codec/vvc_codec/x265.exe --input {path}{sequence}/{name_sub_sequence}.yuv --fps {fr}  --input-res {down_width}x{down_height} --input-depth 8 --psnr --qp {QP} --input-csp i420 --output  {path1}/{name_sub_sequence}_{QP}.bin --csv  {path1}/{name_sub_sequence}_{QP}.csv --csv-log-level 4 >>  {path1}/{name_sub_sequence}_{QP}.txt'
            # os.system(command_encode)

            #decode
            print("okkkk", f'{path1}/{name_sub_sequence}_{QP}.bin')
            command_decode = f'E:/codec/vvc_codec/TAppDecoder.exe -b E:/codec/data/encode_downscale_75_bilinear/{sequence}/{name_sub_sequence}/{name_sub_sequence}_{QP}.bin -o E:/codec/data/decode_downscale_75_bilinear/{sequence}/{name_sub_sequence}/{name_sub_sequence}_{QP}.yuv'
            os.system(command_decode)

# for x, videoname in enumerate(video_list):
#     start = 0 
#     frames = YUV_read_frame(f"./data/{videoname}.yuv", (480, 832))
#     nums_frame = len(frames)

#     num_sequence = int(nums_frame / 100)
#     print(num_sequence)

#     for i in range(num_sequence):
#         path = f'./data/new/{videoname}_{i}'
#         if not os.path.isdir(path):
#             os.mkdir(path)

#         for QP in QP_List:
#             #encode video
#             command_encode = f'E:/codec/vvc_codec/x265.exe --input E:/codec/data/{videoname}.yuv --fps {fr[x]} --seek {start}  --frames 100 --input-res 832x480 --input-depth 8 --psnr --qp {QP} --input-csp i420 --output  E:/codec/data/encode_downscale_video/{videoname}_{i}/{videoname}_QP{QP}.bin --csv  E:/codec/data/encode_downscale_video/{videoname}_{i}/{videoname}_QP{QP}.csv --csv-log-level 4 >>  E:/codec/data/encode_downscale_video/{videoname}_{i}/{videoname}_QP{QP}.txt'
#             os.system(command_encode)

#             #decode video
#             command_decode = f'E:/codec/vvc_codec/TAppDecoder.exe -b E:/codec/data/new/{videoname}_{i}/{videoname}_QP{QP}.bin -o E:/codec/data/new/{videoname}_{i}/{videoname}_QP{QP}.yuv'
#             os.system(command_decode)
#         start += 100
#         print(f"done sequence {i}!--------fr {fr[x]}")
#     print(f"done {videoname}!")

