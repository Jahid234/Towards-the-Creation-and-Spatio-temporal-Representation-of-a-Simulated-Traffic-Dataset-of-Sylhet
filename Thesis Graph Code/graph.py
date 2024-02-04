class Graph:
    def __init__(self, V, E):
        self.V = set(V)
        # self.E = set(frozenset((u,v) for u,v in E))
        self.E = set(E)
        self.adj = {}
        for v in self.V:
            self.addVertex(v)
        for u,v in self.E:
            self.addEdge(u,v)
            
    def addVertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()
        self.V.add(v)
        
    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        self.adj[u].add(v)
        self.adj[v].add(u)
        self.E.add((u,v))
        
    def deg(self, v):
        return len(self.adj[v])
    
    def neighbors(self, v):
        return list(self.adj[v])
    
    @property
    def edges(self):
        return len(self.E)
    
    @property
    def vertices(self):
        return len(self.V)
    
    def removeEdge(self, u, v):
        e = (u,v)
        if e in self.E:
            self.E.remove(e)
            self.adj[u].remove(v)
            self.adj[v].remove(u)
            
    def removeVertex(self, u):
        for v in self.neighbors(u):
            self.removeEdge(u,v)
        del self.adj[u]
        self.V.remove(u)
    
if __name__ == '__main__':
    G = Graph({1,2,3,4}, {(1,2), (2,3), (1,4), (3,4)})
    G.addEdge(1,5)

    G.removeVertex(3)
    print(G.V)
    