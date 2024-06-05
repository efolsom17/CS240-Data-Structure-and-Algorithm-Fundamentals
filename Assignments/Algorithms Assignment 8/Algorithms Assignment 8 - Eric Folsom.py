#### CS240 Algorithms Assignment 8 - Eric Folsom ####

'''
                                            Breadth First Search 

- Basically perform a search at each level. We Can think of a graph as having levels based on the linkeage from a specific starting node. 

- Involves a graph. Graphs have nodes (vertices) and edges (links) which point to other nodes. Also uses a queue to keep track of the node that we are going to search.

1. Start at the root of the graph
2. Visit all the nodes at each level
    Dequeue a node from the front of the queue
    visit the the node and mark it as such
    Enqueue all its adjacent nodes that have not been visited to the back of the queue
3. repeat continue this process until the queue is empty or the node we want to find it found.

Example (More like BFT than BFS):


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
https://www.w3schools.com/dsa/dsa_algo_graphs_traversal.php
https://www.thewikipediagame.com/ - For testing 
https://wikipedia.readthedocs.io/en/latest/code.html - Documentation for the wikipedia module, fairly straightforward.
https://docs.python.org/3/tutorial/errors.html - Ran into errors while making my wikipedia game pathfinder. Relied on the documentation to help me with some extra assitance from chatGPT when I got stuck.
https://www.youtube.com/watch?v=HZ5YTanv5QE: Breadth-First Search in 4 minutes
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

## This doesn't really work (works in theory)/ Takes a really long time to work if it does, ran it for 10 min and didn't resolve

def bfs_wikipediaGame(start, target):
    search_queue = deque([(start, [start])]) # create the same queue, with the starting page to search and the path that we take starting at the starting page
    checked = set()  # Set to keep track of checked articles, using a set this time because apparently it is faster than an array 
    checked.add(start) # and with how many links there are on a wikipedia page its probably a good idea to use this instead

    while search_queue: # while the queue to search is not empty
        article, path = search_queue.popleft() # same as the simple version, get the article string to search and the path that we took to get to it
        
        if article == target: # if we are at the page we want 
            return path # return the path we took to get to it
        
        ## Exception handling here; I got to learn about the try statement and the except
        try: # trys to create links, if one of the errors are thrown do what is described
            links = wikipedia.page(article).links # creates a WikipediaPage object for the article that we are looking for and extracts the links as a list, similar to the above for link in graph[check]
        except wikipedia.DisambiguationError as e: # ran into this error the first time I tested this, a term links to multiple pages
            links = e.options # if a page is disambiguous, links to multiple pages, assign all those links as the links from that article to be searched
        except wikipedia.PageError: # error is raised if the page does not exist, found this after fixing disambiguation error
            continue # skip the page, doesn't exist

        ## This might resolve the large amount of links but I will just comment it out for now
        # Basically if the target article is in the links from a specific article
        # add the target article to the path and then return the path, should stop us from searching all the links to get to the one we want to go to
        #if target in links:
        #    path = path +[target]
        #    return path
        
        
        ### THIS IS WHAT CAUSES THIS TO BE SO SLOW, THERES JUST SO MANY LINKS TO CHECK
        for link in links: # for each link in the links from the given article
            if link not in checked: # if the link hasn't been checked yet
                search_queue.append((link, path + [link])) # add the article and its path to the queue to be checked
                checked.add(link) # note that we have checked that article


## Testing: 
# Search terms taken from https://www.thewikipediagame.com/
# bfs_wikipediaGame('Vietnamese Language', 'Shield')
# vtm = wikipedia.page('Vietnamese Language')
# vtm.links
# len(vtm.links) # 1113 links just from the 'Vietnamese Language' article on wikipedia, no wonder this thing is slow.
## Ran it for 30 min before it timed out, probably got rate limited


'''
                        Depth First Search
                        
- Basically explores as far as possible along each branch of a graph or tree and then backtracks to explore the other unvisited branches of the
tree or graph.

- Uses a graph or tree like BFS, and is usually recursive to perform the DFS.
- Examples are the BST traversal methods: pre-order, in-order, and post-order traversal. These are DFS traversal methods.

How it works:
    1. Start DFS traversal on a node
    2. Recursively call DFS traversal on each of the adjacent nodes if they haven't been visited yet


Resources:
https://www.w3schools.com/dsa/dsa_algo_graphs_traversal.php
https://www.w3schools.com/dsa/dsa_algo_graphs_cycledetection.php
https://www.programiz.com/dsa/graph-dfs
ChatGPT - For brainstorming and bouncing ideas off of. Was helpful for explaining code that I found on the internet as well as debugging my own code.
https://www.youtube.com/watch?v=Urx87-NMm6c: Depth-First Search in 4 Minutes
'''

## Starting Simple, Going to make a simple DFS traversal method and then adapt it to find a cycle and print the cycle in the graph.

def dfs_trav(graph, start, visited = None):
    # graph, is the graph that we want to perform dfs on
    # start is the node to start at
    # visited is an array of the nodes that we have already visited, default None
    if visited == None: # if we are just starting the dfs traversal, will run by default on the first time we call dfs_trav on a graph
        visited = [] # create the array to store the visited nodes
    
    visited.append(start) # add the starting node to the visited array
    
    for link in graph[start]: # for  each other node that the starting node links to
        if link not in visited: # check it we have visited that node
            dfs_trav(graph, link, visited) # recursive call to perform dfs on the neighboring nodes
    
    return visited # returns the nodes that we visit on our traversal. Should be in order of the nodes that we visit.



## testing my basic version

print(dfs_trav(test_graph, 'A')) ## From my drawing of this graph, kinda a weird looking thing, this works

'''
Now I want to change my DFS algorithm to determine if there is a cycle in the graph.
Going to also print the path of the cycle if It is found.
Will also need to keep track of the nodes that are in the current recursive stack

I want to do something similar to my wikipedia game bot, detect cycles in wikipedia articles, could be a way of seeing what articles are related to each other.
But given how my wikipedia game bot went, I don't think it would be a good idea to try and implement this at the current time.
'''

def dfs_cycles(graph, start, visited = None, recurs = None, path = None):
    # graph: graph we want to detect a cycle on
    # start: starting node
    # visited: list of nodes that have been visited
    # recurs: list of nodes that have been visited in the current recursive stack
    # path: path we have taken to get to a certain node based on the starting node
    
    # runs the first time we call this
    if visited == None:
        visited = []
    if recurs == None:
        recurs = []
    if path is None:
        path = []
        
    visited.append(start) # mark the starting node as visited
    recurs.append(start) # add the starting node to the nodes in the recursive stack 
    path.append(start) # add the starting node to the path
    
    for link in graph[start]: # for each neighboring node from the starting node
        if link not in visited: # check if we have visited the node
            if dfs_cycles(graph, link, visited, recurs, path): # recursive call, if this returns true, propogates true up the recursive stack, means that there is a cycle deeper in the graph
                return True # return true if there is a cycle
        elif link in recurs: # if the node linked to the starting node has already been visited in this recursive stack
            cycle_index = path.index(link) # get the index of the path list that contains the first node of the cycle
            cycle_path = path[cycle_index:] + [link] # creates the path of the cycle from the start of the cycle to the end of the cycle
            print(f"Cycle: {cycle_path}") # print the cycle
            return True # returns true if there is a cycle detected
    # if we have explored all the way to the end and there was no cycle detected
    recurs.remove(start) # remove the current node fromm the recursive stack
    path.pop() # remove the current node from the path ( will be the last node we added to the path)
    return False # No cycle detected, return False
        
### Test Graphs

test1_nocycle = {
    1: [2,3],
    2: [4,5],
    3: [6,7],
    4: [],
    5: [],
    6: [],
    7: []
}


'''
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

'''



test2_cycle = {
    1: [2,3],
    2: [4,5],
    3: [1,6,7],
    4: [7],
    5: [],
    6: [],
    7: [3]
}

'''
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
       |_________|
'''

print(dfs_cycles(test1_nocycle, 1))
print(dfs_cycles(test2_cycle, 1))