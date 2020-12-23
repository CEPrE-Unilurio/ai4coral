import numpy as np
import tensorflow as tf
import pathlib
import cv2
import time

from object_detection_abc import  ObjectDetectionABC 
from config import *

class TFLiteSingleton:
    
    __instance = None
    __interpreter = None 

    def __init__(self):
        if TFLiteSingleton.__instance != None:
            raise NotImplemented("This is a singleton class.")
    
    @staticmethod
    def get_instance():
        if TFLiteSingleton.__instance == None:
            interpreter = tf.lite.Interpreter(model_path="model.tflite")
            interpreter.resize_tensor_input(input_index=0, tensor_size=[1, H, W, C])
            TFLiteSingleton.__instance = TFLiteSingleton()
            TFLiteSingleton.interpreter = interpreter
        return TFLiteSingleton.__instance
    
    @property
    def interpreter(self):
        return self.__interpreter

    @interpreter.setter
    def interpreter(self, value):
        self.__interpreter = value

    def info(self):
        tfls = self.get_instance()
        interpreter = tfls.interpreter
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        print("--------------------------------------------- inputs details -----------------------------")
        print(input_details)
        print("--------------------------------------------- output details -----------------------------")
        print(output_details)

class ObjectDetection(ObjectDetectionABC):
    
    def __init__(self):
        pass


if __name__ == '__main__': 
    
    start = time.time()
    print("First call to TFLiteSingleton")
    tfls = TFLiteSingleton.get_instance()
    end = time.time()
    print("Elapsed time {} secs".format(end - start))

    start = time.time()
    print("Second call to TFLiteSingleton")
    tfls = TFLiteSingleton.get_instance()
    end = time.time()
    print("Elapsed time {} secs".format(end - start))
    
    print(" ------------------------------------ info ---------------------------------")
    tfls.info()

    od = ObjectDetection()

