import mysql.connector
from mysql.connector import errorcode
import time
import base64
from sshtunnel import SSHTunnelForwarder
import cred
import pickle
import random
import decimal
import Song
import Playlist
'''
To access the database:

		-> 'cred.py' file needs to be in .../playlist_recommender/ folder and populated with 
			your ssh and mysql usernames and passwords

*** Important ***
		-> Wrap the Song_DB() object you create in a 'with as' statement like this:

				with Song_DB() as dbase:
					dbase.create_SongTable()
					dbase.insert_Songs(song_list)
					... all the database function calls ...

		If you don't wrap in the 'with Song_DB() as somename:' statement it leaves connections half
		open on my computer and acts buggy AF.

		-> You can execute other code/modules inside the with statement if you need run other stuff too
		-> BEFORE FINAL RUN make sure to run delete_ALL_SONGS_IN_DB() and delete_ALL_CLUSTERS_IN_DB()
			so we start with a clean DB and don't have bad rows in the DB (virtually no way to find them after)

		-Luke
'''

class Song_DB:
	def __init__(self):
		self.server = None
		self.connection = None
		self.cursor = None

	def __enter__(self):
		self.server = SSHTunnelForwarder(
			(base64.b64decode(cred.getAddr()), int(base64.b64decode(cred.getAddr_port()))), 
			ssh_password=base64.b64decode(cred.getPassword_SSH()), 
			ssh_username=base64.b64decode(cred.getUsername_SSH()), 
			remote_bind_address=(base64.b64decode(cred.getRemoteAddr()), int(base64.b64decode(cred.getRemoteAddr_port())))
			)
		try:
			self.server.start()
			print "open SSH: success"
		except:
			print "Error: SSH DB server connection unsuccessful."
		try:
			self.connection = mysql.connector.connect(
				host='127.0.0.1', 
				port=self.server.local_bind_port, 
				database='Song_DB', 
				user=base64.b64decode(cred.getUsername_MySQL()), 
				passwd=base64.b64decode(cred.getPassword_MySQL()))
			self.cursor = self.connection.cursor(buffered=True)
			print "open connection: success\nopen cursor: success"
			return self
		except mysql.connector.Error as e:
			print "Error making DB connection:", str(e)
		
	def __exit__(self, exc_type, exc_value, traceback):
		try:
			if not self.cursor is None:
				self.cursor.close()
				print "close cursor: success"
		except mysql.connector.Error as e:
			print str(e)
		try:
			if not self.connection is None:
				self.connection.close()
				print "close connection: success"
		except mysql.connector.Error as e:
			print str(e)
		try:
			if not self.server is None:
				self.server.stop()
				print "close SSH: success"
		except:
			print "Error in Song_DB: '__exit__()' -> SSH server connection not successfully closed"

	def CLEAR_ALL_SONGS_IN_DB(self):
		query = "TRUNCATE Song;"
		if self.executeQuery_Bool(query,'Error deleting all songs from Song table in DB'):
			print "All records in Song table deleted."

	def CLEAR_ALL_PLAYLIST_COMPARE(self):
		query = "TRUNCATE Playlist_Compare;"
		if self.executeQuery_Bool(query,'Error deleting all Playlist_Compare records in DB'):
			print "All records in Playlist_Compare table deleted."

	def closestCluster(self, playlist_aggregate_vector):
		query = "SELECT * FROM Cluster;"
		centroids = self.select_By_Query(query)
		print centroids

	def createTable_Cluster(self):
		query = (
			"CREATE TABLE Cluster "
			"("
			"ClusterID int(11) NOT NULL, "
			"Accousticness decimal(12,8) NOT NULL, "
			"Energy decimal(12,8) NOT NULL, "
			"Instrumentalness decimal(12,8) NOT NULL, "
			"Loudness decimal(12,8) NOT NULL, "
			"Speechiness decimal(12,8) NOT NULL, "
			"PRIMARY KEY (ClusterID) "
			") "
			"ENGINE=InnoDB DEFAULT CHARSET=utf8; "
			)
		if self.executeQuery_Bool(query,'Error creating Cluster table in DB'):
			print "Cluster table added."

	def createTable_Playlist_Compare(self):
		query = (
			"CREATE TABLE Playlist_Compare "
			"("
			"id int(11) NOT NULL AUTO_INCREMENT, "
			"playlist_type_1 varchar(255) NOT NULL, "
			"playlist_type_2 varchar(255) NOT NULL, "
			"accousticness decimal(12,8) NOT NULL, "
			"danceability decimal(12,8) NOT NULL, "
			"energy decimal(12,8) NOT NULL, "
			"instrumentalness decimal(12,8) NOT NULL, "
			"loudness decimal(12,8) NOT NULL, "
			"speechiness decimal(12,8) NOT NULL, "
			"tempo decimal(12,8) NOT NULL, "
			"valence decimal(12,8) NOT NULL, "
			"PRIMARY KEY (id) "
			") "
			"ENGINE=InnoDB DEFAULT CHARSET=utf8; "
			)
		if self.executeQuery_Bool(query,'Error creating Playlist_Compare table in DB'):
			print "Playlist_Compare table added."

	def createTable_Song(self):
		query = (
			"CREATE TABLE Song "
			"("
			"song_db_id int(11) NOT NULL AUTO_INCREMENT, "
			"cluster_id int(11) NOT NULL DEFAULT 9999, "
			"title varchar(255) NOT NULL DEFAULT 'no title', "
			"artist_name varchar(255) NOT NULL DEFAULT 'no artist', "
			"from_playlist varchar(255), "
			"accousticness decimal(12,8) NOT NULL, "
			"artist_familiarity decimal(12,8), "
			"artist_hotness decimal(12,8), "
			"danceability decimal(12,8) NOT NULL, "
			"duration decimal(12,8), "
			"end_of_fade_in decimal(12,8), "
			"energy decimal(12,8) NOT NULL, "
			"instrumentalness decimal(12,8) NOT NULL, "
			"loudness decimal(12,8) NOT NULL, "
			"rec_value decimal(12,8), "
			"speechiness decimal(12,8) NOT NULL, "
			"start_of_fade_out decimal(12,8), "
			"tempo decimal(12,8) NOT NULL, "
			"valence decimal(12,8) NOT NULL, "
			"PRIMARY KEY (song_db_id), "
			"KEY Song_ClusterID_INDEX (cluster_id)"
			") "
			"ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8; "
			)
		if self.executeQuery_Bool(query,'Error creating Song table in DB'):
			print "Song table added."

	def createTable_Training_Song(self):
		query = (
			"CREATE TABLE Training_Song "
			"("
			"song_db_id int(11) NOT NULL AUTO_INCREMENT, "
			"cluster_id int(11) NOT NULL DEFAULT 9999, "
			"title varchar(255) NOT NULL DEFAULT 'no title', "
			"artist_name varchar(255) NOT NULL DEFAULT 'no artist', "
			"from_playlist varchar(255), "
			"accousticness decimal(12,8) NOT NULL, "
			"artist_familiarity decimal(12,8), "
			"artist_hotness decimal(12,8), "
			"danceability decimal(12,8) NOT NULL, "
			"duration decimal(12,8), "
			"end_of_fade_in decimal(12,8), "
			"energy decimal(12,8) NOT NULL, "
			"instrumentalness decimal(12,8) NOT NULL, "
			"loudness decimal(12,8) NOT NULL, "
			"rec_value decimal(12,8) NOT NULL,"
			"speechiness decimal(12,8) NOT NULL, "
			"start_of_fade_out decimal(12,8), "
			"tempo decimal(12,8) NOT NULL, "
			"valence decimal(12,8) NOT NULL, "
			"PRIMARY KEY (song_db_id), "
			"KEY Training_Song_REC_VALUE_INDEX (rec_value)"
			") "
			"ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8; "
			)
		if self.executeQuery_Bool(query,'Error creating Song table in DB'):
			print "Training_Song table added."

	def executeQuery_Bool(self, query, errorDescription=''):
		try:
			self.cursor.execute(query)
			return True
		except mysql.connector.Error as e:
			print errorDescription+": "+str(e)
			return False

	def executeQuery_Return(self, query, errorDescription=''):
		result = []
		try:
			self.cursor.execute(query)
			for row in self.cursor:
				result.append(row)
			print "Select successful."
		except mysql.connector.Error as e:
			print errorDescription+": "+str(e)
		return result		

	def import_From_Playlist(self,playlist):
		songs = []
		for i in range(0,len(playlist.playlist_song_names)):
			song_attributes = {
				"accousticness" : playlist.playlist_accousticness[i],
				"artist_name" : playlist.playlist_song_artists[i],
				"cluster_id" : 9999, # cluster_id = 9999 indicates not clustered
				"danceability" : playlist.playlist_dancibility[i],
				"energy" : playlist.playlist_energy[i],
				"from_playlist" : playlist.playlist_playlistname,
				"instrumentalness" : playlist.playlist_instrumentalness[i],
				"loudness" : playlist.playlist_loudness[i],
				"speechiness" : playlist.playlist_speechness[i],
				"tempo" : playlist.playlist_tempo[i],
				"title" : playlist.playlist_song_names[i],
				"valence" : playlist.playlist_valence[i]
				}
			song = Song(song_attributes)
			songs.append(song)
		self.insert_Songs(songs)

	def insert_Clusters(self, cluster_list=[]):
		if not cluster_list:
			print "cluster_list is empty"
			return
		columns = (
			"INSERT INTO Cluster "
			"(ClusterID, "
			"Accousticness, "
			"Energy, "
			"Instrumentalness, "
			"Loudness, "
			"Speechiness)"
			)
		added_to_db = 0
		for cluster in cluster_list:
			values = (
				"VALUES ("
				"{0}, "
				"{1:.8f}, "
				"{2:.8f}, "
				"{3:.8f}, "
				"{4:.8f}, "
				"{5:.8f} "
				" ) ;".format(
				cluster[0],
				cluster[1],
				cluster[2],
				cluster[3],
				cluster[4],
				cluster[5])
				)
			query = columns + values
			if (self.executeQuery_Bool(query,'Error adding Cluster to DB')):	
				self.connection.commit()
				added_to_db += 1
		print "successfully added %d of %d clusters in cluster_list to DB"%(added_to_db,len(cluster_list))

	def insert_Playlist_Compare(self, playlist_compare_dict):
		columns = "INSERT INTO Playlist_Compare ("
		values = "VALUES ("
		for attr, val in playlist_compare_dict.iteritems():
			attribute = attr.lower().replace(" ","_")
			if val is None:
				columns = columns + attribute + ", "
				values = values + "NULL, "
			elif isinstance(val,float):
				columns = columns + attribute + ", "
				values = values + "{0:.8f}, ".format(val)						
			elif isinstance(val,str):
				columns = columns + attribute + ", "
				values = values + "'{0}', ".format(val)
			elif isinstance(val,int):
				columns = columns + attribute + ", "
				values = values + "{0}, ".format(val)
		columns = columns[:-2] + " ) "
		values = values[:-2] + " ) ;"
		query = columns + values
		if (self.executeQuery_Bool(query,'Error adding fitness delta vector to DB')):
			self.connection.commit()
			print "Added playlist delta vector (%s, %s)"%(playlist_compare_dict['playlist_type_1'],playlist_compare_dict['playlist_type_2'])

	def insert_Songs(self, song_list=[]):
		if not song_list:
			print "song_list is empty"
			return
		songs_added = 0
		for song in song_list:
			if not song.isValid():
				print "song does not have required attributes populated with valid data"
			else:
				columns = "INSERT INTO Song ("
				values = "VALUES ("
				for attribute, value in song.attributes.iteritems():
					if value is None:
						columns = columns + attribute + ", "
						values = values + "NULL, "
					elif isinstance(value,float):
						columns = columns + attribute + ", "
						values = values + "{0:.8f}, ".format(value)						
					elif isinstance(value,str):
						columns = columns + attribute + ", "
						values = values + "'{0}', ".format(value)
					elif isinstance(value,int):
						columns = columns + attribute + ", "
						values = values + "{0}, ".format(value)
				columns = columns[:-2] + " ) "
				values = values[:-2] + " ) ;"
				query = columns + values
				if (self.executeQuery_Bool(query,'Error adding song to DB')):
					self.connection.commit()
					songs_added += 1
		print "successfully added %d of %d songs in song_list to DB"%(songs_added,len(song_list))

		# columns = (
		# 	"INSERT INTO Song "
		# 	"(ClusterID, "
		# 	"Title, "
		# 	"Artist_Name, "
		# 	"Accousticness, "
		# 	"Artist_Familiarity, "
		# 	"Artist_Hotness, "
		# 	"Danceability, "
		# 	"Duration, "
		# 	"End_of_Fade_In, "
		# 	"Energy, "
		# 	"Instrumentalness, "
		# 	"Loudness, "
		# 	"Speechiness, "
		# 	"Start_of_Fade_Out, "
		# 	"Tempo, "
		# 	"Valence) "
		# 	)
		# added_to_db = 0
		# for song in song_list:	
		# 	values = (
		# 		"VALUES ("
		# 		"{0}, "
		# 		"'{1}', "
		# 		"'{2}', "
		# 		"{3:.8f}, "
		# 		"{4:.8f}, "
		# 		"{5:.8f}, "
		# 		"{6:.8f}, "
		# 		"{7:.8f}, "
		# 		"{8:.8f}, "
		# 		"{9:.8f}, "
		# 		"{10:.8f}, "
		# 		"{11:.8f}, "
		# 		"{12:.8f}, "
		# 		"{13:.8f}, "
		# 		"{14:.8f}, "
		# 		"{15:.8f} "
		# 		" ) ;".format(
		# 		song[0],
		# 		song[1],
		# 		song[2],
		# 		song[3],
		# 		song[4],
		# 		song[5],
		# 		song[6],
		# 		song[7],
		# 		song[8],
		# 		song[9],
		# 		song[10],
		# 		song[11],
		# 		song[12],
		# 		song[13],
		# 		song[14],
		# 		song[15])
		# 		)
		# 	query = columns + values
		# 	if (self.executeQuery_Bool(query,'Error adding song to DB')):
		# 		self.connection.commit()
		# 		added_to_db += 1
		# print "successfully added %d of %d songs in song_list to DB"%(added_to_db,len(song_list))		

	def insert_Training_Songs(self, song_list=[]):
			if not song_list:
				print "song_list is empty"
				return
			songs_added = 0
			for song in song_list:
				if not song.isValid():
					print "training song does not have required attributes populated with valid data"
				else:
					# print song.attributes['title']
					# print isinstance(song.attributes['title'],str)
					# print type(song.attributes['title'])
					columns = "INSERT INTO Training_Song ("
					values = "VALUES ("
					for attribute, value in song.attributes.iteritems():
						if value is None:
							columns = columns + attribute + ", "
							values = values + "NULL, "
						elif isinstance(value,float):
							columns = columns + attribute + ", "
							values = values + "{0:.8f}, ".format(value)						
						elif isinstance(value,str) or isinstance(value,unicode):
							value = value.replace("'","")
							value = value.encode(encoding="utf-8", errors="ignore")
							columns = columns + attribute + ", "
							values = values + "'{0}', ".format(value)
						elif isinstance(value,int):
							columns = columns + attribute + ", "
							values = values + "{0}, ".format(value)
					columns = columns[:-2] + " ) "
					values = values[:-2] + " ) ;"
					query = columns + values
					if (self.executeQuery_Bool(query,'Error adding song to DB')):
						self.connection.commit()
						songs_added += 1
			print "successfully added %d of %d training songs in song_list to DB"%(songs_added,len(song_list))

	def select_By_Query(self, query=""):
		return self.executeQuery_Return(query,'Error executing select_By_Query()')

	def select_Song_By_ClusterID(self, tableName, clusterID):
		query = "SELECT * FROM "+tableName+" WHERE ClusterID="+str(clusterID)+";"
		return self.executeQuery_Return(query,'Error executing select_Song_By_ClusterID()')




######### ********** FUNCTIONS FOR DATABASE DEMO ONLY ********** ######### 
	def createTable_Song_Clustered_Index(self):
		query = (
			"CREATE TABLE Song_Clustered_Index "
			"("
			"song_DB_ID int(11) NOT NULL AUTO_INCREMENT, "
			"ClusterID int(11) NOT NULL, "
			"Title varchar(255) NOT NULL, "
			"Artist_Name varchar(255) NOT NULL, "
			"Accousticness decimal(12,8) NOT NULL, "
			"Artist_Familiarity decimal(12,8) NOT NULL, "
			"Artist_Hotness decimal(12,8) NOT NULL, "
			"Danceability decimal(12,8) NOT NULL, "
			"Duration decimal(12,8) NOT NULL, "
			"End_of_Fade_In decimal(12,8) NOT NULL, "
			"Energy decimal(12,8) NOT NULL, "
			"Instrumentalness decimal(12,8) NOT NULL, "
			"Loudness decimal(12,8) NOT NULL, "
			"Speechiness decimal(12,8) NOT NULL, "
			"Start_of_Fade_Out decimal(12,8) NOT NULL, "
			"Tempo decimal(12,8) NOT NULL, "
			"Valence decimal(12,8) NOT NULL, "
			"PRIMARY KEY (song_DB_ID), "
			"KEY Songs_ClusterID_INDEX (ClusterID)"
			") "
			"ENGINE=InnoDB AUTO_INCREMENT=86137 DEFAULT CHARSET=utf8; "
			)
		if self.executeQuery_Bool(query,'Error creating Song table in DB'):
			print "Song table added."

	def createTable_Song_No_Index(self):
		query = (
			"CREATE TABLE Song_No_Index "
			"("
			"song_DB_ID int(11) NOT NULL AUTO_INCREMENT, "
			"ClusterID int(11) NOT NULL, "
			"Title varchar(255) NOT NULL, "
			"Artist_Name varchar(255) NOT NULL, "
			"Accousticness decimal(12,8) NOT NULL, "
			"Artist_Familiarity decimal(12,8) NOT NULL, "
			"Artist_Hotness decimal(12,8) NOT NULL, "
			"Danceability decimal(12,8) NOT NULL, "
			"Duration decimal(12,8) NOT NULL, "
			"End_of_Fade_In decimal(12,8) NOT NULL, "
			"Energy decimal(12,8) NOT NULL, "
			"Instrumentalness decimal(12,8) NOT NULL, "
			"Loudness decimal(12,8) NOT NULL, "
			"Speechiness decimal(12,8) NOT NULL, "
			"Start_of_Fade_Out decimal(12,8) NOT NULL, "
			"Tempo decimal(12,8) NOT NULL, "
			"Valence decimal(12,8) NOT NULL, "
			"PRIMARY KEY (song_DB_ID) "
			") "
			"ENGINE=InnoDB AUTO_INCREMENT=86137 DEFAULT CHARSET=utf8; "
			)
		if self.executeQuery_Bool(query,'Error creating Song table in DB'):
			print "Song table added."

	def delete_ALL_SONGS_IN_DB(self):
		query = "TRUNCATE Song;"
		if self.executeQuery_Bool(query,'Error deleting all songs from Song table in DB'):
			print "All songs in Song table deleted."
		query = "TRUNCATE Song_No_Index;"
		if self.executeQuery_Bool(query,'Error deleting all songs from Song table in DB'):
			print "All songs in Song table deleted."
		
		query = "TRUNCATE Song_Clustered_Index;"
		if self.executeQuery_Bool(query,'Error deleting all songs from Song table in DB'):
			print "All songs in Song table deleted."

	def delete_ALL_CLUSTERS_IN_DB(self):
		query = "TRUNCATE Cluster;"
		if self.executeQuery_Bool(query,'Error deleting all clusters from Cluster table in DB'):
			print "All clusters in Cluster table deleted."

	def insert_Song_Clustered_Index(self, song_list=[]):
		if not song_list:
			print "song_list is empty"
			return
		columns = (
			"INSERT INTO Song_Clustered_Index "
			"(ClusterID, "
			"Title, "
			"Artist_Name, "
			"Accousticness, "
			"Artist_Familiarity, "
			"Artist_Hotness, "
			"Danceability, "
			"Duration, "
			"End_of_Fade_In, "
			"Energy, "
			"Instrumentalness, "
			"Loudness, "
			"Speechiness, "
			"Start_of_Fade_Out, "
			"Tempo, "
			"Valence) "
			)
		added_to_db = 0
		for song in song_list:	
			values = (
				"VALUES ("
				"{0}, "
				"'{1}', "
				"'{2}', "
				"{3:.8f}, "
				"{4:.8f}, "
				"{5:.8f}, "
				"{6:.8f}, "
				"{7:.8f}, "
				"{8:.8f}, "
				"{9:.8f}, "
				"{10:.8f}, "
				"{11:.8f}, "
				"{12:.8f}, "
				"{13:.8f}, "
				"{14:.8f}, "
				"{15:.8f} "
				" ) ;".format(
				song[0],
				song[1],
				song[2],
				song[3],
				song[4],
				song[5],
				song[6],
				song[7],
				song[8],
				song[9],
				song[10],
				song[11],
				song[12],
				song[13],
				song[14],
				song[15])
				)
			query = columns + values
			if (self.executeQuery_Bool(query,'Error adding song to DB')):
				self.connection.commit()
				added_to_db += 1
		print "successfully added %d of %d songs in song_list to DB"%(added_to_db,len(song_list))

	def insert_Song_No_Index(self, song_list=[]):
		if not song_list:
			print "song_list is empty"
			return
		columns = (
			"INSERT INTO Song_No_Index "
			"(ClusterID, "
			"Title, "
			"Artist_Name, "
			"Accousticness, "
			"Artist_Familiarity, "
			"Artist_Hotness, "
			"Danceability, "
			"Duration, "
			"End_of_Fade_In, "
			"Energy, "
			"Instrumentalness, "
			"Loudness, "
			"Speechiness, "
			"Start_of_Fade_Out, "
			"Tempo, "
			"Valence) "
			)
		added_to_db = 0
		for song in song_list:	
			values = (
				"VALUES ("
				"{0}, "
				"'{1}', "
				"'{2}', "
				"{3:.8f}, "
				"{4:.8f}, "
				"{5:.8f}, "
				"{6:.8f}, "
				"{7:.8f}, "
				"{8:.8f}, "
				"{9:.8f}, "
				"{10:.8f}, "
				"{11:.8f}, "
				"{12:.8f}, "
				"{13:.8f}, "
				"{14:.8f}, "
				"{15:.8f} "
				" ) ;".format(
				song[0],
				song[1],
				song[2],
				song[3],
				song[4],
				song[5],
				song[6],
				song[7],
				song[8],
				song[9],
				song[10],
				song[11],
				song[12],
				song[13],
				song[14],
				song[15])
				)
			query = columns + values
			if (self.executeQuery_Bool(query,'Error adding song to DB')):
				self.connection.commit()
				added_to_db += 1
		print "successfully added %d of %d songs in song_list to DB"%(added_to_db,len(song_list))

	def select_Song_By_ClusterID(self, tableName, clusterID):
		query = "SELECT * FROM "+tableName+" WHERE ClusterID="+str(clusterID)+";"
		if self.executeQuery_Bool(query,'Error selecting songs by ClusterID'):
			print "Select successful."
	
	def select_Song_By_Other(self, tableName):
		query = "SELECT song_DB_ID, ClusterID, Title FROM "+tableName+" WHERE Valence > 0.8;"
		if self.executeQuery_Bool(query,'Error selecting songs by ClusterID'):
			print "Select successful."

# with Song_DB() as dbase:





	# dbase.CLEAR_ALL_SONGS_IN_DB()
	# dbase.CLEAR_ALL_PLAYLIST_COMPARE()
	# dbase.createTable_Song()
	# dbase.createTable_Training_Song()
	# dbase.createTable_Cluster()
	# dbase.createTable_Playlist_Compare()
	# dbase.insert_Songs(test_list)
	# dbase.createTable_Playlist_Compare()
	# dbase.insert_Playlist_Compare(playlist_compare_dictionary)
	# songs = dbase.select_By_Query("Select * from Song;")
	# for song in songs:
	# print song



## FOR TESTING ONLY ##
# song_dictionary = {
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
# 	"valence" : 0.4
# 	}

# playlist_compare_dictionary = {
# 	"playlist_type_1" : 'fitness',
# 	"playlist_type_2" : 'rock',
# 	"accousticness" : 0.4,
# 	"danceability" : 0.4,
# 	"energy" : 0.4,
# 	"instrumentalness" : 0.4,
# 	"loudness" : 0.4,
# 	"speechiness" : 0.4,
# 	"tempo" : 0.4,
# 	"valence" : 0.4
# 	}


# song_test = Song.Song(song_dictionary)
# test_list = []
# test_list.append(song_test)
# test_list.append(song_test)


# cluster_list = [
# 	(1,0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
# 	(2,0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
# 	(3,0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346)]

# song_list = [
# 	(3,'test_song_title','test_artist',0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
# 	(3,'test_song_title','test_artist',0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
# 	(3,'test_song_title','test_artist',0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346)]

# with Song_DB() as dbase:
	# dbase.createTable_Song_Clustered_Index()
	# dbase.createTable_Cluster()

	# dbase.insert_Song_Clustered_Index(song_list)
	# dbase.insert_Clusters(cluster_list)

	# dbase.delete_ALL_CLUSTERS_IN_DB()
	# dbase.delete_ALL_SONGS_IN_DB()
	
	# decimal.Decimal(random.randrange(10000))/100


	# with open('centroids.txt', 'rb') as f:
	# 	cluster_list = pickle.load(f)
	# 	dbase.insert_Clusters(cluster_list)

	# with open('all_songs_cluster_combined.txt', 'rb') as f:
	# 	song_list = pickle.load(f)
	# 	for song in song_list:
	# 		song[1] = song[1].replace("'","")
	# 		song[2] = song[2].replace("'","")
		
# insert Cluster backup
	# def createTable_Cluster(self):
	# 	query = (
	# 		"CREATE TABLE Cluster "
	# 		"("
	# 		"ClusterID int(11) NOT NULL, "
	# 		"Accousticness decimal(12,8) NOT NULL, "
	# 		# "Artist_Familiarity decimal(12,8) NOT NULL, "
	# 		# "Artist_Hotness decimal(12,8) NOT NULL, "
	# 		# "Danceability decimal(12,8) NOT NULL, "
	# 		# "Duration decimal(12,8) NOT NULL, "
	# 		# "End_of_Fade_In decimal(12,8) NOT NULL, "
	# 		"Energy decimal(12,8) NOT NULL, "
	# 		"Instrumentalness decimal(12,8) NOT NULL, "
	# 		"Loudness decimal(12,8) NOT NULL, "
	# 		"Speechiness decimal(12,8) NOT NULL, "
	# 		# "Start_of_Fade_Out decimal(12,8) NOT NULL, "
	# 		# "Tempo decimal(12,8) NOT NULL, "
	# 		# "Valence decimal(12,8) NOT NULL, "
	# 		"PRIMARY KEY (ClusterID) "
	# 		") "
	# 		"ENGINE=InnoDB DEFAULT CHARSET=utf8; "
	# 		)
	# 	if self.executeQuery_Bool(query,'Error creating Cluster table in DB'):
	# 		print "Cluster table added."

	# def insert_Clusters(self, cluster_list=[]):
	# 	if not cluster_list:
	# 		print "cluster_list is empty"
	# 		return
	# 	columns = (
	# 		"INSERT INTO Cluster "
	# 		"(ClusterID, "
	# 		"Accousticness, "
	# 		# "Artist_Familiarity, "
	# 		# "Artist_Hotness, "
	# 		# "Danceability, "
	# 		# "Duration, "
	# 		# "End_of_Fade_In, "
	# 		"Energy, "
	# 		"Instrumentalness, "
	# 		"Loudness, "
	# 		"Speechiness)"
	# 		# "Speechiness, "
	# 		# "Start_of_Fade_Out, "
	# 		# "Tempo, "
	# 		# "Valence) "
	# 		)
	# 	added_to_db = 0
	# 	for cluster in cluster_list:
	# 		values = (
	# 			"VALUES ("
	# 			"{0}, "
	# 			"{1:.8f}, "
	# 			"{2:.8f}, "
	# 			"{3:.8f}, "
	# 			"{4:.8f}, "
	# 			"{5:.8f} "
	# 			# "{6:.8f}, "
	# 			# "{7:.8f}, "
	# 			# "{8:.8f}, "
	# 			# "{9:.8f}, "
	# 			# "{10:.8f}, "
	# 			# "{11:.8f}, "
	# 			# "{12:.8f}, "
	# 			# "{13:.8f} "
	# 			" ) ;".format(
	# 			cluster[0],
	# 			cluster[1],
	# 			cluster[2],
	# 			cluster[3],
	# 			cluster[4],
	# 			cluster[5])
	# 			# cluster[6],
	# 			# cluster[7],
	# 			# cluster[8],
	# 			# cluster[9],
	# 			# cluster[10],
	# 			# cluster[11],
	# 			# cluster[12],
	# 			# cluster[13])
	# 			)
	# 		# values = (
	# 		# 	"VALUES ("
	# 		# 	"{0}, "
	# 		# 	"{1:.8f}, "
	# 		# 	"{2:.8f}, "
	# 		# 	"{3:.8f}, "
	# 		# 	"{4:.8f}, "
	# 		# 	"{5:.8f}, "
	# 		# 	"{6:.8f}, "
	# 		# 	"{7:.8f}, "
	# 		# 	"{8:.8f}, "
	# 		# 	"{9:.8f}, "
	# 		# 	"{10:.8f}, "
	# 		# 	"{11:.8f}, "
	# 		# 	"{12:.8f}, "
	# 		# 	"{13:.8f} "
	# 		# 	" ) ;".format(
	# 		# 	cluster[0],
	# 		# 	cluster[1],
	# 		# 	cluster[2],
	# 		# 	cluster[3],
	# 		# 	cluster[4],
	# 		# 	cluster[5],
	# 		# 	cluster[6],
	# 		# 	cluster[7],
	# 		# 	cluster[8],
	# 		# 	cluster[9],
	# 		# 	cluster[10],
	# 		# 	cluster[11],
	# 		# 	cluster[12],
	# 		# 	cluster[13])
	# 		# 	)
	# 		query = columns + values
	# 		if (self.executeQuery_Bool(query,'Error adding Cluster to DB')):	
	# 			self.connection.commit()
	# 			added_to_db += 1
	# 	print "successfully added %d of %d clusters in cluster_list to DB"%(added_to_db,len(cluster_list))













