def digital_root(n):
    while n>10:
        n = sum([int(i) for i in str(n)])
    return n

def digital_root2(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def find_outlier(integers):
    e = [i % 2 for i in integers]
    return integers[e.index(0)] if integers.count(0) == 1 else integers[e.index(1)]