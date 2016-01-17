class Int_Node(object):
    """A simple node object that holds an integer"""
    def __init__(self, n):
        self.num = n
        self.kids = set() #no two nodes are alike
    def children(self):
        return self.kids
    def number(self):
        return self.num
    def add_child(self, node):
        self.kids.add(node)
    def __str__(self):
        return str(self.num)