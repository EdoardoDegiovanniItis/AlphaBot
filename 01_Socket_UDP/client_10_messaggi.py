#PROGRAMMA CLIENT DI UNA STRUTTURA CLIENT-SERVER PER INVIARE 10 MESSAGGI

import socket

server_address = ("10.210.0.20", 8800) #indirizzo ip e porta del server
BUFFER_SIZE = 4092      #dichiarare quanti bit posso trasmettere, se mando più di 4092 allora la parte ulteriore verrà tagliata
message = "Sono il Client"
contatore = 0

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #è un socket di tipo udp

for _ in range(0, 10):
    contatore += 1
    udp_client_socket.sendto(message.encode(), server_address)
    print("Ora aspetto messaggio di ritorno...")
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f"La risposta dal server è: {data.decode()}")
    print(contatore)

udp_client_socket.close()
