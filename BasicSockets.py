import socket

try:
    print("Fully qualified domain name: "+ socket.getfqdn("8.8.8.8"))
    print("Host name to IP address: "+ socket.gethostbyname("WWW.python.org"))
    print("Host name to IP address, extended: "+ str(socket.gethostbyname_ex("WWW.python.org")))
    print("Get host name of local machine: "+ socket.gethostname())

except Exception as err:
    print ("Error: "+ str(err))
