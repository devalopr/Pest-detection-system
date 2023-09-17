from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import os
from . util import getdir

current_dir = getdir(__file__)

wheat_pest_model = YOLO(os.path.join(current_dir,"../models/wheat.pt"))  # load a pretrained model (recommended for training)
# wheat_pest_results = wheat_pest_model .predict(source="WHEAT.mp4", show=True)