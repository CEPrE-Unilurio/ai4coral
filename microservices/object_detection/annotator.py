from settings import common as config
import detector_base
from xml.etree import ElementTree as et
from xml.dom import minidom
import time
from timing import timeit

class Annotator:
    
    def __init__(self):
        self.annotation = et.Element('annotation')
    
    def annotate(self, objs=None):
        LABELS = detector_base.load_labels(config.PATH_TO_LABELS)
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

    def set_folder(self, name=config.FOLDER_NAME):
        folder = et.SubElement(self.annotation, 'folder')
        folder.text = name
        
    def set_filename(self, name = "ai4coral"):
        filename = et.SubElement(self.annotation, 'filename')
        filename.text = name
    
    def set_source(self, name="ai4coral vamizi Island"):
        source = et.SubElement(self.annotation, 'source')
        source.text = name

    def set_size(self, input_shape=config.INPUT_SHAPE):
        size = et.SubElement(self.annotation, 'size')
        width = et.SubElement(size, 'width')
        width.text = str(input_shape[1])
        height = et.SubElement(size, 'height')
        height.text = str(input_shape[0])
        depth = et.SubElement(size, 'depth')
        depth.text = str(input_shape[2])
    
    def prettify(self):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = et.tostring(self.annotation, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    
    @timeit
    def get_annotations(self, objs, filename="ai4coral", source="ai4coral", **kwargs):
        self.set_folder()
        self.set_filename(filename)
        self.set_source(source)
        self.set_size()
        self.annotate(objs)
        return self.prettify()