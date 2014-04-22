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

# Pronalazi cijelo podstablo danog korjena
def nadji_cPodstablo(G, korjen):
    udG = G.to_undirected() # pretvaranje u undirected graf da bi se mogla koristiti funkcija shortest_path
                            # http://stackoverflow.com/questions/13914920/networkx-extract-the-smallest-connected-subgraph
    nodes = nx.shortest_path(udG, korjen).keys() # svi elemetni povezani s korjenom
    podstablo = G.subgraph(nodes) # stvaranje podgrafa od dobijenih elemenata
    DiStablo = podstablo.to_directed() # vracanje tog podstabla u strukturu usmjerenog grafa
    return DiStablo


# Funkcija za spremanje grafa u tekstualnu datoteku
def spremi_graf(G, naziv):
    datoteka = '%s.txt' % naziv
    f = open(datoteka, 'w') 
    for el in G.edges():
        it1, it2 = el
        string = "%s\tima\t%s\n" % (it1, it2)
        f.write(string)
    f.close


def main():
    G = import_graf()
    korjen0 = nadji_korjen(G)[0] # u testnoj mapi se nalaze dva korjena pa zbog toga se na kraj dodaje [1] da se uzme korjen 'START' jer ima više elemenata
    korjen1 = nadji_korjen(G)[1]

    STARTgraph = nadji_cPodstablo(G, korjen1)
    nazivDat = raw_input('Naziv datoteke: ')
    spremi_graf(STARTgraph, nazivDat)

    

    
    

if __name__ == '__main__':
    main()