from config import *
import xml.dom.minidom as md

class Annotactor:
    
    def __init__(self):
        self.annotations = md.parse(SAMPLE_XML_ANNOTATION_PATH)
    
    def add_object(self, obj):
        pass

    def set_folder(self, name):
        pass

    def set_filename(self, name):
        pass

    def set_path(self, path):
        pass

    def set_size(self, W=W, H=H, C=C):
        pass


    def get_annotations(self):
        
    
        return self.annotations


if __name__ == "__main__":

    ann = Annotactor()
    doc = ann.get_annotations()
    print(doc.nodeName)
    print(doc.firstChild.tagName)
