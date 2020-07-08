def song_decoder(song):
    return ' '.join(song.replace('WUB', ' ').split())

def song_decoder2(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()