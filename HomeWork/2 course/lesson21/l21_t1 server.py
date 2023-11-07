"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе.
Сигналом окончания связи служит слово "Пока".
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 55000))
server_socket.listen(1)

print("Сервер начал работу...")

conn, addr = server_socket.accept()
print("Подключение к", addr)

while True:
    message = conn.recv(1024).decode()
    print("Клиент:", message)
    if message.lower() == "пока":
        break
    response = input("Сервер: ")
    conn.send(response.encode())

conn.close()