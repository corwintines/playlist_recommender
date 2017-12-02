import Song
import pickle_tools_Luke
import os



for subdir, dirs, files in os.walk('/Users/Yash/Desktop/playlist_recommender/training_data/pickle/song_lists'):
	for file in files:
		filepath = subdir + os.sep + file
		song_list = pickle_tools_Luke.returnObjectFromPickle(filepath)
		new_song_list = []
		for song in song_list:
			print song.attributes,"\n\n\n"
			song.normalize()
			print song.attributes, "\n"
			# new_song_list.append(song)
		# pickle_tools_Luke.writeToPickle(new_song_list,os.path.join(os.path.dirname(filepath),"new_"+os.path.basename(filepath)))