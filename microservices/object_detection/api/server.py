from detector import app
from cheroot.wsgi import Server

server = Server(
    ('0.0.0.0', 8080),
    app,
    server_name='AI4Coral 1.0',
    numthreads=30)

try:
    server.start()
except KeyboardInterrupt:
    server.stop()
