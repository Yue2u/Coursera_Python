import socket
import select


sock = socket.socket()
sock.bind(('', 10001))
sock.listen()


# Handle 2 requests in the same time in one thread
conn1, addr = sock.accept()
conn2, addr = sock.accept()

# Неблокирующий режим
conn1.setblocking(0)
conn2.setblocking(0)

# по файловым дескрипторам добавляем события
epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2
}

# Обрабатываем соединения с event loop
while True:
    events = epoll.poll(1)
    for fileno, event in events:
        if event & select.EPOLLIN:
            data = conn_map[fileno].recv(1024)
            print(data.decode('utf8'))
        elif event & select.EPOLLOUT:
            conn_map[fileno].send("ping".encode('utf8'))
