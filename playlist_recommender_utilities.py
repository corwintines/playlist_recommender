from nimblenet.data_structures import Instance
from Song import Song
from sql_connector import *
from Cluster import Cluster
import math
import numpy as np

def gather_hundred_songs(playlist):
    hundred_songs = []

    find_cluster_index(playlist)
    cluster_songs = get_cluster_songs(playlist.playlist_cluster_index)
    hundred_closest_songs_indexes = get_closest_songs(playlist, cluster_songs)
    for song_index in hundred_closest_songs_indexes:
        hundred_songs.append(cluster_songs[song_index])

    return hundred_songs


def find_cluster_index(playlist):
    clusters_list = []
    with Song_DB() as dbase:
        clusters = dbase.select_By_Query(query="SELECT * FROM Cluster;")
        for cluster in clusters:
            cluster_dict = {
    			"cluster_id" : cluster[0],
    			"accousticness" : cluster[0],
    			"danceability" : cluster[1],
    			"energy" : cluster[2],
    			"instrumentalness" : cluster[3],
    			"valence" : cluster[4]
    		}
    	    c = Cluster(cluster_dict)
            clusters_list.append(c)

    distance_clusters(playlist, clusters_list)


def distance_clusters(playlist, cluster_list):
    playlist_vector = [playlist.normalized_aggregate_vector[0],
                       playlist.normalized_aggregate_vector[1],
                       playlist.normalized_aggregate_vector[2],
                       playlist.normalized_aggregate_vector[3],
                       playlist.normalized_aggregate_vector[7]]

    cluster_aggregate_vectors = []
    for cluster in cluster_list:
        cluster_vector = [float(cluster.attributes["accousticness"]),
                          float(cluster.attributes["danceability"]),
                          float(cluster.attributes["energy"]),
                          float(cluster.attributes["instrumentalness"]),
                          float(cluster.attributes["valence"])]

        cluster_aggregate_vectors.append(cluster_vector)

    distances = []
    for cluster_vector in cluster_aggregate_vectors:
        dist = math.sqrt(math.pow((playlist_vector[0]-cluster_vector[0]),2)+math.pow((playlist_vector[1]-cluster_vector[1]),2)+math.pow((playlist_vector[2]-cluster_vector[2]),2)+math.pow((playlist_vector[3]-cluster_vector[3]),2)+math.pow((playlist_vector[4]-cluster_vector[4]),2))
        distances.append(dist)

    selected_cluster = distances.index(min(distances))
    playlist.playlist_cluster_index = cluster_list[selected_cluster].attributes["cluster_id"]


def get_cluster_songs(cluster_index):
    song_objects = []
    with Song_DB() as dbase:
        songs = dbase.select_Song_By_ClusterID('Song', cluster_index)
        for song in songs:
            song_dict = {
                "title": song[2],
                "artist_name": song[3],
                "cluster_id" : song[1],
                "accousticness" : song[5],
                "danceability" : song[8],
                "energy" : song[11],
                "instrumentalness" : song[12],
                "loudness": song[13],
                "speechiness": song[15],
                "tempo" : song[17],
                "valence" : song[18]
    		}
            song_object = Song.Song(song_dict)
            song_objects.append(song_object)

    return song_objects


def get_closest_songs(playlist, songs):
    playlist_vector = [playlist.normalized_aggregate_vector[0],
                       playlist.normalized_aggregate_vector[1],
                       playlist.normalized_aggregate_vector[2],
                       playlist.normalized_aggregate_vector[3],
                       playlist.normalized_aggregate_vector[7]]

    song_vectors= []
    for song in songs:
        song_vector = [float(song.attributes["accousticness"]),
                       float(song.attributes["danceability"]),
                       float(song.attributes["energy"]),
                       float(song.attributes["instrumentalness"]),
                       float(song.attributes["valence"])]
        song_vectors.append(song_vector)

    song_distances = []
    for song in song_vectors:
        dist = math.sqrt(math.pow((playlist_vector[0]-song[0]),2)+math.pow((playlist_vector[1]-song[1]),2)+math.pow((playlist_vector[2]-song[2]),2)+math.pow((playlist_vector[3]-song[3]),2)+math.pow((playlist_vector[4]-song[4]),2))
        song_distances.append(dist)

    return np.array(song_distances).argsort()[:100]


def create_prediction_data(song_list):
    prediction_set = []
    for song in song_list:
        prediction_set.append(Instance([float(song.attributes['accousticness']),
                                        float(song.attributes['danceability']),
                                        float(song.attributes['energy']),
                                        float(song.attributes['instrumentalness']),
                                        float(song.attributes['loudness']),
                                        float(song.attributes['speechiness']),
                                        float(song.attributes['tempo']),
                                        float(song.attributes['valence'])]))

    return prediction_set


def generate_top_twentyfive(recommended_values, hundred_song_set):
    top_twentyfive = []
    rec = []
    for value in range(0, len(recommended_values)):
        rec.append(recommended_values[value][0])
    top_twentyfive_indexes = np.array(rec).argsort()[:25]
    print top_twentyfive_indexes
    for index in top_twentyfive_indexes:
        top_twentyfive.append(hundred_song_set[index])

    return top_twentyfive
