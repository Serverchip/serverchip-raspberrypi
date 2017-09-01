import os
import socket


def get_cpu_temperature():
    """Return CPU temperature as a character string"""
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


def get_ram_info():
    """
    Return RAM information (unit=kb) in a list
    Index 0: total RAM
    Index 1: used RAM
    Index 2: free RAM
    """
    p = os.popen('free')
    i = 0
    while True:
        i = i + 1
        line = p.readline()
        if i == 2:
            return line.split()[1:4]


def get_cpu_use():
    """Return % of CPU used by user as a character string"""
    return str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())


def get_disk_space():
    """
    Return information about disk space as a list (unit included)
    Index 0: total disk space
    Index 1: used disk space
    Index 2: remaining disk space
    Index 3: percentage of disk used
    """
    p = os.popen("df -h /")
    i = 0
    while True:
        i = i + 1
        line = p.readline()
        if i == 2:
            return line.split()[1:5]


def get_local_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    return s.getsockname()[0]
