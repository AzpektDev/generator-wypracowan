import socket

host = socket.gethostname()
port = 10002

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

# data = "Hello, server!"
data = input("give temat: ")
data = data + "\r\n\r\n-EndStream-"
clientsocket.send(data.encode('utf-8'))

response = b''
while b'\r\n\r\n-EndStream-' not in response:
    response += clientsocket.recv(1024)
response = response.decode('utf-8')
response = response.replace("\r\n\r\n-EndStream-", "")
print(f"Response from server: {response}")


with open("server_response.txt", "w") as f:
    f.write(response)

clientsocket.close()

