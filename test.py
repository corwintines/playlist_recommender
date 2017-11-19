from Playlist import Playlist
from TrainingPlaylist import TrainingPlaylist

# p = Playlist('spotify','37i9dQZF1DX76Wlfdnj7AP')
# p.get_playlist()
# p.generate_playlist_vector()
# print p.playlist_attribute_vector

t = TrainingPlaylist('spotify','37i9dQZF1DX76Wlfdnj7AP')
t.get_playlist()
t.construct_training_groundtruths()
t.generate_playlist_vector()
print t.training_attribute_vector
