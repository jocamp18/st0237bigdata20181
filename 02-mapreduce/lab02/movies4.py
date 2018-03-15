from mrjob.job import MRJob

class MRMovies4(MRJob):

	def mapper(self, _, line):
		user, movie, rating, genre, date = line.split(',')
		yield movie, int(rating)

	def reducer(self, movie, rating):
		rating_list = list(rating)
		rating_len = len(rating_list)
		yield movie, (rating_len, sum(rating_list)/rating_len)

if __name__ == '__main__':
	MRMovies4.run()
