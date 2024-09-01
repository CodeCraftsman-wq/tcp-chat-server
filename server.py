import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 10000))
server.listen()

print("Server is listening on port 9999...")

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")
    done = False
    while not done:
        msg = client.recv(1024).decode('utf-8')
        print(f"Received: {msg}")
        if msg == 'quit':
            done = True
            client.send("quit".encode('utf-8'))
        else:
            reply = input("Server: ")
            client.send(reply.encode('utf-8'))

    client.close()
