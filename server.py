from flask import Flask, request
from flask_socketio import SocketIO
from flask_cors import CORS  # Import the CORS class

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask application
socketio = SocketIO(app)

@app.route('/b.htm', methods=['POST'])
def handle_message():
    data = request.get_json()
    print(f"Received data: {data}")
    socketio.send(data, room=data['recipient'])
    return {"status": "success"}

if __name__ == '__main__':
    socketio.run(app)