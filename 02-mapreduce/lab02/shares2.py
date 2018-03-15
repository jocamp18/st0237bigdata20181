from mrjob.job import MRJob
from operator import itemgetter

class MRShares2(MRJob):
	
	def mapper(self, _, line):
		share, value, date = line.split(',')
		yield share, (value, date)

	def reducer(self, share, value_date):
		value_date_list = list(value_date)
		value_sort = sorted(value_date_list, key=itemgetter(0))
		date_sort = sorted(value_date_list, key=itemgetter(1))
		if value_sort == date_sort and value_sort[len(value_sort)-1][1] > value_sort[0][1]:
			yield share, "True"

if __name__ == '__main__':
  MRShares2.run()
