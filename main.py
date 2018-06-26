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

while True:
    rb += s.recv(1024)
    temp = rb.split(b"\n")
    rb = temp.pop()

    for i in temp:
        print(i)
        if b"PING" in i:
            s.send(i.replace(b"PING", b"PONG"))
            break
        user = getUser(i)
        message = getMessage(i)
        """if b"test" in message:
            sendMessage(s, b"You said test, " + user + b"!")
            break""" # Message check template [incase forgetting happens]