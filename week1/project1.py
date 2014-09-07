"""
This modules exposes 3 functions: make_complete_graph, compute_in_degrees, in_degree_distribution
"""

# Represents graph 1,2,3 as adjancency lists
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}


EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 
3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}


EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]), 5: set([2]), 
6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """ Given the number of nodes num_nodes 
        returns a dictionary corresponding to a complete directed graph 
        with the specified number of nodes.
    """
    try:
        num_nodes = int(float(num_nodes))
    except ValueError or TypeError:
        return {}

    if num_nodes < 0:
        return {}

    graph = {}
    nodes = [n for n in range(num_nodes)]
    for node in range(num_nodes):
        graph[node] = set()
        for edge in nodes:
            if edge != node:
                graph[node].add(edge)
    
    return graph


def compute_in_degrees(digraph):
    """ Takes a directed graph digraph (represented as a dictionary) and 
        computes the in-degrees for the nodes in the graph. 
        Returns a dictionary with the same set of keys (nodes) as digraph 
        whose corresponding values are the number of edges whose head matches a particular node. 
    """
    in_degrees = {}
    all_edges = digraph.values()
    nodes = digraph.keys()
    count = 0

    for node in nodes:
        for edges in all_edges:
            if node in edges:
                count += 1
        in_degrees[node] = count
        count = 0

    return in_degrees


def in_degree_distribution(digraph):
    """
        This function takes the directed graph that represented as a dictionary.
        And Returns the unnormalized distribution of the in-degrees of the graph.
    """
    digraph = compute_in_degrees(digraph)
    distribution = {}
    for count in digraph.values():
        if count not in distribution.keys():
            distribution[count] = 0
        distribution[count] += 1
    return distribution
