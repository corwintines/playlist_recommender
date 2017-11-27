
class Song:
	def __init__(self,
		self.accousticness = None,
		self.artist_name = None,
		self.artist_familiarity = None,
		self.artist_hotness = None,
		self.clusterID = None,
		self.danceability = None,
		self.duration = None,
		self.end_of_fade_in = None,
		self.energy = None,
		self.instrumentalness = None,
		self.loudness = None,
		self.speechness = None,
		self.start_of_fade_out = None,
		self.tempo = None,
		self.title = None,
		self.valence = None):

	def validValues_ALL(self):
		if not isinstance(self.accousticness,float):
			return False
