class Location(object):
    def __init__(self,x,y):
        '''both x and y are intergers'''
        self.x=x
        self.y=y
    def move(self,deltax,deltay):
        '''both deltax and deltay are intergers'''
        return Location(self.x+deltax,self.y+deltay)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self,other):
        ox,oy = other.x,other.y 
        xDist,yDist = self.x-ox,self.y-oy
        return (xDist**2+yDist**2)**0.5
    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'
class Field(object):
    def __init__(self):
        self.drunks={}
    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate drunk")
        else:
            self.drunks[drunk]=loc
    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('drunk not in field')
