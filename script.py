import networkx as nx
import osmnx as ox 
G = nx.Graph()
G.clear()



G.add_edge(1, 2)
print(G.nodes())
print(G.number_of_nodes())