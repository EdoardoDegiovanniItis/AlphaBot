#PROGRAMMA CLIENT DI UNA STRUTTURA CLIENT-SERVER PER INVIARE 10 MESSAGGI

import socket

server_address = ("192.168.178.110", 8800) #indirizzo ip e porta del server
BUFFER_SIZE = 4092      #dichiarare quanti bit posso trasmettere, se mando più di 4092 allora la parte ulteriore verrà tagliata

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #è un socket di tipo udp

while True:
    message = input("Inserisci un messaggio da inviare al server: ")
    message_to_server = "CLIENT: " + message
    if message == "break":
        udp_client_socket.sendto(message_to_server.encode(), server_address)
        break
    else:
        udp_client_socket.sendto(message_to_server.encode(), server_address)
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    if data == "break":
        break
    print(f"{data.decode()}")

udp_client_socket.close()