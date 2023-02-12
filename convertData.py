import os 

names =  ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic_light',
        'fire_hydrant', 'stop_sign', 'parking_meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports_ball', 'kite', 'baseball_bat', 'baseball_glove', 'skateboard', 'surfboard',
        'tennis_racket', 'bottle', 'wine_glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot_dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted_plant', 'bed', 'dining_table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell_phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy_bear',
        'hair_drier', 'toothbrush']

files = os.listdir('./grouth_truth/classD/RaceHorsesD')
len_file = len(files)
num_sequence = int(len_file / 32)
print(num_sequence)
ratio = 1
count = 0 
k = 0
for file in files:
    # print(file[0])
    with open('./grouth_truth/classD/RaceHorsesD/'+ file, 'r') as f:
        texts = f.read().splitlines()
    # print(text[0].split(' ')) # x,y,w,h (x=x*/N, y= y*/M, w=w*/N, h=h*/M) width N and height M 
    # results = text[1].split(' ')
    if k % 32 ==0:
        if count  == num_sequence:
            break
        if not os.path.isdir(f'../mAP/input/ground-truth/{count}'):
            os.mkdir(f'../mAP/input/ground-truth/{count}')
        path = f'../mAP/input/ground-truth/{count}/'
        
        count+=1
        k = 0
        
    f =  open(path+str(k)+'.txt', 'w')
    # print(k)
    for results in texts:
        results = results.split(' ')
        x = results[1]
        y = results[2]
        w = results[3]
        h = results[4]
        
        x = float(x) * 416
        w = float(w) * 416
        y = float(y) * 240
        h = float(h) * 240 
        # print(type(x))
        top_left_x = abs(x - w//2)
        top_left_y = abs(y - h//2)
        bottom_right_x = x + w//2
        bottom_right_y = y + h//2 

        top_left_x = top_left_x * ratio
        top_left_y = top_left_y * ratio
        bottom_right_x = bottom_right_x * ratio
        bottom_right_y = bottom_right_y * ratio

        f.writelines(names[int(results[0])] + " " + str(int(top_left_x)) + " " + str(int(top_left_y)) + " " + str(int(bottom_right_x)) + " " + str(int(bottom_right_y)) + '\n')
    k += 1
    f.close()


    # image = cv2.rectangle(image, (int(top_left_x), int(top_left_y)), (int(bottom_right_x), int(bottom_right_y)), (255,0,0), 2)

