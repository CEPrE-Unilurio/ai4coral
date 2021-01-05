from config import PATH_TO_MODEL, THRESHOLD
import detector_base
import detect
from annotator import Annotator
import bottle
from bottle import route, run,  get, post, request 
import io
from PIL import Image
from PIL import ImageDraw

@route('/')
def greetings():
    return "Hi, I am the AI4Coral RESTful API\n"


@post('/detect/<filename>')
def do_detections(filename):
    try:
        try:
            start = time.perf_counter()
    
            interpreter = detector_base.make_interpreter(PATH_TO_MODEL)
            interpreter.allocate_tensors()

            image = Image.open(request.body)
            scale = detect.set_input(interpreter, image.size,
                           lambda size: image.resize(size, Image.ANTIALIAS))
            
            interpreter.invoke()
            objs = detect.get_output(interpreter, THRESHOLD, scale)
            
            ann = Annotator()
            annotations = ann.get_annotations(objs=objs, filename=filename)

            inference_annotation_time = time.perf_counter() - start
            print('%.2f ms' % (inference_annotation_time * 1000))

            return annotations
        except:
            raise ValueError
    except ValueError:
        response.status = 400
        return

if __name__ == '__main__':
     run(host='localhost', port=8080)

app = bottle.default_app()
