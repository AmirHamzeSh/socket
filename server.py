import socket
from os import system

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 3030))
server.listen(1)
print("waiting for a connect...")
connection, client = server.accept()
print(client, 'Connected\n')

while True:
    data = connection.recv(1024)
    if data.decode() == "/close":
        connection.close()
        break
    else:
        print("-<" + data.decode() + ">-")
        message = input("-->")

        connection.send(message.encode())

system("pause")