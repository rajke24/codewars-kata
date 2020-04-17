def list_squared(m, n):
    divisors_squared = [[j ** 2 for j in range(1, i + 1) if i % j == 0] for i in range(m, n + 1)]
    return [[int(i[-1] ** 0.5), sum(i)] for i in divisors_squared if sum(i) ** 0.5 % 1 == 0 ]