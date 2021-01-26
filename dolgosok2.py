from dolgosok import Employee

class Manage:
	def __init__(self):
		
		self.employeeList= []
		self.read()
		self.miskolciak()
		
	def read(self):
		
		file = open("dolgozok100.txt", "r", encoding='UTF-8')
		
		row = file.readline()
		
		row=file.readline()
		
		while(row):
			
			rowSplit = row.split(":")
			emp = Employee()
			emp.name = rowSplit[0]
			emp.city = rowSplit[1]
			emp.address = rowSplit[2]
			emp.salary = rowSplit[3]
			emp.bonus = rowSplit[4]
			
			self.employeeList.append(emp)
			row = file.readline()
		
		file.close()
		print(self.employeeList)
			
def miskolciak(self):
	for employee in self.employeeList:			
counter = 0
		if(employee.city == "Miskolc")
			counter += 1
	print("Miskolciak:", counter)
	
def szegediek (self):
	for employee in self.employeeList:
sum = 0;
		if (employee.city == "Szeged"):
				sum += int(employee.salary)
	file = open ("szeged.txt", "w")
	file.write("Szegediek fizetése:" + str(sum))
	file.close()
		

Manage()
