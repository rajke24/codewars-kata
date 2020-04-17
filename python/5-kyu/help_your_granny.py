
def tour(friends, friend_towns, home_to_town_distances):
    distances = []
    friend_towns = [[friend,town] for friend, town in friend_towns if friend in friends] 
    for f in friend_towns:
        distances.append(f[1])

    dist_to_first_town = home_to_town_distances[distances[0]]
    dist_to_last_town =  home_to_town_distances[distances[len(distances) - 1]]
    dist =  dist_to_first_town + dist_to_last_town
    for i in range(len(distances) - 1):
        l = (home_to_town_distances[distances[i + 1]] ** 2 - home_to_town_distances[distances[i]] ** 2) ** 0.5
        dist += l

    return int(dist)

#Other solution
# def tour(friends, friend_towns, home_to_town_distances):
#     dist = 0
#     for i in friend_towns:
#         if i[0] in friends:
#             dist += (home_to_town_distances[i[1]] ** 2 - s ** 2) ** 0.5
#             s = home_to_town_distances[i[1]]
#     dist = dist + s
#     return int(dist)

