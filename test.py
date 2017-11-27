from Playlist import Playlist
from TrainingPlaylist import TrainingPlaylist
from dataset_processing import *
from k_means_clustering_dataset import *
import pickle

# p = Playlist('spotify','37i9dQZF1DWZeKCadgRdKQ')
# p = Playlist('spotify','37i9dQZF1DX76Wlfdnj7AP')
# p.get_playlist()
# p.generate_playlist_vector()
# print p.playlist_attribute_vector

# t = TrainingPlaylist('spotify','37i9dQZF1DX76Wlfdnj7AP')
# t.get_playlist()
# t.construct_training_groundtruths()
# t.generate_playlist_vector()
# print t.training_attribute_vector
# t.find_cluster()
# t.trim_outliers()

song_data = query_spotify_for_attributes()
k_means_labels, k_means_centroids = cluster_data(song_data)
# (clusterid, title, artist, acousticness, artist_familiarity, artist_hotness, dancability, duration, endOfFadeIn, energy, intrumentalness, loudness, speechiness, startOfFadeOut, tempo, valence)
combined_cluster_song_data = combine_cluster_song_data(song_data, k_means_labels)
data_output = open('data.txt', 'wb')
centroid_output = open('centroid.txt', 'wb')
pickle.dump(combined_cluster_song_data, data_output)
pickle.dump(k_means_centroids, centroid_output)
data_output.close
centroid_output.close

with open('data.txt', 'rb') as f:
    data = pickle.load(f)
    print data
