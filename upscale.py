import os 

QP_List = [ 21, 28, 35, 42]
# QP_List = [14]

videoname = 'BQMall_832x480_60_ds75'
for QP in QP_List:

    #encode video
    command_encode = f'E:/codec/data/ffmpeg.exe -s:v 624x360 -r 60 -i E:/codec/data/encode_downscale_video/{videoname}_QP{QP}.yuv -vf scale=832x480 -c:v rawvideo  E:/codec/data/encode_upscale_video/{videoname}_QP{QP}_upscale.yuv'
    os.system(command_encode)
