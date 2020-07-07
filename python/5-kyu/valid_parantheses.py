def valid_parentheses(string):
    stack = []
    
    for s in string:
        if s == '(':
            stack.append(s)
        elif not stack:
            return False
        elif stack.pop() != ')':
            return False
    
    return not stack
