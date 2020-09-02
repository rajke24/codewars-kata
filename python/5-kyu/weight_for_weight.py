def order_weight(string):
    weights = string.split()
    weights = sorted(sorted(weights), key=lambda k:(sum(int(x) for x in k)))
    return ' '.join(weights)