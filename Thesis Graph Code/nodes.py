class node:
    def __init__(self, id, name, demand):
        self.id = id
        self.name = name
        self.demand = demand
        
        
if __name__ == '__main__':
    n = int(input("how many nodes: "))
    L = []*n

    for i in range(n):
        s = input("enter id, name, demand ").split()
        id = int(s[0])
        name = s[1]
        demand = int(s[2])
        L.append(node(id, name, demand))
        
    for i in range(n):
        print(L[i].id, L[i].name, L[i].demand)
        print()
        
        
    
    