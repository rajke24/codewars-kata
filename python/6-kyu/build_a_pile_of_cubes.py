def find_nb(m):
    volume, count = 1, 1
    while volume < m:
        volume += count**3
        count += 1
    return count - 1 if volume == m else -1