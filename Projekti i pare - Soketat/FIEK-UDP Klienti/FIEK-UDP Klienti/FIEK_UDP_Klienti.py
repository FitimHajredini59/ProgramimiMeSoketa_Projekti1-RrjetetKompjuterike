import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

#serverName = 'localhost'
serverName = input("Shenoni emrin e serverit: ")
#serverPort = 12000
Port = input("Shenoni portin: ")
serverPort = int(Port)
addr = (serverName, serverPort)

while 1:
    print("===========================================================================================================")
    var = input("Zgjedhni njeren nga kerkesat:" +
              "\nIPADRESA " +
              "\nNUMRIIPORTIT " +
              "\nBASHKETINGELLORE " +
              "\nPRINTIMI " +
              "\nEMRIIKOMPJUTERIT " +
              "\nKOHA " +
              "\nLOJA " +
              "\nFIBONACCI " +
              "\nKONVERTIMI " +
              "\nFUQIA " +
              "\nPRIME " +
              "\n\nOse shenoni 0 ose zero ose ZERO per ta mbyllyr programin\n ")
    if not var:
        print("Ju lutem shenoni njeren nga kerkesat!")
        continue
    if (var == "0") or (var == "zero") or (var == "ZERO"):
        client_socket.close()
        break
    client_socket.sendto(var.encode(), addr)
    try:
        data, server = client_socket.recvfrom(1024)
        data = data.decode('utf-8')
        print(data)
    except socket.timeout:
        print('REQUEST TIMED OUT')
    finally:
        print("===========================================================================================================")

