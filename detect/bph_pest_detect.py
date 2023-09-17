from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import os 
from . util import getdir

current_dir = getdir(__file__)

bpH_pest_model = YOLO(os.path.join(current_dir,"../models/bph_pest.pt"))  # load a pretrained model (recommended for training)
# bpH_pest_model_result  = bpH_pest_model .predict(source="BPH Pest.mp4", show=True)