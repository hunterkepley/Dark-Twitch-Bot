import socket
from Config import HOST, PORT, PASS, USERNAME, CHANNEL

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(b"PASS " + PASS + b"\r\n") # Send OAUTH key
    s.send(b"NICK " + USERNAME + b"\r\n") # Send bot name
    s.send(b"JOIN #" + CHANNEL + b"\r\n") # Channel to join
    return s

def sendMessage(s, message):
    messageComplete = b"PRIVMSG #" + CHANNEL + b" :" + message
    s.send(messageComplete + b"\r\n")
    print("Sent: " + str(messageComplete))