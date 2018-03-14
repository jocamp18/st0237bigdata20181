from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMovies5(MRJob):
	
	def mapper(self, _, line):
		user, movie, genre, rating, date = line.split(',')
		yield date, int(rating)

	def reducer1(self, date, rating):
		rating_list = list(rating)
		yield 1, (sum(rating_list)/len(rating_list), date)

	def reducer2(self, any, rating):
		yield any, min(rating)

	def steps(self):
		return[
			MRStep(mapper = self.mapper, reducer = self.reducer1),
			MRStep(reducer = self.reducer2)
		]

if __name__ == '__main__':
	MRMovies5.run()
