from od.settings import common as config
from xml.etree import ElementTree as et
from xml.dom import minidom

class PascalVocXML:
  """ A Class used to create a pascal VOC XML 
    
    Attributes
    ----------
    annotation : ElementTree Object
      The root element of the created XML document  
  """

  def __init__(self, filename=None):
    """
      Init the XML document with basic info
    
      Args:
        filename: name of the XML file
    """
    self.annotation = et.Element('annotation')
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
    
  def add_object_element(self, obj=None, label=None):  
    """  Add detected object to the XML file

        Args:
          obj: the detected object
          label: the name of the detected object
    """
    bbox = obj.bbox
    object = et.SubElement(self.annotation, 'object')
    name = et.SubElement(object, "name")
    name.text = label
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
         
  def get_annotations(self):
    """ Return a pretty XML string representing the Pascal VOC XML annotation """
    rough_string = et.tostring(self.annotation, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")