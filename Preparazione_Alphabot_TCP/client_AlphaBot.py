import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #AF_INET = IPV4, SOCK_STREAM = TCP

server_address = ("10.210.0.45", 8888)

try:

    client_socket.connect(server_address)

    while True:

        direction = input("Inserisci un valore da 1 a 4 sapendo che:\n 1) forward\n 2) back\n 3) right\n 4) left: ")
        while int(direction) < 1 or int(direction) > 4:
            direction = input("Reinserisci un valore da 1 a 4 sapendo che:\n 1) forward\n 2) back\n 3) right\n 4) left: ")

        speed = input("Inserisci un valore da 1 a 100 per la potenza del movimento: ")
        while int(speed) < 1 or int(speed) > 100:
            speed = input("Reinserisci un valore da 1 a 100 per la potenza del movimento: ")


        messageToSend = direction + "," + speed
        client_socket.send(messageToSend.encode('utf-8'))
    
except KeyboardInterrupt:
    print("\nChiusura della connessione...")
    client_socket.close()




