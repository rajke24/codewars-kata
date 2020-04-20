import itertools

def choose_best_sum(t, k, ls):
    best_sum = 0
    best_set = None
    combinations = itertools.combinations(ls, k)
    for combination in combinations:
        combi_sum = sum(combination)
        if combi_sum <= t and combi_sum > best_sum:
             best_set = combination
             best_sum = combi_sum
    return best_sum if best_sum != 0 else None

# Other solutions
from itertools import combinations

def choose_best_sum2(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)

import itertools
def choose_best_sum3(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None