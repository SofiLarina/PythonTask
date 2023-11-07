"""
Разработайте приложение, которое будет запрашивать у пользователя название файла,
а затем отправлять содержимое этого файла серверу. Сервер будет выводить сообщение, подсчитывать количество слов и возвращать ответ.
Протестируйте на test.txt
"""
import socket


def count_words(text):
    words = text.split()
    count = len(words)
    return count


def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    file_name = request.strip()

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            word_count = count_words(content)
            response = f"Содержимое файла {file_name}: {content}\nКоличество слов: {word_count}"
            client_socket.send(response.encode('utf-8'))
    except FileNotFoundError:
        response = f"Файл {file_name} не найден"
        client_socket.send(response.encode('utf-8'))


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 55000))
    server_socket.listen(10)
    print("Сервер запущен...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Подключение от {address[0]}:{address[1]}")
        handle_client(client_socket)
        client_socket.close()


if __name__ == '__main__':
    main()