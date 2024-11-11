import socket
from datetime import datetime

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the server (replace '127.0.0.1' with server IP)

    while True:
        # Send message to server
        message = input("Enter message to server: ")
        client_socket.send(message.encode())

        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if message.lower() == 'quit':
            print("Closing connection.")
            client_socket.close()
            break

        # Receive response from server
        server_message = client_socket.recv(1024).decode()

        if server_message.lower() == 'quit':
            print(f"[{timestamp}] Server disconnected")
            client_socket.close()
            break

        print(f"[{timestamp}] Server: {server_message}")

# Run the client
if __name__ == "__main__":
    start_client()
