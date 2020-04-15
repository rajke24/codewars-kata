f_cache ={}

def fibonacci(n):
    if n in f_cache:
        return f_cache[n]
    if n in [0, 1]:
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    f_cache[n] = result
    return result