import socket
import random

host = socket.gethostname()

port = 9999


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen(1)

print("Server is listening...")

while True:
    clientsocket, addr = serversocket.accept()

    print(f"Connection from {addr} has been established.")
    data = clientsocket.recv(1024).decode('utf-8')
    print(f"Data received from client: {data}")

    with open("received_from_client.txt", "w") as f:
        f.write(data)

    random_num = random.randint(1, 1000)
    clientsocket.send(str(random_num).encode('utf-8'))

    clientsocket.close()