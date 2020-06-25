def sum_dig_pow(a, b):
    return [num for num in range(a, b + 1) if sum(int(digit) ** (i+1) for i, digit in enumerate(str(num))) == num]

print(sum_dig_pow(1,100))