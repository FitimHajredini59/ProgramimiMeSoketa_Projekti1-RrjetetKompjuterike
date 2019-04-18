import socket
import sys
from _thread import *
from datetime import datetime
import random
import math

host = 'localhost'
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serverSocket.bind((host, serverPort))
except socket.error as e:
    print(str(e))


print('Serveri u startua ne localhost:' + str(serverPort))
serverSocket.listen(10)
print('Serveri eshte i gatshem te pranoj kerkesa')



#funksioni FIBONNACI per llogaritjen e numrit te radhes se fibonnacit
def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))


#s - njesia qe do te konvertohet , n - vlera e njesise qe do te konvertohet!
def konvertimi(s,n): 
    if(s == "KilowattToHorsepower"):
        return n * 1.341
    elif(s == "HorsepowerToKilowatt"):
        return n / 1.341
    elif(s == "DegreesToRadian"):
        return n * (math.pi / 180)
    elif(s == "RadianToDegrees"):
        return n * (180 / math.pi)
    elif(s == "GallonsToLiters"):
        return n * 3.785
    elif(s == "LitersToGallons"):
        return n / 3.785
    else:
        return "Keni bere nje gabim gjate dhenies se informatave!!"


def is_prime(n):
    x = True
    for x in range(2, n):
        if n % x == 0:
            x = False
            return x
    return x
        


#funksioni per perpunimin e kerkeses qe dergohet nga klienti
def perpunimi_kerkeses(kerkesaVarg, conn, addr):
    if(kerkesaVarg[0] == 'IPADRESA'):
        conn.send(str.encode("IP adresa e klientit eshte:" + addr[0]))


    elif(kerkesaVarg[0] == 'NUMRIIPORTIT'):
       conn.send(str.encode("Klienti është duke përdorur portin " + str(addr[1])))


    elif(kerkesaVarg[0] == 'BASHKETINGELLORE'):
        try:
            s = ""
            s = s.join(kerkesaVarg[1:])                               #ruajme fjaline ne nje string s
            count = 0
            bashketingelloret = set("bcdfghjklmnpqrstvwxz\u00EB")
            for letter in s:                                          #iterojme neper cdo shkronje te stringut
                if letter in bashketingelloret:                       #nese shkronja ne iterim gjendet tek bashketingelloret rritet count
                    count += 1
            conn.send(str.encode("Teksti i pranuar përmbanë "+ str(count) +" bashketingellore"))
        except IndexError:
            conn.send(str.encode("Shenoni nje fjali pas kerkeses BASHKETINGELLORE!"))


    elif(kerkesaVarg[0] == 'PRINTIMI'):
        try:
            s = ""
            s = str.join(" " , kerkesaVarg[1:])
            conn.send(str.encode("Fjalia e dhene per tu printuar " + s))
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje fjali pas kerkeses PRINTIMI"))
            

    elif(kerkesaVarg[0] == 'EMRIIKOMPJUTERIT'):
        try:
            hostname = socket.gethostname()
            conn.send(str.encode("Emri i hostit është " + hostname))
        except error:
            conn.send(str.encode("Emri i hostit nuk dihet."))


    elif(kerkesaVarg[0] == 'KOHA'):
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S');    #Koha: year-month-date, hours-minutes-seconds
        conn.send(str.encode(time))


    elif(kerkesaVarg[0] == 'LOJA'):
        srand = ''
        for x in range(7):
            rand = random.randint(1, 49)   #random number
            randString = str(rand) + " "   #converted to strig
            srand += randString            #all random numbers in one string
        conn.send(str.encode(srand))


    elif(kerkesaVarg[0] == 'FIBONACCI'):
        try:
            n = fibonnaci(int(kerkesaVarg[1]))
            conn.send(str.encode(str(n)))
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas kerkeses FIBONACCI"))
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas kerkeses FIBONACCI"))


    elif(kerkesaVarg[0] == 'KONVERTIMI'):
        helpString1 = "Mundesite per konvertime:\nKilowattToHorsepower  \nHorsepowerToKilowatt  \nDegreesToRadians \nRadiansToDegrees"
        helpString2 = "\nGallonsToLiters \nLitersToGallons"
        try:
            s = kerkesaVarg[1]
            n = float(kerkesaVarg[2])
            conn.send(str.encode(str(konvertimi(s, n))))
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" + helpString1 + helpString2))
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" + helpString1 + helpString2))


    elif(kerkesaVarg[0] == 'FUQIA'):
        try:
            baza = int(kerkesaVarg[1])
            eksponenti = int(kerkesaVarg[2])
            rezultati = pow(baza, eksponenti)
            conn.send(str.encode(str(rezultati)))
        except IndexError:
            conn.send(str.encode("Shenoni bazen pastaj eksponentin pas kerkeses FUQIA"))


    elif(kerkesaVarg[0] == 'PRIME'):
        try:
            n = int(kerkesaVarg[1])
            if is_prime(n):
                conn.send(str.encode("Numri " + str(n) + " eshte numer i thjeshte!"))
            else:
                conn.send(str.encode("Numri " + str(n) + " nuk eshte numer i thjeshte!"))
        except IndexError:
            conn.send(str.encode("Shenoni nje numer pas kerkeses PRIME!"))
        except ValueError:
            conn.send(str.encode("Shenoni nje numer te plote pas kerkeses PRIME!"))

    else:
        conn.send(str.encode("Ju lutem shenoni njerat nga kerkesat!"))
    
def klient_thread(conn, addr):
    while 5 == 5:
        try:
            data = conn.recv(1024)
            kerkesa = data.decode('utf-8')
            kerkesaVarg = kerkesa.split()
            try:
                perpunimi_kerkeses(kerkesaVarg, conn, addr)
            except IndexError:
                conn.send(str.encode("Kerkesa nuk eshte valide!"))
        except OSError:
            conn.close()
    conn.close()


while True: 
    connectionSocket, addr = serverSocket.accept();
    print('Klienti u lidh ne serverin %s me port %s' % addr)
    start_new_thread(klient_thread, (connectionSocket, addr,))

