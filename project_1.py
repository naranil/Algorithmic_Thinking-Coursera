__author__ = 'taras'

"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""

import urllib2
import random
import itertools
from module_1 import in_degree_distribution
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy

dark2_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

# size of gifures in inches horisontal,vertical
rcParams['axes.color_cycle'] = dark2_colors
# linewidth in points
rcParams['lines.linewidth'] = 2
#displays grid
rcParams['axes.grid'] = True
rcParams['axes.facecolor'] = '#eeeeee'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'none'

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
                if random.random() < prob:
                    edges.add(edge)
        graph[node] = edges

    return graph

def normalize_distribution(distribution):

    factor = 1.0/sum(distribution.values())
    normalized_distribution = {key: val*factor for key, val in distribution.items()}

    return normalized_distribution

if __name__ == '__main__':

    graph1 = normalize_distribution(in_degree_distribution(compleate_directed_graph(300, 0.4)))
    graph2 = normalize_distribution(in_degree_distribution(compleate_directed_graph(300, 0.4)))
    graph3 = normalize_distribution(in_degree_distribution(compleate_directed_graph(300, 0.4)))

    plt.loglog(graph1.keys(), graph1.values(), 'go')
    plt.show()

    citation_graph = load_graph(CITATION_URL)
    out_degree = {k: len(v) for (k,v) in citation_graph.items()}

    print (numpy.mean(out_degree.values()))


# x = itertools.islice(normalized_distribution.items(), 0, 10)
# for key, val in x:
#     print key, val







