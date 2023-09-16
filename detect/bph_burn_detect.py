from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import os
from . util import getdir 

current_dir = getdir(__file__)

bpH_burn_model = YOLO(os.path.join(current_dir,"../models/bph_burn.pt"))  # load a pretrained model (recommended for training)
# bpH_burn_model_result  = bpH_burn_model .predict(source="../videos/BPH_burn.mp4", show=True)