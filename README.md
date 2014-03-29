PSEU
====

Generiranje nastavnog sadržaja iz mape koncepata

Predoloženi algoritam:

Algoritam:

odrediti nastavnu cjelinu:
- naći koncept koji nema roditelja
- uzeti njega s njegovim podstablom

odrediti nastavne teme:
- krenuti od korjena
- ići do Nt=3 dubine
- korjen sljedeće teme je list prošle teme

odrediti nastavne jedinice:
- krenuti od korjena
- ići do Nj=1 dubine

- ako je suma koncepata manja od 3 onda dodati još jednu dubinu za nastavnu jednicu; ako nema više dubina, ove koncepte dodati na prethodnu nastavnu jedinicu 
- korjen sljedeće jedinice je list prošle jedinice
