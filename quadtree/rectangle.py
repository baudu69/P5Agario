class Rectangle:
    def __init__(self,x=0,y=0,w=1,h=1):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def contains(self,point):
        return self.x < point.x < self.x + self.w  and self.y < point.y < self.y + self.h
