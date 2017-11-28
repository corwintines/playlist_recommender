import sql_connector
from sql_connector import *



with Song_DB() as dbase:
# Creates the necessary tables for DEMO, no need to run multiple times
	dbase.create_Song_No_Index()
	dbase.create_Song_Clustered_Index()
	dbase.create_ClusterTable()

# Add our calculated cluster centroids to the DB
	# with open('centroids.txt', 'rb') as f:
	# 	cluster_list = pickle.load(f)
	# 	ClusterID = 0
	# 	for cluster in cluster_list:
	# 		cluster.insert(0,ClusterID)
	# 	dbase.insert_Clusters(cluster_list)

# Load the song list to be inserted into the database
	# song_list=[]
	# with open('all_songs_cluster_combined.txt', 'rb') as f:
	# 	song_list = pickle.load(f)
	# 	for song in song_list:
	# 		song[1] = song[1].replace("'","")
	# 		song[2] = song[2].replace("'","")

# Since our list of Training Songs is only ~6700, we insert it 100 times to make the DB tables
# have enough rows to demonstrate the performance differences bewteen tables with a Cluster
# Index and tables without a Cluster Index.  Each table will have ~670000 rows. There are 10
# unique clusters (10 clustered indexes)

	# songs_10000 = []
	# for i in range(0,10000):
	# 	songs_10000.append(random.choice(song_list))

	# dbase.insert_Song_No_Index(songs_10000)
	# dbase.insert_Song_Clustered_Index(song_list)

