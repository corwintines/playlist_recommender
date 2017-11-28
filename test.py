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

# with open('song_data15.txt', 'rb') as f:
#     data = pickle.load(f)
#     print data
#     print len(data)
# song_data = query_spotify_for_attributes()
# song_data_output = open('song_data16.txt', 'wb')
# pickle.dump(song_data, song_data_output)
# song_data_output.close()

with open('all_song_data.txt', 'rb') as all_songs:
    allsongs = pickle.load(all_songs)
    k_means_labels, k_means_centroids = cluster_data(allsongs)
    # (clusterid, title, artist, acousticness, artist_familiarity, artist_hotness, dancability, duration, endOfFadeIn, energy, intrumentalness, loudness, speechiness, startOfFadeOut, tempo, valence)
    combined_cluster_song_data = combine_cluster_song_data(allsongs, k_means_labels)
    allsongs_combined_cluster_song_data_output = open('all_songs_cluster_combined.txt', 'wb')
    pickle.dump(combined_cluster_song_data, allsongs_combined_cluster_song_data_output)
    allsongs_combined_cluster_song_data_output.close()
    centroid_output = open('centroids.txt', 'wb')
    pickle.dump(k_means_centroids, centroid_output)
    centroid_output.close()

with open('centroids.txt', 'rb') as f:
    data = pickle.load(f)
    print data
f.close()

# all_song_data = []
# with open('song_data0.txt', 'rb') as song0:
#     data0 = pickle.load(song0)
#     print len(data0)
#     for song in data0:
#         all_song_data.append(song)
# with open('song_data1.txt', 'rb') as song1:
#     data1 = pickle.load(song1)
#     print len(data1)
#     for song in data1:
#         all_song_data.append(song)
# with open('song_data2.txt', 'rb') as song2:
#     data2 = pickle.load(song2)
#     print len(data2)
#     for song in data2:
#         all_song_data.append(song)
# with open('song_data3.txt', 'rb') as song3:
#     data3 = pickle.load(song3)
#     print len(data3)
#     for song in data3:
#         all_song_data.append(song)
# with open('song_data4.txt', 'rb') as song4:
#     data4 = pickle.load(song4)
#     print len(data4)
#     for song in data4:
#         all_song_data.append(song)
# with open('song_data5.txt', 'rb') as song5:
#     data5 = pickle.load(song5)
#     print len(data5)
#     for song in data5:
#         all_song_data.append(song)
# with open('song_data6.txt', 'rb') as song6:
#     data6 = pickle.load(song6)
#     print len(data6)
#     for song in data6:
#         all_song_data.append(song)
# with open('song_data7.txt', 'rb') as song7:
#     data7 = pickle.load(song7)
#     print len(data7)
#     for song in data7:
#         all_song_data.append(song)
# with open('song_data8.txt', 'rb') as song8:
#     data8 = pickle.load(song8)
#     print len(data8)
#     for song in data8:
#         all_song_data.append(song)
# with open('song_data9.txt', 'rb') as song9:
#     data9 = pickle.load(song9)
#     print len(data9)
#     for song in data9:
#         all_song_data.append(song)
# with open('song_data10.txt', 'rb') as song10:
#     data10 = pickle.load(song10)
#     print len(data10)
#     for song in data10:
#         all_song_data.append(song)
# with open('song_data11.txt', 'rb') as song11:
#     data11 = pickle.load(song11)
#     print len(data11)
#     for song in data11:
#         all_song_data.append(song)
# with open('song_data12.txt', 'rb') as song12:
#     data12 = pickle.load(song12)
#     print len(data12)
#     for song in data12:
#         all_song_data.append(song)
# with open('song_data13.txt', 'rb') as song13:
#     data13 = pickle.load(song13)
#     print len(data13)
#     for song in data13:
#         all_song_data.append(song)
# with open('song_data14.txt', 'rb') as song14:
#     data14 = pickle.load(song14)
#     print len(data14)
#     for song in data14:
#         all_song_data.append(song)
# with open('song_data15.txt', 'rb') as song15:
#     data15 = pickle.load(song15)
#     print len(data15)
#     for song in data15:
#         all_song_data.append(song)
# with open('song_data16.txt', 'rb') as song16:
#     data16 = pickle.load(song16)
#     print len(data16)
#     for song in data16:
#         all_song_data.append(song)
# all_song_data_output = open('all_song_data.txt', 'wb')
# pickle.dump(all_song_data, all_song_data_output)
# all_song_data_output.close()
