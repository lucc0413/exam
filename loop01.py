import math

def base():
	
	numbers = []

	for i in range (0,3):
		number = int(input("Szám: "))
		numbers.append(number)
		
	result = calculate(numbers)
	print(result)
		
def calculate(numbers):
	sum = 0
	for number in (len(numbers)):
		sum+= mat.pow(numbers[num], 2)
	return sum
	
