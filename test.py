from Playlist import Playlist
from TrainingPlaylist import TrainingPlaylist

# p = Playlist('spotify','37i9dQZF1DX76Wlfdnj7AP')
# p.get_playlist()
# p.generate_playlist_vector()
# print p.playlist_attribute_vector

t = TrainingPlaylist('spotify','37i9dQZF1DX76Wlfdnj7AP')
t.get_playlist()
print t.playlist_song_names
