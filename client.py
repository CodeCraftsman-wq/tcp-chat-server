import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",10000))

done =False

while not done:
    client.send(input("Message: ").encode('utf-8'))

    msg = client.recv(1024).decode('utf-8')
    print(msg)
    if msg=="quit":
        done =True
