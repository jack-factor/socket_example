from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    # emit(username + ' has entered the room.', room=room)
    send({'data': 'Entered room: ' + room}, room=room)


@socketio.on('my_room_event')
def send_room_message(message):
    emit('my response',
         {'data': message['data']},
         room=message['room'])


if __name__ == '__main__':
    socketio.run(app)
