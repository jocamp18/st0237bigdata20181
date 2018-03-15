from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMovies3(MRJob):

	def mapper(self, _, line):
		user, movie, rating, genre, date = line.split(',')
		yield date, 1

	def reducer1(self, date, movies):
		yield 1, (sum(movies), date)

	def reducer2(self, any, movies):
		yield any, min(movies)

	def steps(self):
		return[
			MRStep(mapper = self.mapper, reducer = self.reducer1),
			MRStep(reducer = self.reducer2)
		]

if __name__ == '__main__':
	MRMovies3.run()
