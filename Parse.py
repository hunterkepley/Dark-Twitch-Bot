
def getUser(l):
    return l.split(b":", 2)[1].split(b"!", 1)[0] # Gets username

def getMessage(l):
    return l.split(b":", 2)[2] # Gets message sent by user