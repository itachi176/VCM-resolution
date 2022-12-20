import cv2 
import os 
from read_frame import *
import replicate
import natsort
import requests
os.environ['REPLICATE_API_TOKEN'] = '6b700902dae1c7904ca18079d348e86a76070c02'
model = replicate.models.get("pvitoria/chromagan")

video_name = 'BQMall_832x480_60_ds75'
QP_list = [21, 28, 35, 42]
for QP in QP_list:


    path = f'./BGR/{video_name}_QP{QP}'
    save_path = f'./inpainting/{video_name}_QP{QP}/'
    frame_files = os.listdir(path)

    frame_files = natsort.natsorted(frame_files)
    for k,frame in enumerate(frame_files):
        output = model.predict(image=open(f"{path}/{frame}", "rb"))
        img_data = requests.get(output).content
        with open(f'{save_path}/{k}.png', 'wb') as handler:
            handler.write(img_data)
        print(f'done frame {k}!')