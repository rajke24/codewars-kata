def rgb(r, g, b):
    return ''.join(['{:02X}'.format(n) if 0 <= n <= 255 else ('00' if n < 0 else 'FF')  for n in (r,g,b)])

print(rgb(-3,1,1))