import json
import socket

with open('server-conf.json') as f:
    conf = json.load(f)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((conf['HOST'], conf['PORT']))
server.send(json.dumps({
    'purpose': 'register',
    'from': 'python',
    'to': '',
    'data': {}
}).encode() + b'\n')

def send_to(language, msg, purpose='send'):
    server.send(json.dumps({
        'purpose': purpose,
        'from': 'python',
        'to': language,
        'data': msg
    }).encode() + b'\n')

def receive_nowait():
    return json.loads(next(server.makefile('b')))

def receive():
    while True:
        try:
            return receive_nowait()
        except StopIteration:
            pass

if __name__ == '__main__':
    send_to('python', 'testing')
    print(receive())
