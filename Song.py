
class Song:
	def __init__(self, song_dictionary=None):
		self.attributes = {
			"accousticness" : None,
			"artist_name" : None,
			"artist_familiarity" : None,
			"artist_hotness" : None,
			"cluster_id" : None,
			"danceability" : None,
			"duration" : None,
			"end_of_fade_in" : None,
			"energy" : None,
			"instrumentalness" : None,
			"loudness" : None,
			"speechiness" : None,
			"start_of_fade_out" : None,
			"tempo" : None,
			"title" : None,
			"valence" : None}
		if not song_dictionary is None:
			self.fromDict(song_dictionary)
			self.hasData = self.validForDatabase()

	def fromDict(self, song_dictionary):
		for key, value in song_dictionary.iteritems():
			attributeName = key.lower().replace(" ","_")
			if attributeName == 'artist':
				attributeName = 'artist_name'
			if attributeName == 'clusterid':
				attributeName = 'cluster_id'
			if attributeName in self.attributes.keys():
				self.attributes[attributeName] = value

	def validForDatabase(self):
		requiredAttributes = [
			'title', 
			'artist_name',
			'cluster_id', 
			'accousticness', 
			'danceability', 
			'energy', 
			'instrumentalness', 
			'loudness', 
			'speechiness',
			'tempo',
			'valence']
		for attributeName in requiredAttributes:
			if self.attributes[attributeName] is None:
				return False
		return True



# attribute_dictionary = {
# 	"accousticness" : 0.4,
# 	"artist_name" : 'test_artist',
# 	"artist_familiarity" : None,
# 	"artist_hotness" : None,
# 	"cluster_id" : 4,
# 	"danceability" : 0.4,
# 	"duration" : None,
# 	"end_of_fade_in" : None,
# 	"energy" : 0.4,
# 	"instrumentalness" : 0.4,
# 	"loudness" : 0.4,
# 	"speechiness" : 0.4,
# 	"start_of_fade_out" : None,
# 	"tempo" : 0.4,
# 	"title" : 'test_title',
# 	"valence" : 0.4}


# song_test = Song(attribute_dictionary)
# print song_test.attributes
# print song_test.validForDatabase()
# print song_test.hasData
























