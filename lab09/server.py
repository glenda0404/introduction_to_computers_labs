import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('waiting for connection...')

while True:

    conn, addr = s.accept()
    print('connected by ' + (str(addr)))

    while True:
        indata = conn.recv(1024)

        if indata.decode()=="EXIT":
            outdata =  "Closed connection."
            conn.send(outdata.encode())
            print((str(addr))+"closed connection.")
            print('waiting for connection...')
            break            

        else:
            print(str(addr)+":" + indata.decode())
            outdata =  "Echo:"+indata.decode()
            conn.send(outdata.encode())
        
    
