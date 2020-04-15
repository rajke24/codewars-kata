def generate_hashtag(s):
    string = '#' + ''.join(s.title().split()) 
    return False if len(string) == 0 or len(string) > 140 else string