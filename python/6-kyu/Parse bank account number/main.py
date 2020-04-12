def build_dict(s, onlyVals=1):
    dict = {}
    for line in s.splitlines():
        start = 0
        for i in range(len(line) // 3):
            part = line[start : start + 3]
            start += 3
            dict[i] = dict.get(i, '') + part
    return {s:str(i) for i,s in dict.items()} if not onlyVals else dict.values()

digits = build_dict('''\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
''', 0)

def parse_bank_account(s):
    return int(''.join( digits[d] for d in build_dict(s) ))