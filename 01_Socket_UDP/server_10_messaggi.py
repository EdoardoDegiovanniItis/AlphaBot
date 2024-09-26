## PROGRAMMA SERVER DI UNA STRUTTURA CLIENT-SERVER PER INVIARE 10 MESSAGGI

import socket

server_address=("10.210.0.20", 8800) #indirizzo_ip, porta

BUFFER_SIZE = 4092 #massima dimensione trasmissibile
contermessage = 0

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #..., socket di tipo UDP

udp_server_socket.bind(("0.0.0.0", 8800)) #vado a legare il socket all'ip e alla porta del server, in questo caso accetta connessioni a qualsiasi ip del pc


while contermessage < 10:
    contermessage += 1
    print("Sono in ascolto...")

    data, address = udp_server_socket.recvfrom(BUFFER_SIZE) #mette in ascolto il server, bloccante

    print(f"messaggio ricevuto: {data.decode()} da {address}")
    messageForClient = "messaggio di ritorno"
    udp_server_socket.sendto(messageForClient.encode(), address) #rimando al client un messaggio
    print(contermessage)

udp_server_socket.close() #chiudo la connessione