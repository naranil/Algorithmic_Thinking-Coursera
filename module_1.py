# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

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

print EX_GRAPH0


def make_complete_graph(num_nodes):
    graph = {}
    if num_nodes <=1:        
        graph = {0 : set([])}
    else:
        for i in range(num_nodes):
            graph[i]=(set(range(num_nodes)).difference(set([i])))
    return graph

# should be finished
def compute_in_degrees(digraph):
    in_degrees = {}
    for i in digraph.keys():
        if not digraph[i]:
            print digraph[i]
             
        
compute_in_degrees(EX_GRAPH0)







