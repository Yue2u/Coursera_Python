import socket
import threading
import multiprocessing
import os

# Creating socket, Server
#
# https://docs.python.org/3/library/socket.html
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('', 10001))
# sock.listen(socket.SOMAXCONN)
#
# conn, addr = sock.accept()
# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
# #    process data
#     print(data.decode("utf-8"))
#
# conn.close()
# sock.close()

# Not handling exceptions
#
# with socket.socket() as sock:
#     sock.bind(('', 10001))
#     sock.listen()
#
#     while True:
#         conn, addr = sock.accept()
#         print(addr)
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print(data.decode("utf8"))

# Handling exceptions and using timeouts
#
# with socket.socket() as sock:
#     sock.bind(('', 10001))
#     sock.listen()
#
#     while True:
#         conn, addr = sock.accept()
#         # Waiting at most 5 seconds to get data after recv()
#         conn.settimeout(5)  # Default timeout = None if 0 => Nonblocking mode
#         with conn:
#             while True:
#                 try:
#                     data = conn.recv(1024)
#                 except socket.timeout:
#                     print("close connection by timeout")
#                     break
#                 if not data:
#                     break
#                 print(data.decode('utf-8'))

# Handling a few connections in the same time
#
def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))


def worker(sock):
    while True:
        conn, addr = sock.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()


with socket.socket() as sock:
    sock.binf('', 10001)
    sock.listen()

    workers_count = 3
    workers_list = [multiprocessing.Process(target=worker, args=(sock,))
                    for _ in range(workers_count)]

    for w in workers_list:
        w.start()

    for w in workers_list:
        w.join()

