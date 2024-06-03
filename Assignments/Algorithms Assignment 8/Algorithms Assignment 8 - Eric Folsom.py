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

I saw that BFS is used with webcrawlers so I wanted to try and make something along those lines. I was trying to figure out an application for it and I decided on a wikipedia game bot thing. 
The wikipedia game is where you try and see how many clicks it takes to get between two wikipedia articles by only clicking on other wikipedia links in the article. 

I am going to try and implement this by treating each wikipedia article as a node, and then keeping track of the the other articles (nodes) that it links to. This will probably be slow because there are so many
links on each wikipedia article so maybe I limit it to 10 links per article?? 

I am going to base most of my implementation off of what I have read in Grokking and in other places.

Resources:

https://www.manning.com/books/grokking-algorithms
https://wikipedia.readthedocs.io/en/latest/code.html

'''

import wikipedia #  for accessing and searching wikipedia links, already noticed some funny business however with it
# the pages for  'baseball' and 'basketball' are swapped so I wonder if there are more instances like that. 

from collections import deque # using this instead of my own implementation just because I don't really trust my implementation of it (mostly because of my linked list)
# also because grokking uses it

## Simple version to start then gonna build upon to get wikipedia game thing going

def bfs_wiki_test(graph, start, target):
    search_queue = deque([(start, [start])]) # creating the queue. Created as a tuple, contains the starting node and the path (the array)
    
    checked = [start] # array for nodes that we have checked, putting the starting node in for now
    
    while search_queue: # While the queue of nodes to be searched is not empty
        
        check, path = search_queue.popleft() # get the value to check and the path that we took to get to it from the starting node
        
        if check == target: # if we have reached the value we are trying to get to
            return path # return the path we took from the starting node
        
        
        # for each of the other nodes that the node we are checking links to
        for link in graph[check]: 
            if link not in checked: # if the node that it links to has not been checked yet
                search_queue.append((link, path+[link])) # add the node that it links to to the queue and update the path that we have taken to get there
                checked.append(link) # add that link to the list of links that we have already checked
    return None # no path found
    
    
    
### testing

test_graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'H'],
    'C': ['E','D'],
    'D': ['F'],
    'E': ['H'],
    'F': ['G'],
    'G': ['D'],
    'H': ['A']
    }
    
bfs_wiki_test(test_graph, 'A', 'E')

### Example Graph from my explanation

ex_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

'''
From my initial example graph the path from A to F would be A -> C -> F
'''

bfs_wiki_test(ex_graph, 'A', 'F')

## Now to do the real thing with actual wikipedia, gonna need to play around with the library a bit but I think I Have a grasp on it a little. Links are in alphabetical order from each page it seems
# Each article/page is considered a node

def bfs_wikipediaGame(start, target):
    search_queue = deque([(start, [start])]) # create the same queue, with the starting page to search and the path that we take starting at the starting page
    checked = set()  # Set to keep track of checked articles, using a set this time because apparently it is faster than an array 
    checked.add(start) # and with how many links there are on a wikipedia page its probably a good idea to use this instead

    while search_queue: # while the queue to search is not empty
        article, path = search_queue.popleft() # same as the simple version, get the article string to search and the path that we took to get to it
        
        if article == target: # if we are at the page we want 
            return path # return the path we took to get to it
        
        links = wikipedia.page(article).links # creates a WikipediaPage object for the article that we are looking for and extracts the links as a list, similar to the above for link in graph[check]
        for link in links:
            if link not in checked:
                search_queue.append((link, path + [link]))
                checked.add(link)
