import socket
from config import CONNECTION

query = input("temat: ")
print(query)

b = query.encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(CONNECTION)

    s.sendall(b) 

print('Data sent to server')
