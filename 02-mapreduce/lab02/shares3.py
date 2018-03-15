from mrjob.job import MRJob
from mrjob.step import MRStep

class MRShares3(MRJob):
	
	def mapper(self, _, line):
		share, value, date = line.split(',')
		yield share, (float(value), date)

	def reducer1(self, share, value_date):
		yield 1, min(value_date)[1]

	def reducer2(self, _, date):
		date = list(date)
		yield 1, max(date, key=date.count)

	def steps(self):
		return[
			MRStep(mapper = self.mapper, reducer = self.reducer1),
			MRStep(reducer = self.reducer2)
		]

if __name__ == '__main__':
	MRShares3.run()

