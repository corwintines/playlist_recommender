from sql_connector import *

with Song_DB() as dbase:
# Creates the necessary tables for DB DEMO, no need to run multiple times
	dbase.createTable_Song_No_Index()
	dbase.createTable_Song_Clustered_Index()
	dbase.createTable_Cluster()

# Add our calculated cluster centroids to the DB
	with open('centroids.txt', 'rb') as f:
		cluster_list = pickle.load(f)
		ClusterID = 0
		for cluster in cluster_list:
			cluster.insert(0,ClusterID)
			ClusterID += 1
		dbase.insert_Clusters(cluster_list)

# Load the song list to be inserted into the database
	song_list=[]
	with open('all_songs_cluster_combined.txt', 'rb') as f:
		song_list = pickle.load(f)
		for song in song_list:
			song[1] = song[1].replace("'","")
			song[2] = song[2].replace("'","")

# Since our list of Training Songs is only ~6700 songs, we construct lists of three
# different lengths by randomly selecting songs from our list of 6700 and appending
# them to a new list until it is the desired length for testing.  Having duplicate 
# songs is not an issue because they are assigned an AUTO_INCREMENTED primary key and
# our distribution of songs/cluster will remain similar. Also, songs are not in any
# particular order as they enter the DB and so their location in terms of querying
# is random (for the non-indexed table).

# Test 1: 10 000 Songs
	dbase.delete_ALL_SONGS_IN_DB() #Clear songs from database before each test
	songs_10000 = []
	for i in range(0,10000):
		songs_10000.append(random.choice(song_list))
	dbase.insert_Song_No_Index(songs_10000)
	dbase.insert_Song_Clustered_Index(songs_10000)
	dbase.select_Song_By_ClusterID('Song_Clustered_Index', 5) 
	dbase.select_Song_By_ClusterID('Song_No_Index', 5)
	dbase.select_Song_By_Other('Song_Clustered_Index') # Query a non-clustered attribute
	dbase.select_Song_By_Other('Song_No_Index')


# Test 2: 100 000 Songs
	dbase.delete_ALL_SONGS_IN_DB()
	songs_100000 = []
	for i in range(0,100000):
		songs_100000.append(random.choice(song_list))
	dbase.insert_Song_No_Index(songs_100000)
	dbase.insert_Song_Clustered_Index(songs_100000)
	dbase.select_Song_By_ClusterID('Song_Clustered_Index', 5) # Query by Clustered Index Attribute
	dbase.select_Song_By_ClusterID('Song_No_Index', 5)
	dbase.select_Song_By_Other('Song_Clustered_Index') # Query a non-clustered attribute
	dbase.select_Song_By_Other('Song_No_Index')

# Test 3: 1 000 000 Songs
	dbase.delete_ALL_SONGS_IN_DB()
	songs_1000000 = []
	for i in range(0,1000000):
		songs_1000000.append(random.choice(song_list))
	dbase.insert_Song_No_Index(songs_1000000)
	dbase.insert_Song_Clustered_Index(songs_1000000)
	dbase.select_Song_By_ClusterID('Song_Clustered_Index', 5) # Query by Clustered Index Attribute
	dbase.select_Song_By_ClusterID('Song_No_Index', 5)
	dbase.select_Song_By_Other('Song_Clustered_Index') # Query a non-clustered attribute
	dbase.select_Song_By_Other('Song_No_Index')





