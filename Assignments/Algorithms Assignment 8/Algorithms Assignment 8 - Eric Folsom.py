#### CS240 Algorithms Assignment 8 - Eric Folsom ####

'''
                                            Breadth First Search 

- Basically perform a search at each level. We Can think of a graph as having levels based on the linkeage from a specific starting node. 

Example:


Suppose we have the graph:

         A
       /   \
      B     C
     / \   / \ 
    D   E F   G
    
BFS traversal would return [A,B,C,D,E,F,G]. To do this it would do the following:

- Start at Node A
    Node A links to nodes B and C, add them to nodes that need to be checked
    Mark Node A as checked (in case other nodes point to node A)
- Go to node B
    Node B links to nodes D and E, add them to nodes that need to be checked
    Mark node B as checked
- Go to Node C
    Node C links to nodes F and G, add themm to nodes that need to be checked
    Mark node C as checked
- Go to Node D
    Node D does not link to any other nodes
    Mark node D as checked
- Go to Node E
    Node E does not link to any other nodes
    Mark node E as checked
- Go to Node F
    Node F does not link to any other nodes
    Mark node F as checked
- Go to Node G
    Node G does not link to any other nodes
    Mark Node G as checked
- There are no more nodes to check so we are done

To accomplish this we are using a queue to keep track of the nodes that we need to search. At the beginning we enqueue the starting node, node A, to begin our BFS. When we are at node A,
We add the nodes that A links to, B and C, to the queue. Since queues are a FIFO data structure we go to the next node that is in the queue and add the nodes that it links to
to the queue of nodes to be checked.

In pseudocode this looks something like the following:

1. Create a queue and enqueue the starting node
2. While the queue is not empty:
    a. Dequeue the node at the front of the queue.
    b. Visit the node (do something with the contents of the node)
    c. Enqueue all its unvisited neighbors
    
We can take care of the unvisited neighbors part by adding each node to a checked array or set so that we can see if the node we are going to check has already been checked and can skip it if it has been.
I am more familiar with using an array for that kind of thing, but apparently using a set() is more efficient in python. 

I saw that BFS is used with webcrawlers so I wanted to try and make something along those lines.
'''