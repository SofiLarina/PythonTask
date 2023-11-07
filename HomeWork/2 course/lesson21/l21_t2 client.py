import socket

def main():
    server_address = ('localhost', 55000)

    file_name = input("Введите название файла: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    client_socket.send(file_name.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    client_socket.close()


if __name__ == '__main__':
    main()