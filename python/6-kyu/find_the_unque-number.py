def find_uniq(arr):
    a,b = set(arr)
    return a if arr.count(a) == 1 else b

# def find_uniq(arr):
#     a = sorted(arr)
#     return a[0] if a[0] != a[1] else a[-1]

# def find_uniq(arr):
#     a = set(arr)
#     for e in a:
#         if arr.count(e) == 1:
#             return e