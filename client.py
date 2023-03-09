import socket
from os import system

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socke.AF_INET = ipv4
# socket.AF_INET6 = ipv6

# socket.SOCK_STREAM = TCP
# socket.SOCK_DGRAM = UDP

client.connect(('127.0.0.1',3030))
print("you connected :)")
print("for close chat type '/close'")

while True:
    message = input("-->")

    if(message == "/close"):
        client.send("/close".encode())
        client.close()
        break
    else:
        client.send(message.encode())
        data = client.recv(1024)
        print("-<"+data.decode() + ">-")

system("pause")