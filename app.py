from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__);
socketio = SocketIO(app)


# view functions
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/second')
def second():
    return render_template('second.html')


# socket event functions
@socketio.on('server_connect')
def handle_conection(dataIn):
    print(dataIn['data'])



if __name__ == '__main__':
    socketio.run(app)