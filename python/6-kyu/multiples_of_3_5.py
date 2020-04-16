def solution(number):
    sum = 0
    cache = {}
    for i in range(3,number,3):
        sum +=i
        cache[i] = i
    for i in range(5,number,5):
        if i in cache:
            continue
        sum += i
    return sum

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)