import Playlist
import Song
import pickle
import os

# This script takes a set up spotify playlists names from a textfile and retrieves all of the song data.
# All valid songs from the input textfile playlists are saved as a list of Song objects and stored
# in the outpath as a pickle text file

outpath = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/playlists_txt/Song_Lists_By_Playlist_Type'
textfiles_folder = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/playlists_txt'

for subdir, dirs, files in os.walk(textfiles_folder):
	for file in files:
		filepath = subdir + os.sep + file
		f = open(filepath,"r")
		all_songs = []
		name = os.path.basename(filepath)[:-4]
		for line in f:
			songs = []
			line = line[:-1]
			try:
				playlist = Playlist.Playlist(username='spotify', playlistname=line)
				playlist.get_playlist()
			except ValueError:
				continue
			if playlist.playlist_song_names is None:
				continue
			else:
				for i in range(0,len(playlist.playlist_song_names)):
					try:
						song_attributes = {
							"accousticness" : playlist.playlist_accousticness[i],
							"artist_name" : playlist.playlist_song_artists[i],
							"cluster_id" : 9999, # cluster_id = 9999 indicates not clustered
							"danceability" : playlist.playlist_dancibility[i],
							"energy" : playlist.playlist_energy[i],
							"from_playlist" : name.lower(),
							"instrumentalness" : playlist.playlist_instrumentalness[i],
							"loudness" : playlist.playlist_loudness[i],
							"speechiness" : playlist.playlist_speechness[i],
							"tempo" : playlist.playlist_tempo[i],
							"title" : playlist.playlist_song_names[i],
							"valence" : playlist.playlist_valence[i]
							}
						song = Song.Song(song_attributes)
					except IndexError:
						print "CAUGHT INDEX ERROR"
						songs = []
						continue
					if song.hasData:
						songs.append(song)
				for song in songs:
					all_songs.append(song)
		outfile = open(os.path.join(outpath,name+".txt"),"wb")
		pickle.dump(all_songs,outfile)





















