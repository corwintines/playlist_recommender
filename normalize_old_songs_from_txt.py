import Song
import pickle_tools_Luke
import os
import deltaVector


dir_path = os.path.dirname(os.path.realpath(__file__))

for subdir, dirs, files in os.walk(os.path.join(dir_path,'training_data/pickle/normalized')):
	for file in files:
		filepath = subdir + os.sep + file
		if '.DS_Store' in filepath:
			continue
		song_list = pickle_tools_Luke.returnObjectFromPickle(filepath)
		agg_vect = deltaVector.findAverage(song_list)
		print agg_vect
		outpath = os.path.join(os.path.join(dir_path,'training_data/pickle/agg_normalized'),"agg_"+os.path.basename(filepath))
		pickle_tools_Luke.writeToPickle(agg_vect,outpath) 




# dir_path = os.path.dirname(os.path.realpath(__file__))

# for subdir, dirs, files in os.walk(os.path.join(dir_path,'training_data/pickle/normalized')):
# 	for file in files:
# 		filepath = subdir + os.sep + file
# 		if '.DS_Store' in filepath:
# 			continue
# 		song_list = pickle_tools_Luke.returnObjectFromPickle(filepath)
# 		new_song_list = []
# 		for song in song_list:
# 			print "\n",song.attributes
# 			# instrumentalness = song.attributes['loudness']
# 			# loudness = song.attributes['instrumentalness']
# 			# song.attributes.update({'loudness':loudness})
# 			# song.attributes.update({'instrumentalness':instrumentalness})
# 			# print "\n",song.attributes
# 			# song.normalize()
# 			# print "\nnormalized: ",song.attributes
# 			# new_song_list.append(song)
#			# pickle_tools_Luke.writeToPickle(new_song_list,os.path.join('/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/training_data/pickle/normalized',os.path.basename(filepath)))






