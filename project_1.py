__author__ = 'taras'

"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""
import urllib2
import random
import itertools
import module_1
import matplotlib.pyplot as plt

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def compleate_directed_graph(num_nodes, prob):

    nodes = set(range(0,num_nodes))
    graph = {}
    # initialize random as current system time
    random.seed()
    for node in nodes:
        edges = set()
        for edge in nodes:
            if node != edge:
                if random.random() > prob:
                    edges.add(edge)
        graph[node] = edges


    return graph

if __name__ == '__main__':
    print (compleate_directed_graph(12, 0.8))

# citation_graph = load_graph(CITATION_URL)
#
# un_normalized_distribution = module_1.in_degree_distribution(citation_graph)
#
# normalized_distribution = {key : val/27770.  for key, val in un_normalized_distribution.items()}
#
#
# x = itertools.islice(normalized_distribution.items(), 0, 10)
# for key, val in x:
#     print key, val
#
#
# print (sum(normalized_distribution.values()))
#
# plt.loglog(normalized_distribution.keys(), normalized_distribution.values(), 'ro')
# plt.show()







