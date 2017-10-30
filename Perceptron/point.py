import random
from utils import mapping
from utils import f
class Point(object):
    def __init__(self, _size, pos = None,):
        self.size = _size
        self.x = random.uniform(-1, 1) if pos is None else pos[0]
        self.y = random.uniform(-1, 1) if pos is None else pos[1]
        self.bias = 1
        self.label = 1 if self.y > f(self.x) else -1
    def __str__(self):
        return "{},{}".format(self.pixelX(),self.pixelY())
    def pixelX(self):
        return int(mapping(self.x,-1,1,0,self.size[0]))
    def pixelY(self):
        return int(mapping(self.y,-1,1,self.size[1],0))
    def pos(self):
        return (self.pixelX(), self.pixelY())

if __name__ == "__main__":
    p1 = Point((300,300))
    print(p1.pixelX(), p1.pixelY())