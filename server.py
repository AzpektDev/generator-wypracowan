import socket
import openai

openai.api_key = "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"

host = socket.gethostname()
port = 10002

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen(1)

print("Server is listening...")

while True:
    clientsocket, addr = serversocket.accept()

    print(f"Connection from {addr} has been established.")
    data = b''
    while b'\r\n\r\n-EndStream-' not in data:
        data += clientsocket.recv(1024)
    data = data.decode('utf-8')
    data = data.replace("\r\n\r\n-EndStream-", "")

    print(f"Data received from client: {data}")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=data,
        max_tokens=150,
        temperature=0.7
    )

    content_length = len(response['choices'][0]['text'])
    response = response['choices'][0]['text'] + "\r\n\r\n-EndStream-"

    clientsocket.send(response.encode('utf-8'))

    clientsocket.close()