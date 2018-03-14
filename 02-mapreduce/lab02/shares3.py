from mrjob.job import MRJob
from mrjob.step import MRStep

class MRShares3(MRJob):
	
	def mapper(self, _, line):
		share, value, date = line.split(',')
		yield share
