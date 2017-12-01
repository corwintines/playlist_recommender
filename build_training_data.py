import deltaVector
import os
import pickle
import numpy 
import math

pickles_folder = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/training_data/pickle/normalized/agg'

for subdir, dirs, files in os.walk(pickles_folder):
	for file in files:
		if file != '.DS_Store':
			filepath = subdir + os.sep + file
			# deltaVector.normalize_from_pickle(filepath)
			# deltaVector.findAverage_from_pickle(filepath)
			aggregate_song_list1 = os.path.join(os.path.dirname(filepath),'agg_normalized_Fitness.txt')
			in1 = open(aggregate_song_list1,'rb')
			song_list_1 = pickle.load(in1)
			in1.close()
			in2 = open(filepath,'rb')
			song_list_2 = pickle.load(in2)
			in2.close()
			difference_dict = deltaVector.findDistance(song_list_1, 'agg_normalized_Fitness.txt', song_list_2, os.path.basename(filepath))
			distance = math.sqrt(
				math.pow(difference_dict["accousticness"],2) +
				math.pow(difference_dict['danceability'],2) +
				math.pow(difference_dict["energy"],2) +
				math.pow(difference_dict["instrumentalness"],2) +
				math.pow(difference_dict["loudness"],2) +
				math.pow(difference_dict["speechiness"],2) +
				math.pow(difference_dict["tempo"],2) +
				math.pow(difference_dict["valence"],2))
			print "distance ",distance, difference_dict["playlist_type_1"], difference_dict["playlist_type_2"]
