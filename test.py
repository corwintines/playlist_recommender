from Playlist import Playlist
from TrainingPlaylist import TrainingPlaylist

p = Playlist('spotify','37i9dQZF1DX76Wlfdnj7AP')
p.get_playlist()
p.generate_playlist_vector()
print p.playlist_attribute_vector
