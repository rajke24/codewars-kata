def alphabet_position(text):
    return " ".join(str(ord(char) - 96) for char in text.lower() if char.isalpha())

print(alphabet_position('absdfsd'))