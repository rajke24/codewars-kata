def cond(chunk):   
    check = sum([int(dig) ** 3  for dig in chunk])
    if check % 2 == 0:
        return chunk[::-1]
    
    else:
        return chunk[1 : len(chunk)] + chunk[0:1]

def revrot(string, sz):
    if sz <= 0 or sz > len(string): return ''
    strg_size = len(string)
    chunks = [string[x : x + sz]  for x in range(0, strg_size, sz)
             if len(string[x:x + sz]) == sz
             ]
    
    spl_chunks = list(map(cond, chunks))
    revrot_num =  ''.join(spl_chunks)
    
    return revrot_num
    
def revrot2(s, n, res=""):
    if not s or n <= 0 or n > len(s):
        return ""
    
    while len(s) >= n:
        group = s[:n]
        if sum([int(d)**3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]
    
    return res