# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node, end=" ")

        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')



#########################################################

class Graph:

	def __init__(self, edges, n):
		self.adjList = [[] for _ in range(n)]  # Initialize an empty adjacency list for each vertex

		# Add edges to the adjacency list
		for (src, dest) in edges:
			self.adjList[src].append(dest)
			self.adjList[dest].append(src)

def DFS(graph, v, discovered):
	discovered[v] = True  # Mark the current vertex as discovered
	print(v, end=' ')   	# Print the current vertex

	for u in graph.adjList[v]:  # Iterate through the neighbors of the current vertex
		if not discovered[u]:   # If a neighbor is not discovered yet
			DFS(graph, u, discovered)  # Recursively call DFS on the neighbor

if __name__ == '__main__':
	edges = [
		(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
		(3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
	]

	n = 13

	graph = Graph(edges, n)  # Create a graph object

	discovered = [False] * n  # Initialize a list to track discovered vertices

	for i in range(n):
		if not discovered[i]:  # If a vertex is not discovered yet
			DFS(graph, i, discovered)  # Call DFS starting from that vertex








# Algorithm
# Here is a step-by-step explanation of the DFS algorithm:
# 1.Choose a starting vertex and mark it as visited.
# 2.Visit the vertex and process it.
# 3.If there are unvisited neighboring vertices, choose one of them and repeat steps 1 and 2 recursively.
# 4.If all neighboring vertices have been visited or there are no neighbors, backtrack to the previous vertex and repeat step 3 if there are remaining unvisited vertices.
# 5.Repeat steps 1-4 until all vertices have been visited.