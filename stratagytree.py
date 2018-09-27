import random

class Item(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight


x=0
y=0
def maxVal(toConsider,avail):
    '''toConsider is a list of objects that has not been stolen
       avail is weight of stuff that the theaf can take
       thee function return a tuple which is the solution that contains the total value and subjects tuple
    '''
    global x
    x+=1
    if toConsider==[] or avail ==0:
        result = (0,())
    elif toConsider[0].getWeight() > avail:
        # explore the right branch
        result = maxVal(toConsider[1:],avail)
    else :
        nextItem = toConsider[0]
        # explore the left branch
        withVal, withToTake =maxVal(toConsider[1:],avail-nextItem.getWeight())
        withVal += nextItem.getValue()
        # explore the right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:],avail)
        # choose a better branch
        if withVal > withoutVal :
            result = (withVal,withToTake+(nextItem,))
        else :
            result = (withoutVal,withoutToTake)
    return result



def fastMaxVal(toConsider,avail,memo = {}):
    '''toConsider is a list of objects that has not been stolen
       avail is weight of stuff that the theaf can take
       thee function return a tuple which is the solution that contains the total value and subjects tuple
    '''
    global y
    y+=1
    if(len(toConsider),avail) in memo:
        result = memo[(len(toConsider),avail)]
    if toConsider==[] or avail ==0:
        result = (0,())
    elif toConsider[0].getWeight() > avail:
        # explore the right branch
        result = fastMaxVal(toConsider[1:],avail,memo)
    else :
        nextItem = toConsider[0]
        # explore the left branch
        withVal, withToTake =fastMaxVal(toConsider[1:],avail-nextItem.getWeight(),memo)
        withVal += nextItem.getValue()
        # explore the right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],avail,memo)
        # choose a better branch
        if withVal > withoutVal :
            result = (withVal,withToTake+(nextItem,))
        else :
            result = (withoutVal,withoutToTake)
    memo[(len(toConsider),avail)] = result
    return result



def smallTest():
    names=['a','b','c','d']
    vals=[6,7,8,9]
    weights=[3,3,2,5]
    items=[]
    for i in range(len(vals)):
        items.append(Item(names[i],vals[i],weights[i]))
    val,taken=maxVal(items,5)
    print(val)
    for i in taken:
        print(i.getName())



def buildManyItems(itemnum,maxValue,maxWeight):
    items=[]
    for i in range(itemnum):
        items.append(Item(str(i),
                          random.randint(1,maxValue),
                          random.randint(1,maxWeight)
                         )
                    )
    return items



def bigTest(itemnum):
    items=buildManyItems(itemnum,10,10)
    val1,taken1=maxVal(items,40)
    print(val1)
    for i in taken1:
        print(i.getName())
    val2,taken2=fastMaxVal(items,40)
    print(val2)
    for i in taken2:
        print(i.getName())

bigTest(20)
print("x=",x,"y=",y)
