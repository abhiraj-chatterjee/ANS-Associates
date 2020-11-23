# !/usr/bin/python3

import socket
import common_ports
import ipaddress

def isIPAddress(target):
    for each in target:
        if each != '.' and (ord(each) < 48 or ord(each) > 57):
            return False
    return True

def get_open_ports(target, port_range, verboseMode=False):
    open_ports = []

    try: host = socket.gethostbyname(target)
    except:
        if isIPAddress(target):
            return 'Error: Invalid IP address'
        else:
            return 'Error: Invalid hostname'   

    for port in range(port_range[0], port_range[1]+1):
        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        s.settimeout(5)

        if s.connect_ex((host,port)): 
            continue
        else: 
            open_ports.append(port)

        s.close()

    if verboseMode:
        try:
            result = socket.gethostbyaddr(host)
            output = 'Open ports for {URL} ({IP_ADDR})\nPORT\tSERVICE'.format(URL=result[0], IP_ADDR=host)
        except:
            output = 'Open ports for {IP_ADDR}\nPORT\tSERVICE'.format(IP_ADDR=host)
        for eachPort in open_ports:
            output += '\n{PORT}\t{SERVICE}'.format(PORT=eachPort, SERVICE=common_ports.ports_and_services[eachPort])
        return output
    else:
        return(open_ports)