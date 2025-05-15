# 
# Graphs | Python
# 



class Graph:
    def __init__(self):
        self.adj_list = {}


    #
    # Adds a new node to the graph
    #
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []


    #
    # Adds a new node to the edge of the graph
    #
    def add_edge(self, node1, node2):
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)

        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)


    #
    # Visualizer
    #
    def print_graph(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")



    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        result = []

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                result.append(current)
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs(self, start_node):
        visited = set()
        result = []

        def dfs_helper(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list[node]:
                    dfs_helper(neighbor)

        dfs_helper(start_node)
        return result

    def has_cycle(self):
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for node in self.adj_list:
            if node not in visited:
                if dfs(node, None):
                    return True
        return False


#
# Test scenarios
#
def test_graph():
    print("\nTesting Graph:")
    g = Graph()

    for node in ['A', 'B', 'C', 'D', 'E']:
        g.add_node(node)

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    g.print_graph()

    expected = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    assert g.adj_list == expected, "Graph adjacency list is incorrect."
    print("Graph structure test passed.")

    # Test BFS
    bfs_result = g.bfs('A')
    print("BFS from A:", bfs_result)

    # Test DFS
    dfs_result = g.dfs('A')
    print("DFS from A:", dfs_result)

    # Test Cycle Detection
    print("Graph has cycle:", g.has_cycle())

test_graph()