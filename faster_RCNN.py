import detectron2
# from detectron2.utils.logger import setup_logger
# setup_logger()

# import some common libraries
import numpy as np
import cv2
import random
#from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog

import matplotlib.pyplot as plt
# import torchvision.transforms as transforms
from PIL import Image
# def cv2_imshow(img):
#     img = img[:,:,[2,1,0]]
#     img = Image.fromarray(img)
#     img.show()
    # '''plt.figure(figsize=(20, 20))
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()
    # #img = transforms.ToPILImage(img)
    # #plt.show(img)
    # '''

names =  ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic_light',
        'fire_hydrant', 'stop_sign', 'parking_meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports_ball', 'kite', 'baseball_bat', 'baseball_glove', 'skateboard', 'surfboard',
        'tennis_racket', 'bottle', 'wine_glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot_dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted_plant', 'bed', 'dining_table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell_phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy_bear',
        'hair_drier', 'toothbrush']  # class names

# im = cv2.imread("./dog.jpg")
cfg = get_cfg()
# add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.6  # set threshold for this model
# Find a model from detectron2's model zoo. You can either use the https://dl.fbaipublicfiles.... url, or use the detectron2:// shorthand
cfg.MODEL.WEIGHTS = "./model/model_final_280758.pkl"
cfg.MODEL.DEVICE = "cuda"
predictor = DefaultPredictor(cfg)

def RCNN(im):
    
    outputs = predictor(im)

    # print(outputs["instances"].pred_boxes)
    boxes = outputs["instances"].pred_boxes
    labels = outputs["instances"].pred_classes
    scores = outputs['instances'].scores.tolist()
    labels = labels.tolist()
    # print(labels)
    labels = [names[labels[i]] for i in range(len(labels))]
    # print(labels)
    # boxes = boxes.tolist()
    loc = []
    for i in boxes:
        loc.append(i.tolist())
        # loc = i.tolist()
    # im = cv2.rectangle(im, (int(loc[1][0]), int(loc[1][1])), (int(loc[1][2]),int(loc[1][3])), (255,0,0), 2)
        # cv2.putText(im, labels[label], (int(loc[0]), int(loc[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return labels,loc, scores, im
# print(RCNN(cv2.imread('dog.jpg')))
# img = cv2.imread('BQMall_832x480_60_QP21.png')
# labels,loc, scores, im = RCNN(img)
# cv2.imshow("a", im)
# cv2.waitKey()

# v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
# v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
# cv2_imshow(v.get_image()[:, :, ::-1])

