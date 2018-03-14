from mrjob.job import MRJob

class MRDian3(MRJob):
	
	def mapper(self, _, line):
		es, employee, salary, year = line.split(',')
		yield employee, es
	
	def reducer(self, employee, es):
		es_set = set(es)
		yield employee, len(es_set)

if __name__ == '__main__':
  MRDian3.run()		
