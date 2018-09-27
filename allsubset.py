def getBinaryRep(n,length):
    '''turn decimal n to a binary result with a specific length which is a string'''
    result = ''
    while n > 0 : 
        result = str(n%2)+result
        n = n // 2
    if len(result) > length : 
        raise ValueError('length is not enough')
    for i in range(length-len(result)):
        result= '0' + result
    return result
def genAllSubset(L):
    '''return a list which includes all subsets of set L'''
    allsubset=[]
    for i in range(0,2**len(L)):
        binstr = getBinaryRep(i,len(L))
        print(binstr)
        subset=[]
        for j in range(len(L)):
            if binstr[j] == '1':
                subset.append(L[j])
        allsubset.append(subset)
    return allsubset
'''appliance : find the best solution'''
'''there are 5 valuable things in a house, what should a thief steal who can only carry things no 
more than 20 kilograms'''
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
def getvalue(item):
    return item.value
def density(item):
    return item.value*1.0/item.weight
name = ['watch','painting','radio','vase','book','laptop']
value = [175,90,20,50,10,200]
weight = [10,9,4,2,1,20]
Items=[]
for i in range(0,len(value)):
    Items.append(Item(name[i],value[i],weight[i]))
allsubsets=genAllSubset(Items)

class Package(object):
    def __init__(self,subset):
        value=0
        weight=0
        names=[]
        for item in subset:
            value+=item.getValue()
            weight+=item.getWeight()
            names.append(item.getName())
        self.value = value
        self.names = names
        self.weight = weight
    def getName(self):
        return self.names
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
packages= []
for subset in allsubsets:
    packages.append(Package(subset))
lessthan20packages=[package for package in packages if package.weight <= 20 ]
sortedpackages=sorted(lessthan20packages,key=getvalue)
print(sortedpackages[-1].value)
            