def persistence(num):
    count = 0
    while num > 9:
        num = str(num)
        temp = 1
        for digit in num:
            temp *= int(digit)

        num = temp
        count += 1
        
    return count