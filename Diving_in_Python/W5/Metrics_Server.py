import asyncio


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    data_dict = dict()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        data = data.strip()
        if data == '':
            return 'error\nwrong command\n\n'
        if len(data.split(' ', 1)) != 2:
            return 'error\nwrong command\n\n'
        request_type, request_body = data.split(' ', 1)
        if request_type == 'get':
            return self.process_get(request_body)
        elif request_type == 'put':
            return self.process_put(request_body)
        else:
            return 'error\nwrong command\n\n'

    def process_get(self, data):
        data = data.strip()
        if data == '' or ' ' in data:
            return 'error\nwrong command\n\n'
        result = 'ok\n'
        if data == '*':
            for key, datas in self.data_dict.items():
                for timestamp, value in datas.items():
                    result += f'{key} {value} {timestamp}\n'
        elif data in self.data_dict:
            for timestamp, value in self.data_dict[data].items():
                result += f'{data} {value} {timestamp}\n'
        result += '\n'
        return result

    def process_put(self, data):
        data = data.strip()
        if len(data.split()) != 3:
            return 'error\nwrong command\n\n'
        metric_name, value, timestamp = data.split()
        try:
            value = float(value)
            timestamp = int(timestamp)
        except ValueError:
            return 'error\nwrong command\n\n'
        if metric_name not in self.data_dict:
            self.data_dict[metric_name] = dict()
        self.data_dict[metric_name][timestamp] = value
        return 'ok\n\n'
