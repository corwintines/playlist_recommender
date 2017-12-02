import sys
from Playlist import Playlist
from nimblenet.data_structures import Instance
from nimblenet.neuralnet import NeuralNet
from playlist_recommender_utilities import *


username = sys.argv[1]
playlist = sys.argv[2]

base_playlist = Playlist(username, playlist)
base_playlist.get_playlist()
base_playlist.generate_playlist_vector()
base_playlist.generate_normalized_aggregate_vector()

# Funtion to return the 100 closet songs to playlist normalized_aggregate_vectors
#hundred_song_set = gather_hunder_songs(base_playlist)

# prediction_set = create_prediction_data(hundred_song_set)
# network = NeuralNet.load_network_from_file( "%s.pkl" % "training54point1" )
# recommended_values = network.predict(prediction_set)
#returned_playlist = generate_top_twentyfive(recommended_values, hundred_song_set)

# print returned_playlist
