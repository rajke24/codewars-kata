def race(v1, v2, g):
    if v1 > v2: return None
    seconds = g / ((v2 - v1)/3600)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds - h * 3600 - m * 60
    return [int(h), int(m), int(s)]