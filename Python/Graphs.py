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


# 
# Test scenarios
# 
# def test_graph():
#     print("\nTesting Graph:")
#     g = Graph()

#     for node in ['A', 'B', 'C', 'D', 'E']:
#         g.add_node(node)

#     g.add_edge('A', 'B')
#     g.add_edge('A', 'C')
#     g.add_edge('B', 'D')
#     g.add_edge('C', 'D')
#     g.add_edge('D', 'E')

#     g.print_graph()

#     expected = {
#         'A': ['B', 'C'],
#         'B': ['A', 'D'],
#         'C': ['A', 'D'],
#         'D': ['B', 'C', 'E'],
#         'E': ['D']
#     }
#     assert g.adj_list == expected, "Graph adjacency list is incorrect."
#     print("Graph test passed successfully.")
# test_graph()