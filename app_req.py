#!/usr/bin/python
import socket
import json
UDP_IP='10.0.0.8'
UDP_PORT=10111
data=dict()
data['len']=4
data['server']=['10.0.0.1','10.0.0.2','10.0.1.1','10.0.1.2']
send_json=json.dumps(data)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(send_json,(UDP_IP,UDP_PORT))
