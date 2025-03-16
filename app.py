from flask import Flask
from flask_cors import CORS  
import socket

app = Flask(__name__)
CORS(app)  

def get_server_response():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(b'Hello from client!')
        data = client_socket.recv(1024)
        return data.decode()

@app.route('/api')
def api():
    response = get_server_response()
    return response

if __name__ == '__main__':
    app.run(debug=True)
