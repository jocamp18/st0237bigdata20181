from mrjob.job import MRJob

class MRMovies1(MRJob):

	def mapper(self, _, line):
		user, movie, rating, genre, date = line.split(',')
		yield user, (movie, float(rating))

	def reducer(self, user, movies):
		movie_list = [tuple(val) for val in movies]
		movie_set = set(movie_list)
		_, rating = zip(*movie_set)
		yield user, (len(movie_set), sum(rating)/len(rating))

if __name__ == '__main__':
	MRMovies1.run()
