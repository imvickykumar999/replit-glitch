import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))  # Bind to all IP addresses on port 12345
    server.listen(5)
    print('Server started, waiting for connections...')

    while True:
        client_socket, client_address = server.accept()
        print(f'Connection from {client_address}')
        handle_client(client_socket)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f'Received: {message}')
                client_socket.send(f'Echo: {message}'.encode('utf-8'))
            else:
                break
        except:
            break
    client_socket.close()

if __name__ == "__main__":
    start_server()

