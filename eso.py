#Langó Luca, 2021.01.07. SZOFT I/1/E

print('Langó Luca, 2021.01.07, SZOFT I/1/E')
print('Ágazati 001 mintafeladat megoldása')


print('Csapadék mennyiség milliméterben')

elozo = input('Előző heti csapadék:')

aktualis = int(input('Aktális heti csapadék:'))

if 100 > elozo:
	print('Több csapadék')
elif elozo > aktualis:
	print('Kevesebb csapadék')
else:
	print('Nem változott')
