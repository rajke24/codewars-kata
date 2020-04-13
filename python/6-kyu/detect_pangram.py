import string
import re
from collections import Counter

def is_pangram(s):
    return len(Counter(re.sub('[^a-z]+', '', s.lower()))) == 26

#Other solution
# def is_pangram(s):
#     return set(string.ascii_lowercase) <= set(s.lower())

