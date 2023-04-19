import socket

host = socket.gethostname()
port = 10001

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

# data = "Hello, server!"
data = input("give temat: ")
clientsocket.send(data.encode('utf-8'))


response = clientsocket.recv(1024).decode('utf-8')
print(f"Response from server: {response}")


with open("server_response.txt", "w") as f:
    f.write(response)


clientsocket.close()

