import socket
host = "10.4.15.76"
port = 2000
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((host, port))
    s.sendall(b"Hello Python World")
    data = s.recv(1024)

print("Receivd response: "+ repr(data))