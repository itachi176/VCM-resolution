import os 

# QP_List = [22, 27, 32, 37]
# QP_List = [47, 52 , 50]
QP_List = [21, 28, 35, 42]

videoname = 'BQMall_832x480_60_ds75'
for QP in QP_List:

    #encode video
    command_encode = f'E:/codec/vvc_codec/x265.exe --input E:/codec/data/{videoname}.yuv --fps 60 --input-res 624x360 --input-depth 8 --psnr --qp {QP} --input-csp i420 --output  E:/codec/data/encode_downscale_video/{videoname}_QP{QP}.bin --csv  E:/codec/data/encode_downscale_video/{videoname}_QP{QP}.csv --csv-log-level 4 >>  E:/codec/data/encode_downscale_video/{videoname}_QP{QP}.txt'
    os.system(command_encode)

    #decode video
    command_decode = f'E:/codec/vvc_codec/TAppDecoder.exe -b E:/codec/data/encode_downscale_video/{videoname}_QP{QP}.bin -o E:/codec/data/encode_downscale_video/{videoname}_QP{QP}.yuv'
    os.system(command_decode)