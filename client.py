import socket
from colorama import Fore, Back, Style
from getpass import getpass
from datetime import datetime
from config import connection

user = input(Fore.BLUE + "login: " + Style.RESET_ALL)
password = getpass(Fore.BLUE + "password: " + Style.RESET_ALL)

# host = socket.gethostname()
# port = 10004

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(connection)

# data = "Hello, server!"
data = input(Fore.BLUE + "Give temat rozprawki/wypracowania: " + Style.RESET_ALL)
data = data + "\r\n\r\n-EndStream-"
clientsocket.send(data.encode('utf-8'))

response = b''
while b'\r\n\r\n-EndStream-' not in response:
    response += clientsocket.recv(1024)
response = response.decode('utf-8')
response = response.replace("\r\n\r\n-EndStream-", "")
print(f"{Fore.GREEN}Response from server:{Style.RESET_ALL} {Fore.MAGENTA}{response}{Style.RESET_ALL}")


with open("server_response.txt", "w") as f:
    f.write(Fore.BLUE + response + Style.RESET_ALL)

with open(f"history/{user}-{password}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-history.txt", "w") as f:
    f.write(response.split("\r\n\r\n")[0])


clientsocket.close()

