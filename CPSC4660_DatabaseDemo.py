from db_demo_sql_connector import *

dir_path = os.path.dirname(os.path.realpath(__file__))
all_songs_path = os.path.join(dir_path,"training_data/pickle/clustered_songs/all_songs_clustered.txt")
# all_centroids_path = os.path.join(dir_path,"training_data/pickle/clustered_songs/centroids.txt")
all_clusters_path = os.path.join(dir_path,"training_data/pickle/clustered_songs/clusters.txt")



with Song_DB_DEMO() as demo_db:
# Creates the necessary tables for DB DEMO, no need to run multiple times
	demo_db.createTable_Song_No_Index()
	demo_db.createTable_Song_Clustered_Index()
	demo_db.createTable_Cluster()

# Add our calculated cluster centroids to the DB
	cluster_list = []
	with open(all_clusters_path, 'rb') as f:
		demo_db.delete_ALL_CLUSTERS_IN_Song_DB_DEMO()
		cluster_list = pickle.load(f)
		# ClusterID = 0
		# for cluster in cluster_list:
		# 	cluster.insert(0,ClusterID)
		# 	ClusterID += 1
		demo_db.insert_Clusters(cluster_list)


# Load the song list to be inserted into the database
	song_list = []
	with open(all_songs_path, 'rb') as f:
		song_list = pickle.load(f)

# Since our list of Training Songs is only ~6700 songs, we construct lists of three
# different lengths by randomly selecting songs from our list of 6700 and appending
# them to a new list until it is the desired length for testing.  Having duplicate 
# songs is not an issue because they are assigned an AUTO_INCREMENTED primary key and
# our distribution of songs/cluster will remain similar. Also, songs are not in any
# particular order as they enter the DB and so their location in terms of querying
# is random (for the non-indexed table).


# Test 1: 10 000 Songs
	demo_db.delete_ALL_SONGS_IN_Song_DB_DEMO() #Clear songs from database before each test
	songs_10000 = []
	for i in range(0,10000):
		songs_10000.append(random.choice(song_list))
	demo_db.insert_Song_No_Index(songs_10000)
	demo_db.insert_Song_Clustered_Index(songs_10000)
	demo_db.select_Song_By_ClusterID('Song_Clustered_Index', 5) 
	demo_db.select_Song_By_ClusterID('Song_No_Index', 5)
	demo_db.select_Song_By_Other('Song_Clustered_Index') # Query a non-clustered attribute
	demo_db.select_Song_By_Other('Song_No_Index')


# Test 2: 100 000 Songs
# 	demo_db.delete_ALL_SONGS_IN_Song_DB_DEMO()
# 	songs_100000 = []
# 	for i in range(0,100000):
# 		songs_100000.append(random.choice(song_list))
# 	demo_db.insert_Song_No_Index(songs_100000)
# 	demo_db.insert_Song_Clustered_Index(songs_100000)
# 	demo_db.select_Song_By_ClusterID('Song_Clustered_Index', 5) # Query by Clustered Index Attribute
# 	demo_db.select_Song_By_ClusterID('Song_No_Index', 5)
# 	demo_db.select_Song_By_Other('Song_Clustered_Index') # Query a non-clustered attribute
# 	demo_db.select_Song_By_Other('Song_No_Index')

# # Test 3: 1 000 000 Songs
# 	demo_db.delete_ALL_SONGS_IN_Song_DB_DEMO()
# 	songs_1000000 = []
# 	for i in range(0,1000000):
# 		songs_1000000.append(random.choice(song_list))
# 	demo_db.insert_Song_No_Index(songs_1000000)
# 	demo_db.insert_Song_Clustered_Index(songs_1000000)
# 	demo_db.select_Song_By_ClusterID('Song_Clustered_Index', 5) # Query by Clustered Index Attribute
# 	demo_db.select_Song_By_ClusterID('Song_No_Index', 5)
# 	demo_db.select_Song_By_Other('Song_Clustered_Index') # Query a non-clustered attribute
# 	demo_db.select_Song_By_Other('Song_No_Index')





