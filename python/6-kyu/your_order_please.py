import re

def order(sentence):
    return " ".join(sorted(sentence.split(' '), key=lambda k: re.findall("\d+", k)))

def order2(sentence):
    return " ".join(sorted(sentence.split(' '), key=lambda k: sorted(k)))