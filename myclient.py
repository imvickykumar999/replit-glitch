import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.0.18', 12345))  # Replace with your server's IP and port

    while True:
        message = input('Enter message: ')
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f'Received: {response}')

if __name__ == "__main__":
    start_client()

