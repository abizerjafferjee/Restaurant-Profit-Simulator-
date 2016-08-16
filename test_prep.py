class Tree:
    def __init__(self, value = None, children = None):
        self.value = value
        self.children = children.copy() if children else []
    def leaf_count(self):
        if len(self.children) == 0:
            return 1
        else:
            return sum([leaf_count(i) for i in self.children])
    def height(self):
        if len(self.children) == 0:
            return 1
        else:
            return 1 + max([height(i) for i in self.children])
    def arity(self):
        if len(self.children) == 0:
            return 0
        else:
            return max(len(self.children) + [arity(i) for i in self.children])
    def count(self):
        if len(self.children) == 0:
            return 1
        else:
            return 1 + sum([count(i) for i in self.children])




