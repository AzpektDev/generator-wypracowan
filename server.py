import socket

import openai

openai.api_key = "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"

host = socket.gethostname()
port = 10001

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen(1)

print("Server is listening...")

while True:
    clientsocket, addr = serversocket.accept()

    print(f"Connection from {addr} has been established.")
    data = clientsocket.recv(1024).decode('utf-8')
    print(f"Data received from client: {data}")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=data,
        max_tokens=150,
        temperature=0.7
    )

    clientsocket.send(response['choices'][0]['text'].encode('utf-8'))

    clientsocket.close()