import socket
import wspy

class EchoConnection(wspy.Connection):
    def onopen(self):
        print 'Connection opened at %s:%d' % self.sock.getpeername()
        self.send(wspy.TextMessage(u"test"))

    def onmessage(self, message):
        print 'Received message "%s"' % message.payload

    def onclose(self, code, reason):
        print 'Connection closed'

server = wspy.websocket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 12345))
server.listen(5)

while True:
    client, addr = server.accept()
    EchoConnection(client).receive_forever()