#!usr/bin/env python3

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages

            for links in graph:
                if page in graph[links]:
                    newrank += d* (ranks[links]/len(graph[links]))
            newranks[page] = newrank
        ranks = newranks
    return ranks
