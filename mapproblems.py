class Edge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src+'-->'+self.dest
class Diagraph(object):
    #nodes is a list that includes all nodes
    #edges is a dic that can link all nodes to their subnodes
    def __init__(self):
        self.nodes=[]
        self.edges={}
    def addNode(self,node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node]=[]
    def addEdge(self,edge):
        src=edge.src
        dest=edge.dest
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('node not on graph')
        else:
            self.edges[src].append(dest)
    def subNodes(self,node):
        return self.edges[node]
    def hasNode(self,node):
        return node in self.nodes
    def __str__(self):
        result=''
        for src in self.nodes:
            for dest in self.edges[src]:
                result=result+src+'-->'+dest+'\n'
        return result[:-1]
class Graph(Diagraph):
    def addEdge(self,edge):
        Diagraph.addEdge(self,edge)
        rev=Edge(edge.dest,edge.src)
        Diagraph.addEdge(self,rev)
def printPath(path):
    '''path is a list of nodes'''
    result=''
    for i in range(len(path)):
        result=result+path[i]
        if i != len(path)-1 :
            result=result + '-->'
    return result
def DFS(graph,start,end,path,shortest,toPrint=False):
    '''assume that graph is a map without direction;
       start and end are nodes;
       path and shortest are lists of nodes;
       return the shortest path.  '''
    path=path+[start]
    
    if toPrint:
        print('current DFS path:',printPath(path))
    if start==end:
        return path
    for node in graph.subNodes(start):
        
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                
                newPath=DFS(graph,node,end,path,shortest,toPrint=True)
                if newPath != None:
                    
                    shortest = newPath
    return shortest
def BFS(graph,start,end,toPrint):
    '''graph is a map without direction;
       start and end are nodes;
       return the shortest path between two nodes.'''
    initPath=[start]
    pathQueue=[initPath]
    while len(pathQueue) != 0:
        tmpPath=pathQueue.pop(0)
        print('current BFS path:',printPath(tmpPath))
        lastNode=tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.subNodes(lastNode):
            if nextNode not in tmpPath:
                newPath=tmpPath+[nextNode]
                pathQueue.append(newPath)



nodes=[str(i) for i in range(6)]

diagraph=Diagraph()
for n in nodes:
    diagraph.addNode(n)
    
diagraph.addEdge(Edge(nodes[0],nodes[1]))
diagraph.addEdge(Edge(nodes[0],nodes[2]))
diagraph.addEdge(Edge(nodes[1],nodes[2]))
diagraph.addEdge(Edge(nodes[1],nodes[0]))
diagraph.addEdge(Edge(nodes[2],nodes[3]))
diagraph.addEdge(Edge(nodes[2],nodes[4]))
diagraph.addEdge(Edge(nodes[3],nodes[1]))
diagraph.addEdge(Edge(nodes[3],nodes[4]))
diagraph.addEdge(Edge(nodes[3],nodes[5]))
diagraph.addEdge(Edge(nodes[4],nodes[0]))
print(DFS(diagraph,'0','5',[],None,toPrint=True))


    
