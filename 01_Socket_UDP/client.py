#CLIENT

import socket

server_address = ("192.168.1.124", 8800) #indirizzo ip e porta del server
BUFFER_SIZE = 4092      #dichiarare quanti bit posso trasmettere, se mando più di 4092 allora la parte ulteriore verrà tagliata
message = "Sono il Client"

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #è un socket di tipo udp

try:
    udp_client_socket.sendto(message.encode(), server_address)
    print("Ora aspetto messaggio di ritorno...")
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f"La risposta dal server è: {data.decode()}")
finally:
    udp_client_socket.close()