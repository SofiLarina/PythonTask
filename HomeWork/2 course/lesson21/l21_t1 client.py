import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 55000))

while True:
    message = input("Клиент: ")
    client_socket.send(message.encode())
    if message.lower() == "пока":
        break
    response = client_socket.recv(1024).decode()
    print("Сервер:", response)

client_socket.close()