import socket
import threading
from datetime import datetime

# Function to handle client connection
def handle_client(client_socket):
    while True:
        # Receive message from the client
        message = client_socket.recv(1024).decode()
        
        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if message.lower() == 'quit':
            print(f"[{timestamp}] Client disconnected")
            client_socket.close()
            break
        
        print(f"[{timestamp}] Client: {message}")
        # Send a reply to the client
        server_message = input("Enter message to client: ")
        client_socket.send(server_message.encode())

        if server_message.lower() == 'quit':
            print("Closing connection.")
            client_socket.close()
            break

# Start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all network interfaces on port 12345
    server_socket.listen(1)
    print("Server is listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Handle the client in a new thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Run the server
if __name__ == "__main__":
    start_server()
