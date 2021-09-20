from socket import *

serverPort = 11500
s = socket(AF_INET, SOCK_DGRAM)
s.bind((gethostname(), serverPort))

print("Server Running")
running = True
while running:

    message, clAdr = s.recvfrom(2048)
    message = message.decode()
    message = message.upper()
    if message.upper()=="QUIT":
        returnMsg="GoodBye!!"

        s.sendto(returnMsg.encode(), clAdr)
    else:
        returnMsg = "Hello, What is your name? "

        s.sendto(returnMsg.encode(), clAdr)

        name, clAdr = s.recvfrom(2048)
        name = name.decode()

        wlcmMsg = "Hello " + name + " ,Welcome to SIT202!!"
        s.sendto(wlcmMsg.encode(), clAdr)

