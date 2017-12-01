import deltaVector
import os
import pickle
import numpy
import math

pickles_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data','pickle','normalized','agg')


def get_distance_between_playlist_types():
	distance_dictonary = {}
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

				distance_dictonary.update({difference_dict["playlist_type_2"]:distance})

	return distance_dictonary


def normalize_distance_values(playlist_distances):
	furthest_distance = 0
	for key in playlist_distances:
		if playlist_distances[key] > furthest_distance:
			furthest_distance = playlist_distances[key]


	for key in playlist_distances:
		normalized_distance = playlist_distances[key]/furthest_distance
		playlist_distances.update({key:normalized_distance})

	return playlist_distances


def apply_normalized_distances(playlist_distances):
	iteration = 0
	for key in playlist_distances:
		if key == 'agg_normalized_R_B.txt':
			song_file = 'R_B.txt'
		else:
			song_file = str(key.split('_')[2])
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'song_lists', song_file)) as data:
			song_data = pickle.load(data)
			for song in song_data:
				song.attributes.update({"rec_value":playlist_distances[key]})

			song_file_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'song_lists_with_recommended', song_file), 'wb')
			pickle.dump(song_data, song_file_output)
			song_file_output.close()


def produce_training_test_playlists(playlist_distances):
	test_1 = []
	test_2 = []
	test_3 = []
	test_4 = []
	test_5 = []
	test_6 = []
	test_7 = []
	test_8 = []
	test_9 = []
	test_10 = []

	training_1 = []
	training_2 = []
	training_3 = []
	training_4 = []
	training_5 = []
	training_6 = []
	training_7 = []
	training_8 = []
	training_9 = []
	training_10 = []

	for key in playlist_distances:
		if key == 'agg_normalized_R_B.txt':
			song_file = 'R_B.txt'
		else:
			song_file = str(key.split('_')[2])
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'song_lists_with_recommended', song_file)) as data:
			song_data = pickle.load(data)
			for song in range(0, len(song_data)):
				if song%20 == 0:
					training_1.append(song_data[song])
				if song%20 == 1:
					training_2.append(song_data[song])
				if song%20 == 2:
					training_3.append(song_data[song])
				if song%20 == 3:
					training_4.append(song_data[song])
				if song%20 == 4:
					training_5.append(song_data[song])
				if song%20 == 5:
					training_6.append(song_data[song])
				if song%20 == 6:
					training_7.append(song_data[song])
				if song%20 == 7:
					training_8.append(song_data[song])
				if song%20 == 8:
					training_9.append(song_data[song])
				if song%20 == 9:
					training_10.append(song_data[song])
				if song%20 == 10:
					test_1.append(song_data[song])
				if song%20 == 11:
					test_2.append(song_data[song])
				if song%20 == 12:
					test_3.append(song_data[song])
				if song%20 == 13:
					test_4.append(song_data[song])
				if song%20 == 14:
					test_5.append(song_data[song])
				if song%20 == 15:
					test_6.append(song_data[song])
				if song%20 == 16:
					test_7.append(song_data[song])
				if song%20 == 17:
					test_8.append(song_data[song])
				if song%20 == 18:
					test_9.append(song_data[song])
				if song%20 == 19:
					test_10.append(song_data[song])

	training_1_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_1.txt'), 'wb')
	pickle.dump(training_1, training_1_output)
	training_1_output.close()
	training_2_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_2.txt'), 'wb')
	pickle.dump(training_2, training_2_output)
	training_2_output.close()
	training_3_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_3.txt'), 'wb')
	pickle.dump(training_3, training_3_output)
	training_3_output.close()
	training_4_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_4.txt'), 'wb')
	pickle.dump(training_4, training_4_output)
	training_4_output.close()
	training_5_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_5.txt'), 'wb')
	pickle.dump(training_5, training_5_output)
	training_5_output.close()
	training_6_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_6.txt'), 'wb')
	pickle.dump(training_6, training_6_output)
	training_6_output.close()
	training_7_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_7.txt'), 'wb')
	pickle.dump(training_7, training_7_output)
	training_7_output.close()
	training_8_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_8.txt'), 'wb')
	pickle.dump(training_8, training_8_output)
	training_8_output.close()
	training_9_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_9.txt'), 'wb')
	pickle.dump(training_9, training_9_output)
	training_9_output.close()
	training_10_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_10.txt'), 'wb')
	pickle.dump(training_10, training_10_output)
	training_10_output.close()

	test_1_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_1.txt'), 'wb')
	pickle.dump(test_1, test_1_output)
	test_1_output.close()
	test_2_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_2.txt'), 'wb')
	pickle.dump(test_2, test_2_output)
	test_2_output.close()
	test_3_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_3.txt'), 'wb')
	pickle.dump(test_3, test_3_output)
	test_3_output.close()
	test_4_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_4.txt'), 'wb')
	pickle.dump(test_4, test_4_output)
	test_4_output.close()
	test_5_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_5.txt'), 'wb')
	pickle.dump(test_5, test_5_output)
	test_5_output.close()
	test_6_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_6.txt'), 'wb')
	pickle.dump(test_6, test_6_output)
	test_6_output.close()
	test_7_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_7.txt'), 'wb')
	pickle.dump(test_7, test_7_output)
	test_7_output.close()
	test_8_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_8.txt'), 'wb')
	pickle.dump(test_8, test_8_output)
	test_8_output.close()
	test_9_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_9.txt'), 'wb')
	pickle.dump(test_9, test_9_output)
	test_9_output.close()
	test_10_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_10.txt'), 'wb')
	pickle.dump(test_10, test_10_output)
	test_10_output.close()


playlist_distances = get_distance_between_playlist_types()
normalized_playlist_distances = normalize_distance_values(playlist_distances)
apply_normalized_distances(normalized_playlist_distances)
produce_training_test_playlists(normalized_playlist_distances)
