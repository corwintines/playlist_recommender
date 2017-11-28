import mysql.connector
from mysql.connector import errorcode
import time
import base64
from sshtunnel import SSHTunnelForwarder
import cred

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
			self.cursor = self.connection.cursor()
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

	def insert_Clusters(self, cluster_list=[]):
		if not cluster_list:
			print "cluster_list is empty"
			return
		columns = (
			"INSERT INTO Cluster "
			"(ClusterID, "
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
		for cluster in cluster_list:
			values = (
				"VALUES ("
				"{0}, "
				"{1:.8f}, "
				"{2:.8f}, "
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
				"{13:.8f} "
				" ) ;".format(
				cluster[0],
				cluster[1],
				cluster[2],
				cluster[3],
				cluster[4],
				cluster[5],
				cluster[6],
				cluster[7],
				cluster[8],
				cluster[9],
				cluster[10],
				cluster[11],
				cluster[12],
				cluster[13])
				)
			query = columns + values
			if (self.executeQuery(query,'Error adding Cluster to DB')):	
				self.connection.commit()
				added_to_db += 1
		print "successfully added %d of %d clusters in cluster_list to DB"%(added_to_db,len(cluster_list))

	def insert_Songs(self, song_list=[]):
		if not song_list:
			print "song_list is empty"
			return
		columns = (
			"INSERT INTO Song "
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
			if (self.executeQuery(query,'Error adding Song to DB')):
				self.connection.commit()
				added_to_db += 1
		print "successfully added %d of %d songs in song_list to DB"%(added_to_db,len(song_list))

	def executeQuery(self, query, errorDescription=''):
		try:
			self.cursor.execute(query)
			return True
		except mysql.connector.Error as e:
			print errorDescription+": "+str(e)
			return False

	def create_ClusterTable(self):
		query = (
			"CREATE TABLE Cluster "
			"("
			"ClusterID int(11) NOT NULL, "
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
			"PRIMARY KEY (ClusterID) "
			") "
			"ENGINE=InnoDB DEFAULT CHARSET=utf8; "
			)
		if self.executeQuery(query,'Error creating Cluster table in DB'):
			print "Cluster table added."

	def create_SongTable(self):
		query = (
			"CREATE TABLE Song "
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
		if self.executeQuery(query,'Error creating Song table in DB'):
			print "Song table added."

	def delete_ALL_SONGS_IN_DB(self):
		query = "TRUNCATE Song;"
		if self.executeQuery(query,'Error deleting all songs from Song table in DB'):
			print "All songs in Song table deleted."

	def delete_ALL_CLUSTERS_IN_DB(self):
		query = "TRUNCATE Cluster;"
		if self.executeQuery(query,'Error deleting all clusters from Cluster table in DB'):
			print "All clusters in Cluster table deleted."


cluster_list = [
	(1,0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
	(2,0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
	(3,0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346)]

song_list = [
	(3,'test_song_title','test_artist',0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
	(3,'test_song_title','test_artist',0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346),
	(3,'test_song_title','test_artist',0.342345,0.5345,6345.346,0.34634,2643.346,2456.243464,0.23456234,0.2346,0.2346,0.2346,0.2346,0.2346,0.2346)]

with Song_DB() as dbase:
	dbase.create_SongTable()
	dbase.create_ClusterTable()

	dbase.insert_Songs(song_list)
	dbase.insert_Clusters(cluster_list)

	# dbase.delete_ALL_CLUSTERS_IN_DB()
	# dbase.delete_ALL_SONGS_IN_DB()




