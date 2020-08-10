def search(titles, term): 
    return list(filter(lambda title: term in title.lower(), titles))

def search2(titles, term): 
    return [ title for title in titles if term in title.lower() ]