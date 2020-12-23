import abc

class ObjectDetectionABC(abc.ABC):
    @abc.abstractmethod
    def get_detection(self, image_frame):
        """ 
            Return a Pascal VOC format annotation containig 
            the detections made by the model on the image_frame
        """
        pass
