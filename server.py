from socketserver import BaseRequestHandler, TCPServer
import json
import threading

# Slog (Short Logger)
globals().update({t:(lambda t,c:lambda m:print(f'[\033[{c}m{t.upper()}\033[0m] {m}'))(t,c)for t,c in{'error':31,'debug':32,'warning':33,'info':34}.items()})

with open('server-conf.json') as f:
    conf = json.load(f)

servers = {}

def get_data(sock):
    with sock.makefile('b') as f:
        for s in f:
            yield json.loads(s.decode())

def validate(data):
    return all(x in data for x in ['purpose', 'from', 'to', 'data'])

class Handler(BaseRequestHandler):
    def handle(self):
        global ls
        for self.data in get_data(self.request):
            if not validate(self.data): warning('Data does not match schema.')
            debug(self.data['from'] + ' -> ' + repr(self.data))
            if self.data['purpose'] == 'register':
                info(f"Registering {':'.join(map(str,self.client_address))} as {self.data['from']}")
                if self.data['from'] in servers: warning(f"Overwriting {self.data['from']}")
                servers[self.data['from']] = self.request
            elif self.data['purpose'] == 'send':
                info(f"Sending data to {self.data['to']}")
                servers[self.data['to']].sendall(json.dumps(self.data).encode() + b'\n')
            elif self.data['purpose'] == 'deregister':
                # Add logging here when used
                servers.pop(self.data['from'])
            elif self.data['purpose'] == 'echo':
                info(f"Echoing {self.data['from']}: {self.data}")
                servers[self.data['from']].sendall(json.dumps(self.data).encode() + b'\n')

try:
    info('Starting server...')
    with TCPServer((conf['HOST'], conf['PORT']), Handler) as server:
        server.serve_forever()
finally:
    info('Shutting down server')
    for x in servers.values():
        x.sendall(json.dumps('stop').encode())
    info('Server shutdown.')
