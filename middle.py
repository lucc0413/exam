import math


def middle():
	for i in range(0,5):
		number = int(input("Szám: "))
		list = []
		list.append(number)
		
	result = calcMiddle(list)
	
	print("A mértani közepe {:>20.3f}".format(result))
		
def calcMiddle(list):
	
#.sqrt(szamok *)
	
	multiple = 1;
	for i in list:
		multiple *= i 
		result = pow(multiple, 1/ len(list))
	 
	 return result

middle()
