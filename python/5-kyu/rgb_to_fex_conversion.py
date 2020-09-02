def rgb(r, g, b):
    return ''.join([f'{n:02X}' if 0 <= n <= 255 else ('00' if n < 0 else 'FF')  for n in (r,g,b)])