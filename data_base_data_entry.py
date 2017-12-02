import os
from sql_connector import Song_DB
import Song
import Cluster
import hdf5_access_Luke
import pickle_tools_Luke
import os
import Playlist


dir_path = os.path.dirname(os.path.realpath(__file__))

agg_normalized = os.path.join(dir_path,'training_data/pickle/agg_normalized')

normalized = os.path.join(dir_path,'training_data/pickle/normalized')

song_lists = os.path.join(dir_path,'training_data/pickle/song_lists')

song_lists_with_recommended = os.path.join(dir_path,'training_data/pickle/song_lists_with_recommended')

msd_original_data_folder = os.path.join(dir_path,'/MillionSongSubset/data')

output_folder = os.path.join(dir_path,'training_data/pickle/songs_msd')
pickle_file_name = 'song_list_mined_from_hdf5.txt'
out_path = os.path.join(output_folder,pickle_file_name)


# msd_songs = pickle_tools_Luke.returnObjectFromPickle(out_path)
# spotify_songs = pickle_tools_Luke.returnObjectFromPickle(os.path.join(dir_path,'msd_data/all_song_data.txt'))
# title_list = []
# for song in spotify_songs:
# 	title = song[0].lower().replace("'","").replace(" ","_")
# 	title_list.append(title)
# for song in msd_songs:
# 	if song.attributes['title'].lower().replace("'","").replace(" ","_") in title_list:
# 		print song.attributes['title']

for subdir, dirs, files in os.walk(song_lists_with_recommended):
	for file in files:
		filepath = subdir + os.sep + file
		songs_with_rec = pickle_tools_Luke.returnObjectFromPickle(filepath)
		for song in songs_with_rec:
			print song.attributes


# with Song_DB() as dbase:
	


	# song_list = hdf5_access_Luke.getSongs_MSD(msd_original_data_folder)
	# out_path = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/training_data/pickle/songs_msd/song_list_mined_from_hdf5.txt'
	# pickle_tools_Luke.writeToPickle(song_list, out_path)
	# print songs

	# songs = pickle_tools_Luke.returnObjectFromPickle('/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/msd_data/all_song_data.txt')
	# for song in songs:
	# 	print song
	



	# clusters = pickle_tools_Luke.returnObjectFromPickle('/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/msd_data/centroids.txt')
	# cluster_id = 0
	# cluster_objects = []
	# for cluster in clusters:
	# 	clusterDict = {
	# 		"accousticness" : cluster[0],
	# 		"cluster_id" : cluster_id,
	# 		"energy" : cluster[1],
	# 		"instrumentalness" : cluster[2],
	# 		"loudness" : cluster[3],
	# 		"speechiness" : cluster[4]
	# 		}
	# 	cluster_object = Cluster.Cluster(clusterDict)
	# 	cluster_objects.append(cluster_object)
	# for c in cluster_objects:
	# 	print c.attributes

	# dbase.insert_Clusters(cluster_list)
	# dbase.createTable_Playlist_Compare()
	# for subdir, dirs, files in os.walk(song_lists_with_recommended):
	# 	for file in files:
	# 		filepath = subdir + os.sep + file
	# 		song_list = Song.readSongListFromPickle(filepath)
	# 		dbase.insert_Training_Songs(song_list)
			# for song in song_list:
			# 	print song.attributes
