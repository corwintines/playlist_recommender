# A class for more securely handling our cluster data when it is outside of the data base. Less
# potential for indexing errors compared with using other storage objects.  Also provides
# checks for when a cluster is created that it also has all the required attributes populated and can 
# be entered in the DataBase.  Check value of Cluster.isValid() before any insert/analysis operations.

class Cluster:
	def __init__(self, cluster_dictionary=None):
		self.attributes = {
			"accousticness" : None,
			"cluster_id" : None,
			"energy" : None,
			"instrumentalness" : None,
			"loudness" : None,
			"speechiness" : None
			}

		if not cluster_dictionary is None:
			self.fromDict(cluster_dictionary)

	def fromDict(self, cluster_dictionary):
		for key, value in cluster_dictionary.iteritems():
			attributeName = key.lower().replace(" ","_")
			if attributeName == 'clusterid':
				attributeName = 'cluster_id'
			if attributeName in self.attributes.keys():
				self.attributes[attributeName] = value

	def isValid(self):
		requiredAttributes = [
			'cluster_id', 
			'accousticness', 
			'energy', 
			'instrumentalness', 
			'loudness', 
			'speechiness']
		for attributeName in requiredAttributes:
			if self.attributes[attributeName] is None:
				return False
		return True



