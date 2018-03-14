from mrjob.job import MRJob

class MRShares1(MRJob):
	
	def mapper(self, _, line):
		share, value, date = line.split(',')
		yield share, (value, date)

	def reducer(self, share, date_value):
		date_value_list = list(date_value)
		print(date_value_list)
		yield share, (min(date_value_list)[1], max(date_value_list)[1])

if __name__ == '__main__':
  MRShares1.run()
