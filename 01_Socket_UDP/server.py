## PROGRAMMA SERVER DI UNA STRUTTURA CLIENT-SERVER PREPARAZIONE ALPHABOT

import socket

server_address=("192.168.1.124", 8800) #indirizzo_ip, porta

BUFFER_SIZE = 4092 #massima dimensione trasmissibile

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #..., socket di tipo UDP

udp_server_socket.bind(("0.0.0.0", 8800)) #vado a legare il socket all'ip e alla porta del server, in questo caso accetta connessioni a qualsiasi ip del pc

print("Sono in ascolto...")
    
data, address = udp_server_socket.recvfrom(BUFFER_SIZE) #mette in ascolto il server, bloccante


print(f"messaggio ricevuto: {data.decode()} da {address}")

messageForClient = "messaggio di ritorno"
udp_server_socket.sendto(messageForClient.encode(), address) #rimando al client un messaggio

print("Ho rimandato il messaggio")

udp_server_socket.close() #chiudo la connessione