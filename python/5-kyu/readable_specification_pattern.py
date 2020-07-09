class Meta(type):
    def __invert__(self):     return Meta("", (), {"__new__":lambda _, x: not self(x)})
    def __and__(self, other): return Meta("", (), {"__new__":lambda _, x: self(x) and other(x)})
    def __or__(self, other):  return Meta("", (), {"__new__":lambda _, x: self(x) or other(x)})

class Specification(metaclass=Meta):
    pass