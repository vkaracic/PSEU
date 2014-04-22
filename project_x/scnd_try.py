# -*- coding: utf-8 -*-
import networkx as nx


# importiranje datoteke citavog grafa koja je obliku Cmap propozicija:
# koncept \t veza \t koncept\n
def import_graf():
    G = nx.DiGraph() # Stvaranje strukture grafa
    f = open('test_mapa.txt', 'r')
    for line in f:
        koncept1, veza, koncept2 = line.split('\t')
        koncept2 = koncept2.strip('\n')
        G.add_node(koncept1)
        G.add_node(koncept2)
        G.add_edge(koncept1, koncept2) # potrebno povezati dva konepta da bi se dobio usmjereni graf
    return G

# Pronalazi sve korjene u grafu
def nadji_korjen(G):
    korjen = [n for n, d in G.in_degree().items() if d==0]
    return korjen

def nadji_cPodstablo(G, korjen):
    udG = G.to_undirected()
    nodes = nx.shortest_path(udG, korjen).keys()
    return nodes


def main():
    G = import_graf()
    prviKorjen = nadji_korjen(G)[1]
    #print nadji_cPodstablo(G, prviKorjen)
    nodes = [d for d in G.nodes_iter()]
    print nodes

if __name__ == '__main__':
    main()