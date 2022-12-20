import os
import natsort
path = './data/new/'
list_file = os.listdir(path)
for sequence in list_file:
    if not os.path.isdir('./data/downscale_75_bilinear/'+ sequence):
        os.mkdir('./data/downscale_75_bilinear/'+ sequence)

    list_sub_sequence = os.listdir(path+sequence)
    list_sub_sequence = natsort.natsorted(list_sub_sequence)
    # print(list_sub_sequence)
    tok = sequence.split('_')
    size = tok[1]
    width = size.split('x')[0]
    down_width = int(int(width)*0.75)
    height = size.split('x')[1]
    down_height = int(int(height)*0.75)

    fr = tok[2]
    for sub_sequence in list_sub_sequence:
        name_sub_sequence = sub_sequence.split('.')[0]
        sub_sequence_path = path + sequence + "/" + sub_sequence
        command = f'E:/codec/data/ffmpeg.exe -s:v {size} -sws_flags bilinear -r {fr}  -i {sub_sequence_path} -vf scale={str(down_width)}x{str(down_height)} -c:v rawvideo  ./data/downscale_75_bilinear/{sequence}/{name_sub_sequence}_down75.yuv'
        os.system(command)
    print("ok!")
