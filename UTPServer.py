import socket

host = "127.0.0.5"
port = 8075

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((host, port))
    print("Server started on {}:{}".format(host, port))
    
    while True:
        data, addr = s.recvfrom(1024)
        print("Received data from {}: {}".format(addr, data.decode()))
        s.sendto(data, addr)