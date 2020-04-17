import math

def step(step, start, end):
    for i in range(start, end - step):
        print(isPrime(i))
        if isPrime(i) and isPrime(i + step):
            return [i, i + step]
    return None

def isPrime(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True