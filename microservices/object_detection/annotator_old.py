from settings import common as config
import detector_base
from xml.etree import ElementTree as et
from xml.dom import minidom
import time
from timing import timeit

class PascalVocXML:
  """ A Class used to create a pascal VOC XML 
    
    Attributes
    ----------
    annotatio : ElementTree
      The root element of the created XML document  
  """

  def __init__(self, objs=None, filename=None):
    """
      Args:
        objs: list of detected objects
    """
    self.annotation = et.Element('annotation')
    self.build_pascal_voc_xml(objs=objs, filename=filename)

  def build_pascal_voc_xml(self, objs=None, filename=None):
    """ Build a XML document from the list of detected objects """
    folder = et.SubElement(self.annotation, 'folder')
    folder.text = config.FOLDER_NAME
    filename_ = et.SubElement(self.annotation, 'filename')
    filename_.text = filename
    source = et.SubElement(self.annotation, 'source')
    source.text = config.SOURCE_NAME
    size = et.SubElement(self.annotation, 'size')
    width = et.SubElement(size, 'width')
    width.text = str(config.INPUT_SHAPE[1])
    height = et.SubElement(size, 'height')
    height.text = str(config.INPUT_SHAPE[0])
    depth = et.SubElement(size, 'depth')
    depth.text = str(config.INPUT_SHAPE[2])
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
         
  @timeit
  def get_annotations(self, **kwargs):
    """ Return a pretty XML string representing the Pascal VOC XML annotation """
    rough_string = et.tostring(self.annotation, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")