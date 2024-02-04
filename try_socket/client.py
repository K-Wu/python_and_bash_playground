import socket

def connect_to_dummy_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")
        data = s.recv(1024)
        print(f"Received: {data.decode()}")

if __name__ == '__main__':
    connect_to_dummy_server()