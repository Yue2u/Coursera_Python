import time
import socket


class ClientError(Exception):
    pass


def check_metrics(key, value, timestamp):
    return True


def parse_response(response):
    result = {}
    if response == '':
        return result
    for solo_metrics in response.split('\n'):
        if solo_metrics == '':
            continue
        if len(solo_metrics.split()) != 3:
            raise ClientError('Not enough args to unpack')
        key, value, timestamp = solo_metrics.split()
        try:
            value = float(value)
            timestamp = int(timestamp)
        except Exception as err:
            raise ClientError('Wrong data passed, err')
        if key not in result:
            result[key] = []
        result[key].append((int(timestamp), float(value)))

    for metrics in result.values():
        metrics.sort(key=lambda ts: ts[0])

    return result


class Client:
    def __init__(self, host, port, timeout=None):
        try:
            self.sock = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError('Connection error', err)

    def __del__(self):
        self.sock.close()

    def read_data(self):
        data = b''
        while not data.endswith(b'\n\n'):
            try:
                data += self.sock.recv(1024)
            except socket.error as err:
                raise ClientError('Get Response error', err)

        decoded_response = data.decode()
        status, info = decoded_response.split('\n', 1)
        info.strip()

        if status != 'ok':
            raise ClientError('Get Response error')
        return info

    def put(self, metric_name, value, timestamp=None):
        try:
            self.sock.sendall(
                f'put {metric_name} {value} {int(timestamp or time.time())}\n'.encode('utf8'))
            if self.sock.recv(1024).decode('utf8') != 'ok\n\n':
                raise socket.error
        except socket.error as err:
            raise ClientError('Put error', err)

    def get(self, metric_name):
        try:
            self.sock.sendall(f'get {metric_name}\n'.encode('utf8'))
        except socket.error as err:
            raise ClientError('Get error', err)

        response = self.read_data()
        return parse_response(response)


