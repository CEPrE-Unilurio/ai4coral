from bottle import Bottle, request

app = Bottle()

@app.get('/')
def greetings():
    return "Hi, I am an AI4Coral RESTful API"
