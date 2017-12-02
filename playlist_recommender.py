import sys
from Playlist import Playlist
from nimblenet.data_structures import Instance
from nimblenet.neuralnet import NeuralNet
from deltaVector import *

username = sys.argv[1]
playlist = sys.argv[2]

base_playlist = Playlist(username, playlist)
base_playlist.get_playlist()
base_playlist.generate_playlist_vector()
base_playlist.generate_normalized_aggregate_vector()

print base_playlist.normalized_aggregate_vector

#prediction_set = generate_input_data(hundred_song_set)
network = NeuralNet.load_network_from_file( "%s.pkl" % "54point5" )
#recommended_values = network.predict(prediction_set)
#returned_playlist = generate_top_twentyfive(recommended_values, hundred_song_set)
