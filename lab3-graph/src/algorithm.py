#!/usr/bin/env python3

import sys
import logging

log = logging.getLogger(__name__)

from math import inf

def warshall(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Warshall's
    algorithm.

    Warshall's algorithm is similar to Floyd's, but gives the transitive closure
    instead of the minimum distances.

    Pre: adjlist is not empty.
    '''
    
    num_nodes = adjlist.node_cardinality()

    paths = [[False for _ in range(num_nodes)] for _ in range(num_nodes)]
    a_matrix = adjlist.adjacency_matrix()
    
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j or a_matrix[i][j]!=inf:
                paths[i][j] = True
            

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                paths[i][j] = paths[i][j] or (paths[i][k] and paths[k][j])


    return paths





def floyd(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Floyd's algorithm.

    Floyd's algorithm is similar to Warshall's, but gives the minimum distances
    instead of transitive closure.

    Pre: adjlist is not empty.
    '''

    num_nodes = adjlist.node_cardinality()
    a_matrix = adjlist.adjacency_matrix()

    paths = [[inf for _ in range(num_nodes)] for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                paths[i][j] = 0
            else:
                paths[i][j] = a_matrix[i][j]
                

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                through_k = paths[i][k] + paths[k][j]
                paths[i][j] = min(paths[i][j], through_k)

    return paths

def min(a, b):
    if a<b:
        return a
    else:
        return b

def dijkstra(adjlist, start_node):
    '''
    Returns the result of running Dijkstra's algorithm as two N-length lists:
    1) distance d: here, d[i] contains the minimal cost to go from the node
    named `start_node` to the i:th node in the adjacency list.
    2) edges e: here, e[i] contains the node name that the i:th node's shortest
    path originated from.

    If the index i refers to the start node, set the associated values to None.

    Pre: start_node is a member of adjlist.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 *
    b|* * 2
    c|* * *

    For start node "a", the expected output would then be:

    d: [ None, 1, 3]
    e: [ None, 'a', 'b' ]
    '''
    log.info("TODO: dijkstra()")
    d = []
    e = []
    return d, e

def prim(adjlist, start_node):
    '''
    Returns the result of running Prim's algorithm as two N-length lists:
    1) lowcost l: here, l[i] contains the weight of the cheapest edge to connect
    the i:th node to the minimal spanning tree that started at `start_node`.
    2) closest c: here, c[i] contains the node name that the i:th node's
    cheapest edge orignated from. 

    If the index i refers to the start node, set the associated values to None.

    Pre: adjlist is setup as an undirected graph and start_node is a member.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 3
    b|1 * 1
    c|3 1 *

    For start node "a", the expected output would then be:

    l: [ None, 1, 1]
    c: [ None, 'a', 'b' ]
    '''
    log.info("TODO: prim()")
    l = []
    c = []
    return l, c

if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
