# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:48:27 2019
Problem Set 5

Problem 1: Periodic Points of a Word
Problem 2: Connected Components of Function
"""
from nose.tools import ok_

# =============================================================================
# Problem 1
# Given a word of length n, the program computes to find a set of periodic points
# which is defined by a point that is in the given word. Periodic points of the 
# associated function is found by using lp_orbits to find the cycles, and add 
# each of the cycle to a set which will be returned by the program.
# =============================================================================
def lp_apply(p, i):
    n = len(p)
    
    if 0 <= i and i < n:
        return p[i]
    
def lp_orbit(p, i):
    n = len(p)
    
    if 0 <= i and i <n:
        rv = [i]
        j = lp_apply(p, i)
        
        #if the rv length exceeds the list length, it indicates that there
        #is repeating elements
        while j != i and len(rv) <= n:
            if j in rv[1:]:
                return None
            rv.append(j)
            j = lp_apply(p, j)
            
        return rv


def lp_orbits(p):
    n = len(p)
    seen = set()
    orbits = []
    
    for i in range(n):
        if i not in seen:
            o = lp_orbit(p, i)
            if o != None:
                seen |= set(o)
                orbits.append(o)
    orbits.sort(key = len)
    
    return orbits

def periodic_points(f):
    periodic_set = set()
    cycle_f = lp_orbits(f)
    
    for cycle in cycle_f:
        #cycle is all the periodic points of f, thus take the union of all the
        #cycles computed by lp_orbits
        periodic_set |= set(cycle)
    
    return periodic_set
    
#Code Tests
ok_({0, 3, 4, 5} == periodic_points([5, 3, 4, 0, 3, 4]))
ok_({1, 2, 3, 4} == periodic_points([3, 2, 4, 1, 3]))
ok_({0, 1, 4} == periodic_points([1, 0, 1, 2, 4, 0]))
ok_({0, 1, 2, 3} == periodic_points([3, 0, 1, 2]))


# =============================================================================
# Problem 2
# Given with a list of points, the two points, i and j, are eventually colliding
# under the function. Two points will be connected by an edge between that 
# particular point and f(particular point). This program returns the total number
# of connected components based on the function using the module from networkx.
# =============================================================================

import networkx as nx 

def count_components(f):
    g = nx.Graph()
    g.add_nodes_from(range(len(f)))
    
    for node in range(len(f)):
        g.add_edge(node, f[node])
    num_connected_components = nx.number_connected_components(g)
    return num_connected_components


#Code Tests
ok_(3 == count_components([0, 2, 4, 5, 1, 3]))
ok_(2 == count_components([1, 2, 4, 3, 2]))
ok_(2 == count_components([6, 3, 2, 1, 0, 3, 2]))
ok_(1 == count_components([1, 2, 3, 1, 2]))
ok_(6 == count_components([1, 0, 1, 0, 4, 5, 6, 7, 8]))

