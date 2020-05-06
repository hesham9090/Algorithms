"""

Depth First Search:
It runs to explore nodes and edges of a graph
visits every vertex once and checks every edge in the graph once

Input: Graph G = (V,E)
Output: List of vertices marked in the order they are first encountered by the DFS traversal

Check below image for graph we tried to build
https://github.com/hesham9090/Algorithms/blob/master/images/DFS.PNG

"""


graph = { "A":['B','C'] , "B":['D','E'], "C":['F','G'], "E":['H','I'],
         "H":['L','M','N'], "I":['O','P'], "G":['J','K'], "K":['Q'],
          "L":[], "M":[], "N":[], "O":[], "P":[], "Q":[], "D":[], "F":[], "J":[]

}

class DFS:

    def __init__(self):
        print("Initializations started")
        self.visited = set()                  #Set to keep track of visited nodes
        self.traversal_order = []             #to keep track of order of visited nodes
        

    def depth_first_search(self, graph, node):
        if node not in self.visited:
            self.visited.add(node)
            self.traversal_order.append(node)
            for neighbor in graph[node]:
                self.depth_first_search(graph, neighbor)
        return self.traversal_order

testCase1 = DFS()
print(testCase1.depth_first_search(graph,'A'))

testCase2 = DFS()
print(testCase2.depth_first_search(graph,'D'))

testCase3 = DFS()
print(testCase3.depth_first_search(graph,'G'))

"""
Time complexity analysis
O(|V | + |E|) where |V | and |E| are the number of the graph’s vertices and edges, respectively
"""
