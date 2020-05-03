import re

months31 = '(01|03|05|07|08|10|12)'
months30 = '(04|06|09|11)'
month28 = '02'
days31 = '(0[1-9]|[1-2][0-9]|3[01])'
days30 = '(0[1-9]|[12][0-9]|30)'
days28 = '(0[1-9]|1[0-9]|2[0-8])'

valid_date = re.compile('\[(%s-%s|%s-%s|%s-%s)\]' % (months31, days31, months30, days30, month28, days28))