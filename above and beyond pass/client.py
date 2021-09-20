from socket import *
serverName=gethostname()
serverPort=11500
s=socket(AF_INET,SOCK_DGRAM)
running=True
while running:
    msg=input("What msg would u like to send? \nType Quit to Quit: ")

    s.sendto(msg.encode(),(serverName,serverPort))
    reply,serverAdr=s.recvfrom(2048)
    reply=reply.decode()
    print(reply)
    if msg.upper()=="QUIT":
        running=False
        s.close()
