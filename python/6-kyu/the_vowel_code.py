vowels = {
    'a' : '1',
    'e' : '2',
    'i' : '3',
    'o' : '4',
    'u' : '5'
}

def encode(st):
    return ''.join([vowels[letter] if letter in vowels else letter for letter in st])
    
def decode(st):
    word = ''
    for char in st:
        if char in vowels.values():
            for vowel, number in vowels.items():
                if char == number:
                    word += vowel
        else: word += char
    return word

def encode2(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode2(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)