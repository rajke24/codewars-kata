from collections import Counter

def duplicate_count(text):
    return sum(1 for v in Counter(text.lower()).values() if v > 1)
    
#Other solution
# def duplicate_count(s):
#   return len([c for c in set(s.lower()) if s.lower().count(c)>1])