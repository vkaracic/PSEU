# -*- coding: utf-8 -*-
import networkx as nx
G = nx.DiGraph()
NasCjelina = nx.DiGraph()
NasTema = nx.DiGraph()
lista =[]

def nadji_subtree(node,G,razina,br):
    if node == []: return 0
    lista.append(node)
    susjedi = G.neighbors(node)
    br=br+1
    for susjed in susjedi:
        if susjed !=[] and susjed not in lista:
            if razina == 0:
                nadji_subtree(susjed,G,razina,br)
            elif razina > 0:
                if br < razina:
                     nadji_subtree(susjed,G,razina,br)



def import_file():

    f = open('Svi.txt', 'r')
    for line in f:
        koncept1, veza, koncept2, nl = line.split('\t')
        G.add_node(koncept1)
        G.add_node(koncept2)
        G.add_edge(koncept1, koncept2)
    roots=[n for n in G.nodes() if G.in_degree(n)==0]
    leafs=[n for n in G.nodes() if G.out_degree(n)==0]

    #for susjed in G.neighbors('e-ucenje'):
        #print("Susjedi == od", susjed, "====")
       # print(G.neighbors(susjed))

    #SG = G.subgraph('e-ucenje')


def main():
    import_file()
    nadji_subtree('e-ucenje',G,0,0)
    NasCjelina = G.subgraph(lista)
    lista.clear()
    nadji_subtree('e-ucenje',NasCjelina,3,0)
    NasTema=NasCjelina.subgraph(lista)
    print(len(NasTema.nodes()))

main()
