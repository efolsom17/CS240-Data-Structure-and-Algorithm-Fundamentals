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
        #    path = path + [target]
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