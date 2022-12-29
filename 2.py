# 2.py
import networkx as nx
import numpy as np
from collections import defaultdict 

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
            for destination in G.neighbors(current_node):
                # Calculate the transition probability for a neighbor


            # Normalize the probability

    return d_graph