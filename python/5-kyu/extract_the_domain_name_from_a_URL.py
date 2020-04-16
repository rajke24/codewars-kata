import re

def domain_name(url):
    pattern = r'(https?://)?(www\.)?(?P<name>[\w-]+).'
    return re.search(pattern, url).group('name')

