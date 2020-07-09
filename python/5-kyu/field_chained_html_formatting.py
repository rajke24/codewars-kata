class html:
    def __init__(self, tags=[]):
        self.tags = tags
    def __getattr__(self, tag):
        return html(self.tags + [tag])
    def __call__(self, *text):
        ret = ''.join(text)
        for tag in self.tags[::-1]:
            ret = f"<{tag}>{ret}</{tag}>"
        return ret
Format = html()