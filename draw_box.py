import cv2
from read_frame import *

video_name = ''
frames = YUV_read_frame(f'./data/PartyScene_832x480_50.yuv', (480, 832))

with open('./mAP_6seq/PartyScene_832x480_50_QP21/0.txt', 'r') as f:
    texts = f.read().splitlines()
print(texts)

for res in texts:
    tok = res.split(' ')
    label = tok[0]
    top_left_x = int(tok[2])
    # print("topleftx:", top_left_x)
    top_left_y = int(tok[3])
    # print("toplefty:", top_left_y)
    bottom_right_x = int(tok[4])
    # print("bottomx:", bottom_right_x)
    bottom_right_y = int(tok[5])
    # print("bottomy:", bottom_right_y)
    if label == "person":
        color = (0,0,255)
    if label == "teddy_bear":
        color = (0,255,0)
    if label == "handbag":
        color = (255,0,0)
    # save_img = cv2.rectangle(frames[0], (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255,0,0))
    save_img = cv2.rectangle(frames[400], (top_left_x, top_left_y), (bottom_right_x,bottom_right_y), color, 2)
    cv2.putText(frames[400], label, (top_left_x, top_left_y+18), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2)

    cv2.imwrite("PartyScene_832x480_50_QP21.png", frames[400])