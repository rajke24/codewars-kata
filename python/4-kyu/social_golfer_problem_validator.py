def valid(days):
    met = {}
    day_length = len(days[0])
    group_length = len(days[0][0])
    golfers = [g for d in days[0] for g in d ]
    for day in days:
        if len(day) != day_length: return False
        for group in day:
            if len(group) != group_length: return False
            for player in group:
                if player not in golfers: return False
                if player not in met:
                    met[player] = set(group)
                else:
                    if len(met[player] & set(group)) > 1: return False
                    met[player].add(group)
    return True