import codecs

def rot13(msg):
    rot13 = str.maketrans( 
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return msg.translate(rot13)

def rot13_2(msg):
    return codecs.encode(msg, 'rot13')