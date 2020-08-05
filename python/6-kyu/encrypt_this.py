def encrypt_this(text):
    words = []
    for word in text.split():
        word = list(word)
        word[0] = str(ord(word[0]))
        
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        words.append(''.join(word))
    return ' '.join(words)