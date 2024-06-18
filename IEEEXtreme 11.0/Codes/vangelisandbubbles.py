class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
 
    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)
 
    def check_whether_visited(self, v, visited, parent):
        visited[v] = True
        
        for i in self.adj_list[v]:
            if not visited[i]:
                if self.check_whether_visited(i, visited, v):
                    return True
            elif parent != i:
                return True
            
        return False
 
    def check_cycle(self):
        visited = [False] * self.num_vertices
        
        for i in range(self.num_vertices):
            if not visited[i]:
                if self.check_whether_visited(i, visited, -1):
                    return True
                
        return False


for i in range(int(input())):
    n , m = map(int, input().split())
    edges = list(map(int, input().split()))
    
    graph = Graph(n)
    
    for i in range(0, len(edges), 2):
        graph.add_edge(edges[i], edges[i + 1])
        
    print(1 if graph.check_cycle() else 0)