def fagy(ho):
	return ho < 0
		 
heat = input('Hő: ')
while heat != 'vege':
    heat = int(heat)
    if fagy(heat):
        print("Fagy volt")
    else:
        print('Nem volt vagy')

    heat = input('Hő: ')

