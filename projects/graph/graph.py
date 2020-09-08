"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError('notexistent vertex')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()

        # Add starting vertex ID
        q.enqueue(starting_vertex)

        # Create set for visiteed verts
        visited = set()

        # While queue is not empty 
        while q.size() > 0:

            # Dequeue a vert
            v = q.dequeue()

            # If not visited
            if v not in visited:
                # Visit it
                print(v)

                # Mark as visited
                visited.add(v)

                # Add  all neighbors to the queue
                for neighbors in self.get_neighbors(v):
                    q.enqueue(neighbors)

        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack
        s = Stack()

        # Add starting vertex ID
        s.push(starting_vertex)

        # Create set for visiteed verts
        visited = set()

        # While stack is not empty 
        while s.size() > 0:

            # Dequeue a vert
            v = s.pop()

            # If not visited
            if v not in visited:
                # Visit it
                print(v)

                # Mark as visited
                visited.add(v)

                # Add  all neighbors to the stack
                for neighbors in self.get_neighbors(v):
                    s.push(neighbors)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
    
        """
        # create an empty stack
    
        if visited is None:
            visited = set()
    
        visited.add(starting_vertex)
        print(starting_vertex)
        for neigh in self.get_neighbors(starting_vertex):
           
            if neigh not in visited:

                self.dft_recursive(neigh, visited)  
      
        # pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting_vertex_id
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH 
            path = q.dequeue()
            # Grab the last vertex from the PATH 
            v = path[-1]
            # if that vertex has not been visited...
            if v not in visited:
                # Check if it's the target
                if v == destination_vertex:
                    # If so return path
                    return path
                # Mark it as visited..
                visited.add(v) 
                # Then add a path to its neighbors to the back of the queue
                for neigh in self.get_neighbors(v):
                    # Copy the path
                    # path_copy = path[:]                
                    # Append the neighbors to the back
                    # path_copy.append(neigh)
                    # enque it
                    q.enqueue(path + [neigh])
                  
                    
   


        # pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # Create an empty queue and enqueue A PATH TO the starting_vertex_id
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first PATH 
            path = s.pop()
            # Grab the last vertex from the PATH 
            v = path[-1]
            # if that vertex has not been visited...
            if v not in visited:
                # Check if it's the target
                if v == destination_vertex:
                    # If so return path
                    return path
                # Mark it as visited..
                visited.add(v) 
                # Then add a path to its neighbors to the back of the queue
                for neigh in self.get_neighbors(v):
                    # Copy the path
                    path_copy = path[:]                
                    # Append the neighbors to the back
                    path_copy.append(neigh)
                    # enque it
                    s.push(path_copy)
                  
        # pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        

        # pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
