# Graphs
# Network that helps define relationships between various components
# Node: Vertex
# Connection: Edge
# Graph: G(V,E) is a set of vertices V and edges E, where an edge is a connection between verticies
# Degree = Number of neighbors
# Path = Sequence of vertices
# Cycle = Path that starts and ends at the same vertex
# Connectivity : Concept applied 3 ways: To 2 specific nodes, to the graph, and to a subset
# Directed vs Undirected: Undirected means edges move both ways, while in undirected, it is only one-way
# Special kind = Tree. 3 properties: Connected and acyclic; Removing edge disconnects graph; adding edge creates a cycle

# Create graph class
class Graph():
    def __init__(self):
        # Graph is only going to hold the vertices, which will be a Python dictionary
        self.vertices = {}
        
# Function to add a new vertex to the graph
    def addVertex(self, value):
        if value not in self.vertices: # Check to see if the vertex is new
            self.vertices[value] = Vertex(value)
        return self.vertices[value] #

# Function to add new connection edge. It takes two vertices and one edge
    def addEdge(self, value1, value2):
        v1 = self.addVertex(value1)
        v2 = self.addVertex(value2)
        v1.addNeighbor(v2)
    
# Function to print the graph itself.
    def printGraph(self):
        for vertex in self.vertices.values():
            vertex.printVertex(set())
        
# Vertex class definition
class Vertex():
    def __init__(self, value, neighbors=None):
        self.value = value
        if neighbors == None: # It could be a brand new vertex
            self.neighbors = set()
        else: # Or tt could be connected to a series of vertices
            self.neighbors = set(neighbors)
    
    def addNeighbor(self, neighbor):
        # Bi-directional Edge
        if neighbor is not self and neighbor not in self.neighbors: # Avoid duplicates
            self.neighbors.add(neighbor)
            neighbor.neighbors.add(self)  # Ensure bidirectional edge
    
    def printVertex(self, marked = None):
        if marked == None:
            marked = set() # Marked variable to track if vertices have already been printed or checked
        if self.value in marked:
            return
        print(f'Vertex Value: {self.value}')
        marked.add(self.value) # Add vertex to marked so it won't be printed anymore
        for neighbor in self.neighbors:
            neighbor.printVertex(marked) # Call recursive function for all neighbors
        
if __name__ == "__main__":
    # Simple testing
    grafo = Graph()
    grafo.addVertex("A")
    grafo.addVertex("B")
    grafo.addVertex("C")
    grafo.addEdge("B", "C")
    grafo.addEdge("A", "C")
    grafo.printGraph()