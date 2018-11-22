import webbrowser

class Movie():
	""" This class provides a way to store movie related information"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	
	# the content for each movie is provided in entertainment_center.py
	# the content in entertainment_center.py must be provided in this order:
	def __init__(self, movie_title, move_rating, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.rating = move_rating
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		