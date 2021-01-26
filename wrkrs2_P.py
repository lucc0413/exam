import os
from wrkrs import Worker

class Workers:
	def __init__ (self):
		self.workerList = []
		self.read()
																														  
	def read(self):
		if (os.path.exists("dolgozok100.txt")):
			
			file = open("dolgozok100.txt", "r", encoding = "UTF-8")
			file.readline()
			row = file.readline()
		
		
			while(row):
				splitWorker = row.split(":")
				worker = Worker()
				worker.name = splitWorker[0]
				worker.city = splitWorker[1]
				worker.address = splitWorker[2]
				worker.salary = splitWorker[3]
				worker.bonus = splitWorker[4]
				worker.borndate = splitWorker[5]
				worker.enter = splitWorker[6]
				
				self.workerList.append(worker)
				
				row=file.readline()
			
			file.close()
			
	def printWorkerCount(self):
		print(f"Workers: {len(self.workerList)}")

workers = Workers()
workers.printWorkerCount()
