
import socket, threading, time, re, os, sys


def tcplink(sock, addr):
    print("Accept new conn from %s:%s..." % addr)

    while True:
        data = sock.recv(1024) # receive request
        time.sleep(1)
        if data: # if any data recved from the client
            
            # TODO process the data
            print(data)
            
            # send response
            sock.send("\nHTTP/1.1 200 OK\n\n".encode())
            # send images (content)
            with open('myimage.png', 'rb') as f:
                content = f.read()
                sock.sendall(content)
            break
    sock.close() # close conn
    print("Conn from %s:%s closed." % addr)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Init socket
    s.bind(('127.0.0.1', 9901)) # IP address and Port number
    s.listen(5) # at most 5 clients
    
    print("wait for conn...")
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
