from mrjob.job import MRJob

class MRMovies7(MRJob):
	
	def mapper(self, _, line):
		user, movie, rating, genre, date = line.split(',')
		yield genre, (rating, movie)

	def reducer(self, genre, movie_rating):
		yield genre,min(movie_rating)[1]

if __name__ == '__main__':
	MRMovies7.run()
