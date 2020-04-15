def doubles(maxk, maxn):
    return sum([sum([1 / ((n + 1) ** (2 * k)) for n in range(1, maxn + 1)]) / k for k in range(1, maxk + 1)])
print(doubles(1,10))

