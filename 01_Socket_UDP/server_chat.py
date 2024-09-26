## PROGRAMMA SERVER DI UNA STRUTTURA CLIENT-SERVER PER INVIARE 10 MESSAGGI

import socket

server_address=("192.168.178.110", 8800) #indirizzo_ip, porta

BUFFER_SIZE = 4092 #massima dimensione trasmissibile

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #..., socket di tipo UDP

udp_server_socket.bind(("0.0.0.0", 8800)) #vado a legare il socket all'ip e alla porta del server, in questo caso accetta connessioni a qualsiasi ip del pc

while True:
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE) #mette in ascolto il server, bloccante
    if data == "break":
        break
    print(f"{data.decode()}")

    message = input("Inserisci un messaggio da inviare al client: ")
    message_to_client = "SERVER: " + message
    if message == "break":
        udp_server_socket.sendto(message_to_client.encode(), address) #rimando al client un messaggio
        break
    else:
        udp_server_socket.sendto(message_to_client.encode(), address) #rimando al client un messaggio

udp_server_socket.close() #chiudo la connessione