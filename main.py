from socketIO_client import SocketIO

from monitoring import (get_cpu_temperature,
                        get_local_ip_address,
                        get_cpu_use,
                        get_ram_info)


def handle_response(data):
    print(data)


if __name__ == '__main__':
    with SocketIO('192.168.1.112', 5000) as socketIO:
        # socketIO.on('response', handle_response)
        ip = get_local_ip_address()
        socketIO.emit('connected', ip)

        while True:
            socketIO.emit('temperature_in', {'temp': get_cpu_temperature(), 'ip': ip})
            socketIO.emit('cpu_in', {'cpu': get_cpu_use(), 'ip': ip})
            socketIO.emit('ram_in', {'ram': get_ram_info(), 'ip': ip})
            socketIO.wait(seconds=2)
