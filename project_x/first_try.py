# -*- coding: utf-8 -*-
import networkx as nx

# inicijalizacija usmjerenog grafa
G = nx.DiGraph()
# inicijalizacija usmjerenog grafa nastavne cjeline
NasCjelina = nx.DiGraph()
# inicijalizacija usmjerenog grafa nastavne teme
NasTema = nx.DiGraph()
# prazna lista u koju se dodaju elementi podstabala
lista =[]


# rekurzivna funkcija za pronalazak podstabla, ulazni parametri: 
# korijen od kojega zelimo podstablo naci, citavi graf, razina  
# do koje zelimo traziti podstablo (za razinu 0 uzima citavo 
# podstablo), 
def nadji_subtree(node,G,razina,br):
	# base case, ako je dosao do kraja stabla vraca null
    if node == []: return 0

    # dodaj trenutni cvor u listu
    lista.append(node)
    # neighbors je metoda NetworkX-a gdje vraca djecu nekog cvora do razine 1
    # iste dodaje u varijablu susjedi iz koje redom rekurzivno za svakog trazi podliste
    susjedi = G.neighbors(node)
    # trenutna razina (inicijalno 0) 
    br=br+1


    for susjed in susjedi:
    	# uzima samo susjede koji postoje i nisu vec dodani u listi
        if susjed !=[] and susjed not in lista:

            if razina == 0:
                nadji_subtree(susjed,G,razina,br)
            elif razina > 0:
                if br < razina: # ako je trenutna razina manja od zeljene
                     nadji_subtree(susjed,G,razina,br)


# importiranje datoteke citavog grafa koja je obliku Cmap propozicija:
# koncept \t veza \t koncept\n
def import_file():

    f = open('Svi.txt', 'r')
    for line in f:
        koncept1, veza, koncept2, nl = line.split('\t')
        G.add_node(koncept1)
        G.add_node(koncept2)
        G.add_edge(koncept1, koncept2) # potrebno povezati dva konepta da bi se dobio usmjereni graf
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
    #print(NasCjelina.nodes())
    #lista.clear() # dobivam error na ovome, Ivane za sto je ovo bilo?
    nadji_subtree('e-ucenje',NasCjelina,3,0)
    NasTema=NasCjelina.subgraph(lista)
    print(len(NasTema.nodes()))

if __name__ == '__main__':
<<<<<<< HEAD
	main()
=======
	main()
>>>>>>> 68c855c94a8488ca5f74d34d31564f794e53176b
