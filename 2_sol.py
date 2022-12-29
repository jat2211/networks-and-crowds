# 2.py
import networkx as nx
import numpy as np
from collections import defaultdict
from networkx.algorithms.shortest_paths.generic import shortest_path_length

# generating the graph
def get_graph(file):
    G = nx.Graph()
    file = open(file, 'r')
    lines = file.readlines()
    for i in lines:
        edge = i.strip().split()
        G.add_edge(edge[0],edge[1])
    return G

def compute_transition_prob(G,p,q):
    """
    Compute transition probabilities for graph G.
    """
    d_graph = defaultdict(lambda:{})
    for source in G.nodes:
        for current_node in G.neighbors(source):
            # Calculate unnormalized probabilities
            d_graph[current_node][source] = []
            for destination in G.neighbors(current_node):
                # Calculate the transition probability for a neighbor
                path_len = shortest_path_length(G, source, destination)
                if path_len == 0:
                    transition_prob = 1/p
                elif path_len == 1:
                    transition_prob = 1
                elif path_len == 2:
                    transition_prob = 1/q
                d_graph[current_node][source].append(transition_prob)
            # Normalize the probability
            prob_sum = sum(d_graph[current_node][source])
            for i in range(len(d_graph[current_node][source])):
                d_graph[current_node][source][i] = d_graph[current_node][source][i] / prob_sum
    return d_graph
