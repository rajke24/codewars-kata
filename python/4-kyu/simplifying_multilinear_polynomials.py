import re

def simplify(poly):
    matches = re.findall(r'([+-]?)([0-9]*)([a-z]+)', poly)
    expand = [[int(x[0] + (x[1] if x[1] != '' else '1')), ''.join(sorted(x[2]))] for x in matches]
    variables = sorted(list(set(x[1] for x in expand)),key = lambda x: (len(x), x))
    coefficients = {v: sum(i[0] for i in expand if i[1] == v) for v in variables}
    return '+'.join([str(coefficients[v]) + v for v in variables if coefficients[v] != 0]).replace('+-', '-').replace('1', '')
