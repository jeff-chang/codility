import random
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.depth = 0
        self.l = None
        self.r = None
   
class Tree(object):
    root = None
    depth = 0
 
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            newNode = Node(value)
            self._add(self.root, newNode)
   
    def _add(self, parentNode, newNode):
#        print parentNode.value, newNode.value
        if parentNode.value > newNode.value:
            self.depth = self.depth + 1
            if parentNode.l == None:
                 parentNode.l = newNode
#                 print "left"
#                 print parentNode.value, newNode.value
                 newNode.depth = self.depth
                 self.depth = 0
            else:
                 self._add(parentNode.l, newNode)
        else:
            self.depth = self.depth + 1
            if parentNode.r == None:
                 parentNode.r = newNode
#                 print "right"
#                 print parentNode.value, newNode.value
                 newNode.depth = self.depth
                 self.depth = 0
            else:
                 self._add(parentNode.r, newNode)

    def walk(self):
        if(self.root.value != None):
            self._walk(self.root)

    def _walk(self, node):
        if node.value != None:
            if node.l != None:
                self._walk(node.l)
            print str(node.value) + " " + str(node.depth)
            if node.r != None:
                self._walk(node.r)

    def path(self):
        self.path = []
        if(self.root.value != None):
           self._path(self.root)

    def _path(self, node):
        if node.value != None:
             self.path.append(node.value)
             if node.l == None and  node.r == None: #leaf
                 print self.path, self.diffDigits(self.path)
                 self.path.pop()
             else:
                 if node.l != None:
                     self._path(node.l)
                 if node.r != None:
                     self._path(node.r)
                 self.path.pop()
    
    def diffDigits(self, path):
        diffCount = 0
        for i in path:
            if diffCount < path.count(i):
                diffCount = path.count(i)
        return diffCount

def soultion(T):
    pass


Tree = Tree()
for i in range(50000):
    Tree.add(random.randint(0,50000))
# Tree.walk()
Tree.path()
