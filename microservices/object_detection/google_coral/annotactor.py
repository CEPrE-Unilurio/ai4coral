from config import *
import detector_base
from xml.etree import ElementTree as et
from xml.dom import minidom
import detect
import time

class Annotactor:
    
    def __init__(self):
        self.annotation = et.Element('annotation')
    
    def annotate(self, objs=None):
        LABELS = detector_base.load_labels(PATH_TO_LABELS)
        for obj in objs:
            bbox = obj.bbox
            
            object = et.SubElement(self.annotation, 'object')
            
            name = et.SubElement(object, "name")
            name.text = LABELS.get(obj.id, obj.id)
            
            bndbox = et.SubElement(object, 'bndbox')
            
            xmin = et.SubElement(bndbox, 'xmin')
            xmin.text = str(bbox.xmin)
            
            xmax = et.SubElement(bndbox, 'xmax')
            xmax.text = str(bbox.xmax)
            
            ymin = et.SubElement(bndbox, 'ymin')
            ymin.text = str(bbox.ymin)
            
            ymax = et.SubElement(bndbox, 'ymax')
            ymax.text = str(bbox.ymax)
            
            score = et.SubElement(object, 'score')
            score.text = str(obj.score)

    def set_folder(self, name=FOLDER_NAME):
        folder = et.SubElement(self.annotation, 'folder')
        folder.text = name
        
    def set_filename(self, name = "ai4coral"):
        filename = et.SubElement(self.annotation, 'filename')
        filename.text = name
    
    def set_source(self, name="ai4coral vamizi Island"):
        source = et.SubElement(self.annotation, 'source')
        source.text = name

    def set_size(self, W=W, H=H, C=C):
        size = et.SubElement(self.annotation, 'size')
        width = et.SubElement(size, 'width')
        width.text = str(W)
        height = et.SubElement(size, 'height')
        height.text = str(H)
        depth = et.SubElement(size, 'depth')
        depth.text = str(C)
    
    def prettify(self):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = et.tostring(self.annotation, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def get_annotations(self, objs, filename="ai4coral", source="ai4coral"):
        self.set_folder()
        self.set_filename(filename)
        self.set_source(source)
        self.set_size()
        self.annotate(objs)
        return self.prettify()


if __name__ == "__main__":

    bbox1 = detect.BBox(xmin = 1, xmax = 2, ymin = 3, ymax = 4)    
    obj1 = detect.Object(id = 0, score = 0.8, bbox = bbox1)
    
    bbox2 = detect.BBox(xmin = 5, xmax = 6, ymin = 7, ymax = 8)    
    obj2 = detect.Object(id = 1, score = 0.7, bbox = bbox2)
    
    objs = [obj1, obj2]
    
    start = time.perf_counter()
    ann = Annotactor()
    annotation = ann.get_annotations(objs)
    annotation_time = time.perf_counter() - start
    print(annotation)
    print('It tooks %.2f ms to do the annotation' % (annotation_time * 1000))

