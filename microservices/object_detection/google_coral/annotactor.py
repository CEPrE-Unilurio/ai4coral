from config import *
from xml.etree import ElementTree as et
from xml.dom import minidom

class Annotactor:
    
    def __init__(self):
        self.annotation = et.Element('annotation')
    
    def add_objects(self, objs=None):
        object = self.annotation.getElementsByTagName("object")
        self.annotation.lastChild.appendChild(object) 
        
        for obj in self.annotation.getElementsByTagName("object"):
            print(obj.toxml())

    def set_folder(self, name=FOLDER_NAME):
        folder = et.SubElement(self.annotation, 'folder')
        folder.text = name
        
    def set_filename(self, name):
        pass

    def set_size(self, W=W, H=H, C=C):
        pass 
    
    def prettify(self):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = et.tostring(self.annotation, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def get_annotations(self):
        self.set_folder()
        return self.prettify()


if __name__ == "__main__":

    ann = Annotactor()
    annotation = ann.get_annotations()
    print(annotation)
