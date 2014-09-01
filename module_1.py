"""directd graph specific methods"""
EX_GRAPH0 = {0 : set([1, 2]),
             1 : set([]),
             2 : set([])}

EX_GRAPH1 = {0 : set([1, 5, 4]),
             1 : set([2, 6]),
             2 : set([3]),
             3 : set([0]),
             4 : set([1]),
             5 : set([2]),
             6 : set([])}

EX_GRAPH2 = {0 : set([1, 5, 4]),
             1 : set([2, 6]),
             2 : set([3, 7]),
             3 : set([7]),
             4 : set([1]),
             5 : set([2]),
             6 : set([]),
             7 : set([3]),
             8 : set([1, 2]),
             9 : set([0, 4, 5, 6, 7, 3])
             }

def make_complete_graph(num_nodes):
    """makes complete graph from given number of nodes
    so every possible edge is counted"""
    graph = {}
    if num_nodes <=1:        
        graph = {0 : set([])}
    else:
        for num in range(num_nodes):
            graph[num]=(set(range(num_nodes)).difference(set([num])))
    return graph

def compute_in_degrees(digraph):
    """computes in_degree for every node, as amount of 
    nodes directed to particular node. (considering every tail
    node for particular head node)"""
    in_degrees = {}
    for key in digraph.keys():
        in_degrees[key]=0
    for key in digraph.keys():
        for elemnt in digraph[key]:
            in_degrees[elemnt] += 1
    
    return in_degrees
             
def in_degree_distribution(digraph):
    """computes in_degree_distiribution
    as amount of pissible in_degrees
    in particular graph"""
    graph_in_degrees = set(compute_in_degrees(digraph).values())
    in_deg_dist = {}
    for val in graph_in_degrees:
        in_deg_dist[val] = 0
    
    for degree in in_deg_dist.keys():
        in_deg_dist[degree] = compute_in_degrees(digraph).values().count(degree)
        
    return in_deg_dist
