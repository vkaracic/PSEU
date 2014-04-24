# -*- coding: utf-8 -*-
import networkx as nx

# importiranje datoteke citavog grafa koja je obliku Cmap propozicija:
# koncept \t veza \t koncept\n
def ucitaj_graf():
    rjecnik = {}
    G = nx.DiGraph() # Stvaranje strukture grafa
    f = open('test_mapa.txt', 'r')
    for line in f:
        koncept1, veza, koncept2 = line.split('\t')
        koncept2 = koncept2.strip('\n')
        G.add_node(koncept1)
        G.add_node(koncept2)
        G.add_edge(koncept1, koncept2) # potrebno povezati dva konepta da bi se dobio usmjereni graf
        rjecnik[koncept1, koncept2] = veza
    return G, rjecnik

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


# Trazi podstablo zadane dubine od zadanog korjena 
def nadji_jedno_podstablo(G, korjen, dubina):
    if dubina == 0: return # ako je dubina premasena prekida rekurziju
        
    susjedi = G.neighbors(korjen) # trazi susjede od zadanog korjena
    #print susjedi

    tmpGraf.add_nodes_from(susjedi) # dodaj susjede u globalni graf

    for item in susjedi:
        tmpGraf.add_edge(korjen, item) # napravi vezu izmedju trenutnog susjeda i njegovog korjena
        nadji_jedno_podstablo(G, item, dubina-1) # funkcija se ponavlja s tim da korjeni budu elementi iz prethodnih susjeda a dubina se smanjuje
    return tmpGraf


def nadji_sva_podstabla(G, korjen, dubina):
    listaJedinica = []
    pocetni_graf = nadji_jedno_podstablo(G, korjen, dubina) # trazi pocetni graf
    spremi_graf(pocetni_graf, korjen) # sprema pocetni graf u zasebnu datoteku

    listaGrafova.append(pocetni_graf)

    listovi = [n for n,d in pocetni_graf.out_degree().items() if d==0] # trazenje listova pocetnog grafa
    for el in listovi:
        graf = nadji_jedno_podstablo(G, el, dubina)
        listaJedinica.append(graf)
        nadji_sva_podstabla(G, el, dubina)
        # if provjera_dubine(graf, el, dubina):
        #     spremi_graf(graf, el) # spremanje grafa u svoju datoteku
        # else:

        tmpGraf.clear() # brisanje elemenata globalnog grafa zbog sljedece iteracije

    return listaJedinica
    

def provjera_dubine(G, korjen, dubina):
    pass



def main():
    global tmpGraf
    tmpGraf = nx.DiGraph()

    G, rjecnik_grafa = ucitaj_graf()
    korjen0 = nadji_korjen(G)[0] # u testnoj mapi se nalaze dva korjena pa zbog toga se na kraj dodaje [1] da se uzme korjen 'START' jer ima više elemenata
    korjen1 = nadji_korjen(G)[1]

    print G.edges()

    print rjecnik_grafa
    # subG1 = nadji_cPodstablo(G, korjen1)

    # tmpGraf.add_node(korjen1)

    # tmp = nadji_sva_podstabla(subG1, korjen1, 3)
    # print tmp
    # tmp2 = tmp[0]
    

if __name__ == '__main__':
    main()
