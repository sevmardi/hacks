import time
import random
import networkx as nx
from sklearn import linear_model
import random
import matplotlib.pyplot as plt


# Compute shortest path between source and all other nodes reachable from source.
G = nx.path_graph(5)
path=nx.single_source_shortest_path_length(G,0)
print(path[4])
