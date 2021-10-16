import socket

# Creating socket, Client
#
# sock = socket.socket()
# sock.connect(('127.0.0.1', 10001))
# sock.sendall("ping".encode("utf-8"))
# sock.close()

# How to do the same shrter
# sock = socket.create_connection(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf-8"))
# sock.close()

# Not handling exceptions
#
# with socket.create_connection(("127.0.0.1", 10001)) as sock:
#     sock.sendall("ping".encode('utf8'))

# Handling exceptions and using timeouts
#
with socket.create_connection(('127.0.0.1', 10001), 5) as sock:  # Connect timeout set to 5
    # Send/read timeout changed to 2
    sock.settimeout(2)
    try:
        sock.sendall("ping".encode('utf-8'))
    except socket.timeot:
        print('send data timeout')
    except socket.error as ex:
        print('send data error:', ex)
