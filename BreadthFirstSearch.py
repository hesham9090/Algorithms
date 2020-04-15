"""

Breadth First Search:

Input: Graph G = (V,E)
Output: Graph G vertices marked in the order they are first encountered by the BFS traversal

Check below image for graph we tried to build
https://github.com/hesham9090/Algorithms/tree/master/images/BFS.jpg

"""


graph = { "A":['B','C'] , "B":['D','E'], "C":['F','G'], "E":['H','I'],
         "H":['L','M','N'], "I":['O','P'], "G":['J','K'], "K":['Q'],
          "L":[], "M":[], "N":[], "O":[], "P":[], "Q":[], "D":[], "F":[], "J":[]

}

class BFS:
    def __init__(self):
        self.visited_order = []
        self.queue = []

    def breadth_first_search(self,graph,node):
        self.visited_order.append(node)
        self.queue.append(node)

        while self.queue:
            print("Current queue", self.queue)
            s = self.queue.pop(0)
            print("Removed from Queue ",s)

            for neighbor in graph[s]:
                if neighbor not in self.visited_order:
                    self.visited_order.append(neighbor)
                    self.queue.append(neighbor)
        return self.visited_order

testCase1 = BFS()
print(testCase1.breadth_first_search(graph,'A'))

testCase2 = BFS()
print(testCase2.breadth_first_search(graph,'D'))

testCase3 = BFS()
print(testCase3.breadth_first_search(graph,'G'))

"""
Time complexity analysis
O(|V | + |E|) where |V | and |E| are the number of the graph’s vertices and edges, respectively
"""