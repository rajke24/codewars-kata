def solution(s):
    return [s[i:i+2] if len(s[i:i+2]) == 2 else f"{s[-1]}_"  for i in range(0, len(s), 2)]  


# Other solution
# import re

# def solution(s):
#     return re.findall(".{2}", s + "_")