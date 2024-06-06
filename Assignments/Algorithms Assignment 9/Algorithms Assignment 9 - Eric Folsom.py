### Algorithms Assignment 9 - Eric Folsom

## example graph for testing
test_graph = {
    'A': {'B': 2, 'C': 8, 'D': 4},
    'B': {'E': 3, 'H': 5},
    'C': {'E': 10, 'D': 9},
    'D': {'F': 1},
    'E': {'H': 5},
    'F': {'G': 7},
    'G': {'D': 1},
    'H': {'A': 12}
    }

'''
                    Dykstra's Algorithm
                    
Dijkstra's Algorithm is an algorithm that is used for finding the shortest path between nodes in a weighted graph.

The algorithm is as follows:

Pick some starting node, and let the distance of node N be the distace from the starting node to node N. We initially assign the distances to each node, aside from the starting node which
we set to 0, to be infinite. When we run the algorithm, the disance of nod N is the length of the shortest path known so far between the starting node and node N.

1. Mark every node as unvisited. For this we use a set of all unvisited nodes which we can call the unvisited set.
2. Assign each node a distance from the start value, for the starting node this is 0 and for all others this is inifity.
3. From the unvisited set, choose the node that has the smallest distance. If there are only nodes that have infinite distance, we go to step 6 and stop. If we only care about the distance to a certain node
we can stop here if the node that we choose is the target node. Otherwise we can keep trying to find the shortest path to all accessible nodes.
4. While we are at the current node, look at all neighboring nodes and then update their distance through the current node. Compare the new distance we just calculated to the one currently assigned to the neighbor, 
and assign it the smaller distance, so if the distance to a certain node is greater than the distance we just calculated, update it with the value we calculated. But if the value at that node was less than the value we 
just calculated, keep the original value.
5. Once we have finished calculating the distance for all the unvisited neighbors of the current node, mark the current node as visited, and remove it from the unvisited set. Then go back to step 3.
6. Once we have visited every node, each visited node will contain its shortest distance from the starting node. To find the path, start at the target node and pick the previous neighbor that has the shortest distance until we reach the starting node.


P-Code:

function dijkstra( graph, start, end):
    create a distance dictionary for all other nodes with distances set to infinity, starting distance set to 0
    create a dictionary to keep track of the parent nodes with all nodes set to None
    create a list of all nodes we need to visit
    
    While the list of node to visit is not empty
        pick the node with the smallest distance that has not been visited
            If the smallest distance is infinite, the remaining nodes are unreachable
        remove the current node from the list of nodes we want to visit
        If we have already visited the node,
            recreate the path to that node
        else, explore the neighbors of the current node
            Calculate the distance to the neighboring node
            If the calculated distance is less than the known distance to that node
                update the shortest distance to the neighbor
                update the previous node for the neighbor
                add the neighbor and its distance to the queue


I am mostly adapting the code from Grokking as well as fromm w3schools. I took a lot of inspiration for the P-code and algorithm explanation from the Wikipedia article.     

Resources:
Grokking
https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
'''

infinit = float('inf') #infinity

# function for calculating the node with the shortest distance, took this pretty much straight from grokking
def min_distance_node(distance, visited):
    min_dist = float('inf')
    min_dist_node = None
    for node in distance:
        dist = distance[node]
        if dist< min_dist and node not in visited:
            min_dist = dist
            min_dist_node = node
    return min_dist_node

def dijkstra(graph, start, target):
    # create a distance dictionary for all other nodes with distances set to infinity, starting distance set to 0
    distance = {node: infinit for node in graph}
    distance[start] = 0
    # create a dictionary to keep track of the parent nodes with all nodes set to None
    parents = {node: None for node in graph}
    # list of nodes that we have visited, might use this instead of keeping track of the nodes that we haven't visited yet.
    visited = []
    
    # select the current node as the lowest distance node that has not been visited yet
    current = min_distance_node(distance, visited)
    while current: # if all nodes have already been visited, finish the loop
        dist = distance[current] # get the distance to the current node
        neighbors = graph[current] # get the neighbors of the current node
        for n in neighbors.keys(): # Go through the neighbors of the current node
            new_dist = dist + neighbors[n] # calculate the new distance to that node
            if distance[n] > new_dist: # if it is shorter to get to the neighbor by going through this node
                distance[n] = new_dist # update the distance for this node
                parents[n] = current # the node becomes the new parent of the neighbor
            visited.append(current) # mmark the node as visited
        current = min_distance_node(distance, visited) # find the next node that we have process, and continue looping through
    
    
    ## Recreate the path and the distance to the target node
    path = [] # list to store the nodes that we visited along the path
    if distance[target] is not infinit: # if the target node is reachable from the starting node
        current = target # start from the end
        # backtrack to recreate the path
        while current: # while current is not none
            path.append(current) # add the current node that we are at to the path
            current = parents[current] # go to the current node's parent node, then continue looping until there is no more parent nodes 
        path.reverse() # reverse the order of the path so that we start at the starting node
    
    # returns a tuple with the path and the distance of the path
    return path, distance[target]  
                 

path, distance = dijkstra(test_graph,'A', 'G')
print(f"Path from 'A' to 'G': {path}\nDistance: {distance}")

'''
                    Prim's Algorithm
                    
Prim's algorithm is an algorithm for finding a Minimum Spanning Tree (MST) on a graph. A MST is the collection of all edges
required to connect all vertices in an undirected graph, with the minimum total edge weight. It is considered a "greedy" algorithm because it chooses
the locally optimal solution, which will in turn lead to a globally optimal solution.

Algorithm:

1. Choose a random node as the starting node, and include it as the first node in the MST
2. Commpare the edges from the MST. Choose the edge with the lowest weight that connects a node among the MST nodes to a node outside the MST
3. Add that edge and node to the MST.
4. Repeat steps 2 and 3 until all the nodes are in the MST. 

P-code:

def prims(graph):
    Create and empty list of nodes to keep track of the nodes that we have visited
    pick a random node
    Add the starting node to the list of visited nodes
    examine all neighboring nodes from the starting node
        Pick the node with the smallest distance fromm the starting node
    add the new node to 

Resources:
https://www.w3schools.com/dsa/dsa_algo_mst_prim.php
https://en.wikipedia.org/wiki/Prim%27s_algorithm
https://www.programiz.com/dsa/prim-algorithm
https://www.youtube.com/watch?v=cplfcGZmX7I
'''
# Graph for testing Prim's Algorithm on.
test_graph2 = {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }