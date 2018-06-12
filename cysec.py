import networkx as nx

G=nx.Graph()
G.add_cycle([0,1,2,3])
G.add_cycle([0,3,4,5])
print(nx.cycle_basis(G,0))
list1=list(nx.cycle_basis(G))
print(len(list1))
print(G.degree())
