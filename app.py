from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

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
def handle_conection(data):
    print(data['data'])

@socketio.on('slider_moved')
def handle_slider_move(data):
    print('slider moved with value = ' + data['value'] + '\n')
    emit('move_slider', {'value': data['value']}, room='stream_room')

# room event functions
@socketio.on('join_room')
def on_join_room(data):
    room = data['room']
    join_room(room)


if __name__ == '__main__':
    socketio.run(app)