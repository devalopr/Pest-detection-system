from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO("BPH Burn.pt")  # load a pretrained model (recommended for training)
# Use the model
results = model.predict(source="BPH Burn.mp4", show=True)