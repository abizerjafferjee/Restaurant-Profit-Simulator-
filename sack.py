class Sack:
    def __init__(self):
        self._content, self._key = {}, (1,1)

    def add(self, obj):
        self._key = (self._key[0], self._key[1] + 1)
        self._content[self._key] = obj

    def remove(self):
        return self._content.popitem()[1]

