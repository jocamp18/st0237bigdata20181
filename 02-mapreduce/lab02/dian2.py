from mrjob.job import MRJob

class MRDian2(MRJob):
	
	def mapper(self, _, line):
		es, employee, salary, year = line.split(',');
		yield employee, float(salary)

	def reducer(self, employee, wages):
		wages_list = list(wages)
		yield employee, sum(wages_list)/len(wages_list)

if __name__ == '__main__':
	MRDian2.run()
