import socket
from   cheroot import wsgi
from   app import app

server = wsgi.Server(
    bind_addr=('0.0.0.0', 8000),
    wsgi_app=app,
    request_queue_size=500,
    server_name=socket.gethostname()
)

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()
