import detector
import bottle
from bottle import route, run


@route('/')
def greetings():
    return "Hi, I am the AI4Coral RESTful API\n"


@route('/detect')
def detect():


if __name__ == '__main__':
     run(host='localhost', port=8080)

app = bottle.default_app()

