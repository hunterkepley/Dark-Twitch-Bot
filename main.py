from Socket import openSocket
from Socket import sendMessage
from Parse import getUser, getMessage

def join(s):
    rb = b''
    connecting = True
    print("Starting bot...\n\nTo stop the bot, restart the terminal\n\n")
    while connecting:
        rb += s.recv(1024)
        temp = rb.split(b"\n")
        rb = temp.pop()

        for i in temp:
            print(i)
            connecting = doneJoining(i)
    sendMessage(s, b"Has joined the chat")
    

def doneJoining(l):
    if(b"End of /NAMES list" in l):
        return False
    return True

s = openSocket()
join(s)
rb = b''
canBet = False

while True:
    rb += s.recv(1024)
    temp = rb.split(b"\n")
    rb = temp.pop()

    for i in temp:
        print(i)
        if b"PING" in i:
            s.send(i.replace(b"PING", b"PONG"))
            break
        user = getUser(i).decode()
        message = getMessage(i).decode()
        print(message)
        # Check for ! [bot command indicator]
        if message[0] == '!':
            message = message[1:].lower()
            if message == "betstart\r":
                sendMessage(s, b"Betting has begun!")
                canBet = True
                break
            elif message == "betstop\r":
                sendMessage(s, b"Betting has stopped! Let the game begin and good luck!")
                canBet = False
                break