import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host='10.210.0.45'

port = 8888

server_socket.bind((host,port))

server_socket.listen(5)

print("Server open...")

client_socket, addr = server_socket.accept()
print(f"Connesione da: {addr}")

while True:
    
    message=client_socket.recv(1024).decode('utf8')
    
    direction, speed = message.split(",")
    
    if message == '':
        break
    elif int(direction) == 1:
        print(f"Direction: Forward\nSpeed: {speed}")
    elif int(direction) == 2:
        print(f"Direction: Backward\nSpeed: {speed}")
    elif int(direction) == 3:
        print(f"Direction: Right\nSpeed: {speed}")
    elif int(direction) == 4:
        print(f"Direction: Left\nSpeed: {speed}")

print("Connessione interrotta")
server_socket.close()
    