from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from detect.bph_burn_detect import bpH_burn_model
from detect.bph_pest_detect import bpH_pest_model
from detect.wheat_pest_detect import wheat_pest_model
from detect.sources import bph_burn_source
from detect.sources import bph_pest_source
from detect.sources import wheat_source
from detect.sources import corn_source
import cv2

class modelSelector:
    def __init__(self):
        self.start(self.choose_model())

    def choose_model(self):
        print("""
            1: BPH Burn Model
            2: BPH Pest Model
            3: Wheat Pest Model
              """)

        model = int(input("Choose model: "))
        return model

    def start(self, arg):
        switch = {
            1: [bpH_burn_model, bph_burn_source],
            2: [bpH_pest_model, bph_pest_source],
            3: [wheat_pest_model, wheat_source]
        }
        
        selected_model =  switch.get(arg, None)

        if selected_model is None:
            raise ValueError("Invalid case")
        
        
        self.run(selected_model[0], selected_model[1])

    def run(self, custom_model, source, show=True):
        result = custom_model.predict(source=source, show=show)
        return result


if __name__=='__main__':
    modelSelector()