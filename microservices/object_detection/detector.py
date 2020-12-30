import bottle
from bottle import route, run


@route('/')
def greetings():
    return "Hi, I am the AI4Coral RESTful API\n"

@route('/predict', method='POST')
def predict():
    pass
    return

if __name__ == '__main__':
     run(host='localhost', port=8080, reloader=True)

app = bottle.default_app()

