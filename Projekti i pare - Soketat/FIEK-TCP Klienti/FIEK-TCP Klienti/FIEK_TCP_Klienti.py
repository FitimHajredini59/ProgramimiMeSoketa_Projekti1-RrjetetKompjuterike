import socket
import sys 
import select

#serverName = 'localhost'
serverName = input("Shenoni emrin e serverit: ")

#serverPort = 12000
Port = input("Shenoni portin: ")
serverPort = int(Port)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName,serverPort))
while 1:
    print("=====================================================================================================")
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
              "\nPRIME " +
              "\nFUQIA " +
              "\n\nOse shenoni 0 ose zero ose ZERO per ta mbyllyr programin\n ")
    var = var.strip() 
    if len(var) > 128:
        print("Kerkesa nuk mund te jete me e gjate se 128 karaktere!!!")
        continue
    if not var:
        print("Ju lutem shenoni nje kerkese!")
        continue
    if (var == "0") or (var == "zero") or (var == "ZERO") or (var == "Zero") :
        s.close()
        break
    s.sendall(str.encode(var))
    data = s.recv(1024)
    data = data.decode('utf-8')
    print(data)

