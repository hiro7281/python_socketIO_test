import socketio

class MyCustomNamespace(socketio.ClientNamespace):
    def on_connect(self):
        print('connection established robot')

    def on_reconnect(self):
        print('reconnection established robot')

    def on_disconnect(self):
        print('disconnected from server robot')

    def on_my_event(self, data):
        self.emit('my_response', data)

    def hello(self):
        self.emit('hello', {'hello': 'my response'})

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def on_reconnect(self):
    print('reconnection established robot')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('hello', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.register_namespace(MyCustomNamespace('/robotControl'))

sio.connect('http://192.168.0.9:3001')
sio.emit('hello', {'my name': 'alice'}, namespace='/robotControl')
#developping...
#more develop...
