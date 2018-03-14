from mrjob.job import MRJob

class MRDian1(MRJob):
	def mapper(self,_,line):
		es, employee, salary, year = line.split(',')
		yield es, float(salary)

	def reducer(self, es, wages):
		wages_list = list(wages)
		yield es, sum(wages_list)/len(wages_list)

if __name__ == '__main__':
	MRDian1.run()
