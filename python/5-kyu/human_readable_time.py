# Definitely overcomplicated solution
def make_readable(sec):
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    seconds = sec - hours * 3600 - minutes * 60
    return f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}'

# Also quite nice solution
def make_readable2(s):
    hours = s / 3600
    minutes = s / 60 % 60
    seconds = s % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'

# Best solution
def make_readable3(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)