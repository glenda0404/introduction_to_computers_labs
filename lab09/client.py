import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    outdata = input('Send:')
    s.send(outdata.encode())
    indata = s.recv(1024)
    print(indata.decode())
    if indata.decode()=="Closed connection.":
        s.close()
        break

    


