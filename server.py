import socket
import openai
from colorama import Fore, Back, Style
from config import connection

openai.api_key = "" # paste here your openai api key!! (chill, my key was revoked)

# host = socket.gethostname()
# port = 10004

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(connection)

serversocket.listen(1)

print(Fore.GREEN + "Server is listening..." + Style.RESET_ALL)

while True:
    clientsocket, addr = serversocket.accept()

    print(f"{Fore.GREEN}Connection from {addr} has been established.{Style.RESET_ALL}")
    data = b''
    while b'\r\n\r\n-EndStream-' not in data:
        data += clientsocket.recv(1024)
    data = data.decode('utf-8')
    data = data.replace("\r\n\r\n-EndStream-", "")

    print(f"{Fore.GREEN}Data received from client: {data}{Style.RESET_ALL}")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Napisz rozprawkę/wypracowanie na temat " + data,
        max_tokens=800,
        temperature=0.7
    )

    content_length = len(response['choices'][0]['text'])
    response = response['choices'][0]['text'] + "\r\n\r\n-EndStream-"

    clientsocket.send(response.encode('utf-8'))

    clientsocket.close()