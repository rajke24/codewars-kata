def expanded_form(num):
    digits = list(str(num))
    zeros = len(digits)
    new_num = ''
    for d in digits:
        if int(d) > 0:
            new_num += d.ljust(zeros, '0') + ' + '
        zeros -= 1 
        
    return new_num[:-3]

  

