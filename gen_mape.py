def main():
	djeca = ['START'] # Pocetni korjen mape
	f = open('test_mapa.txt', 'w') 
	ctrl = 0 # Kontrolna varijabla

	while True: # Petlja se vrti dok se korjen 'START' ponovno ne pojavi
		# u listu djeca se dodaje svaki novi element tako da upiti idu po sirini
		for el in djeca:  
			# Kontrola ponavljanja
			if el == 'START': ctrl += 1
			if ctrl >= 2: break

			print 'Korjen = ', el # Zaglavlje
			slovo = raw_input('Slovo: ') # Unos zasebnog slova
			if slovo == '0': continue # Ako element nema djece treba se nula unijeti i bit ce preskocen
			unos = input('Broj djece: ')
			
			for i in range(1, int(unos)+1): # Broj djece od 1 do unesenog broja (bolje od 0 do unosa-1)
				djeca.append(str(slovo) + str(i)) # Dodavanje elementa u listu
				string = '%s\tima\t%s\t\n' % (el, str(slovo) + str(i)) # Format stringa koji ce se upisati u propozicijsku datoteku
				f.write(string)
			print djeca # Testni print liste
		break
	f.close()

if __name__ == '__main__':
	main()
