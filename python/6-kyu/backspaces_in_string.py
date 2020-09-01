def clean_string(s):
    stack = []
    for x in s:
        if stack and x == '#':
            stack.pop()
        elif x != '#':
            stack.append(x)
    return ''.join(stack)