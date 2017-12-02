import os
from sql_connector import Song_DB
import Song
import Cluster
import pickle_tools_Luke
import k_means_clustering_dataset
import dataset_processing


dir_path = os.path.dirname(os.path.realpath(__file__))
all_songs_path_extension = 'training_data/pickle/song_lists_with_recommended/all_songs_with_rec.txt'
path_all_songs_no_cluster_id = os.path.join(dir_path,all_songs_path_extension)
path_all_songs_clustered = os.path.join(dir_path,'training_data/pickle/clustered_songs/all_songs_clustered.txt')
path_centroids = os.path.join(dir_path,'training_data/pickle/clustered_songs/centroids.txt')
path_clusters = os.path.join(dir_path,'training_data/pickle/clustered_songs/clusters.txt')

def centroidsToClusterList(path_centroids):
	centroids = pickle_tools_Luke.returnObjectFromPickle(path_centroids)
	cluster_list = []
	cluster_id = 0
	for centroid in centroids:
		cluster_dict = {
			"cluster_id" : cluster_id,
			"accousticness" : centroid[0],
			"danceability" : centroid[1],
			"energy" : centroid[2],
			"instrumentalness" : centroid[3],
			"valence" : centroid[4]
		}
		cluster = Cluster.Cluster(cluster_dict)
		cluster_list.append(cluster)
		cluster_id += 1
	pickle_tools_Luke.writeToPickle(cluster_list,path_clusters)

with Song_DB() as dbase:
	not_clustered = pickle_tools_Luke.returnObjectFromPickle(path_all_songs_no_cluster_id)
	print "clustering %d songs"%len(not_clustered)
	cluster_IDs_by_song_list_index, centroids = k_means_clustering_dataset.cluster_data(not_clustered)
	clustered = dataset_processing.combine_cluster_song_data(not_clustered, cluster_IDs_by_song_list_index)
	pickle_tools_Luke.writeToPickle(clustered,path_all_songs_clustered)
	pickle_tools_Luke.writeToPickle(centroids,path_centroids)
	all_songs = pickle_tools_Luke.returnObjectFromPickle(path_all_songs_clustered)
	
	dbase.createTable_Song()
	dbase.insert_Songs(all_songs)

	centroidsToClusterList(path_centroids)
	cluster_list = pickle_tools_Luke.returnObjectFromPickle(path_clusters)
	for cluster in cluster_list:
		print cluster.attributes

	dbase.createTable_Cluster()
	dbase.insert_Clusters(cluster_list)












