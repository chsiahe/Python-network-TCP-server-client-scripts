import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 9703)
print('Connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Receive the server's IP address
    data = sock.recv(1024)
    print('Server IP address:', data.decode())

   
