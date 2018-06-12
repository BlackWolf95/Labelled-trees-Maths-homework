import networkx as nx
from random import randint
n=8
G1=nx.complete_graph(n)
G2=nx.Graph()
G2=G1

#G will be the output Graph
G=nx.Graph()
E=G.edges()

E2=G2.edges()
V2=G2.nodes()
len_V2=G2.number_of_nodes()
len_E2=G2.number_of_edges()
#V1 not needed, not available
#print(E2)
#print(V2)
#print(len_E2)
#print(len_V2)
#from 0 to n-1 we find the nodes
#and its corresponding vertices
x=0
#while (x<=n-1 and ):
while (len(G.nodes)!=n):
    #select a vertex randomly
    temp=randint(0,n-1)
    #print(temp)
    found=list(G2.edges(temp))
    #from 1the edges connected to the vertex
    #we randomly choose an edge
    temp2=randint(0,len(found)-1)
    rand_edge=found[temp2]
    #print(rand_edge)
    #get the start and ending nodes of the random edge obtained
    u=rand_edge[0]
    v=rand_edge[1]
    #now check if u is not equal to v that is no self loop
    #now add the nodes if it is not present
    if (G.has_node(u)==False):
        G.add_node(u)
    if (G.has_node(v)==False):
        G.add_node(v)
    # and see if there exists an ed
    if (u!=v) and (G.has_edge(u,v)==False):
        G.add_edge(u,v)
        #now check for cycles in G
        list1=list(nx.cycle_basis(G))
        #if length of list1 is 0, then there are no cycles
        if((len(list1)==0)and (nx.is_connected(G)==True)):
            x=x+1
            #print("Go ahead!")
        else:
            #x=0
            #reinitialize graph G
            #G=nx.Graph()
            G.remove_edge(u, v)
            G.remove_node(u)
            G.remove_node(v)
            E=G.edges()
            #print("RESTART!",len(list1),x)



#print(G.nodes())
#print(G.edges())
print("NUMBER OF NODES IN G")
print(len(G.nodes()))

print("NUMBER OF EDGES IN G")
print(len(G.edges()))
#print("DEGREES OF EACH NODE")
leaves=0;
avg=0
print("Degrees of each vertex:")
for i in range(0,n):
    deg=G.degree(i)
    print(deg)
    avg=avg+deg
    if deg==1:
        leaves=leaves+1

print("LEAVES")
print(leaves)
print("DIAMETER")
d=nx.diameter(G)
print(d)
print("TOTAL DEGREE")
print(avg)
print("AVERAGE DEGREE")
avg=float(avg/n)
print(deg)
