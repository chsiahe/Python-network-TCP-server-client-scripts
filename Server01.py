import socket
import time
import os
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9703)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)

        # Send the client its IP address
        connection.sendall(client_address[0].encode())

        # Set a timeout on the socket
        connection.settimeout(20.0)

        # Wait for the client to send a command
        while True:
            data = connection.recv(16)
            command = data.decode().strip()

            if not data:
                # If the client closed the connection or did not respond within the timeout period, break out of the loop
                break

            elif command == 'TIME':
                # If the command is 'TIME', send the current time to the client
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                connection.sendall(current_time.encode())

            elif command == 'IP':
                # If the command is 'IP', send the client's IP address to the client
                connection.sendall(client_address[0].encode())

            elif command == 'OS':
                # If the command is 'OS', send information on the server's operating system to the client
                os_info = os.uname()
                connection.sendall(' '.join(os_info).encode())

            elif command == 'FILE':
                # If the command is 'FILE', send a dummy file to the client
                with open('dummy_file.txt', 'r') as f:
                    connection.sendall(f.read().encode())

            elif command == 'EXIT':
                # If the command is 'EXIT', close all open sockets and exit the program
                connection.close()
                sock.close()
                sys.exit()

    finally:
        # Close the connection
        connection.close()
