__author__ = 'taras'

"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
import module_1
import project_1
import matplotlib.pyplot as plt
class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def make_dpa_graph(n, m):

    dpa_graph = module_1.make_complete_graph(m)
    dpa = DPATrial(m)

    for new_node in range(m, n):
        new_node_neighbors = dpa.run_trial(m)
        dpa_graph[new_node] = new_node_neighbors

    return dpa_graph


if __name__ == '__main__':

    graph = project_1.normalize_distribution(module_1.in_degree_distribution(make_dpa_graph(27770,12)))
    plt.loglog(graph.keys(), graph.values(), 'go')
    plt.xlabel('Nodes')
    plt.ylabel('Connectivity')
    plt.title('DPA graph in-degree distribution')
    plt.show()


