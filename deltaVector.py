import numpy as np
import os 
import Song
import pickle


# playlist_compare_dictionary = {
# 	"playlist_type_1" : ''
# 	"playlist_type_2" : 'rock',
# 	"accousticness" : 0.4,
# 	"danceability" : 0.4,
# 	"energy" : 0.4,
# 	"instrumentalness" : 0.4,
# 	"loudness" : 0.4,
# 	"speechiness" : 0.4,
# 	"tempo" : 0.4,
# 	"valence" : 0.4
# 	}

def normalize_from_pickle(in_filepath):
	with open(in_filepath,'rb') as f:
		song_list = pickle.load(f)

		outpath = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/training_data/pickle/normalized'
		outfile = os.path.join(outpath,"normalized_"+os.path.basename(in_filepath))
		outf = open(outfile, 'wb')
		normalized_song_list = normalize(song_list)
		pickle.dump(normalized_song_list, outf)
		outf.close()
		for song in normalized_song_list:
			print song.attributes

def findAverage_from_pickle(in_filepath):
	inf = open(in_filepath,'rb')
	song_list = pickle.load(inf)
	inf.close()
	outpath = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/training_data/pickle/normalized'
	outfile = os.path.join(outpath,"agg_"+os.path.basename(in_filepath))
	outf = open(outfile, 'wb')
	findAverage_song_list = findAverage(song_list)
	pickle.dump(findAverage_song_list, outf)
	outf.close()
	print "PRINTING THE AGGREGATE VECTOR : ", " \n"
	for song in findAverage_song_list:
		print song, findAverage_song_list[song]

def findDistance_from_pickle(in_filepath):
	inf = open(in_filepath,'rb')
	song_list = pickle.load(inf)
	inf.close()
	outpath = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/training_data/pickle/normalized'
	outfile = os.path.join(outpath,"distance_"+os.path.basename(in_filepath))
	outf = open(outfile, 'wb')
	findDistance_song_list = findDistance(song_list)
	pickle.dump(findDistance_song_list, outf)
	outf.close()
	print "PRINTING THE Distance VECTOR : ", " \n"
	for song in findDistance_song_list:
		print song, findDistance_song_list[song]

def normalize(song_list):
	danceability = []
	energy = []
	loudness = []
	accousticness = []
	instrumentalness = []
	speechiness = []
	tempo = []
	valence = []

	for song in song_list:
		if song.hasData:
			danceability.append(song.attributes['danceability'])
			energy.append(song.attributes['energy'])
			loudness.append(song.attributes['loudness'])
			accousticness.append(song.attributes['accousticness'])
			instrumentalness.append(song.attributes['instrumentalness'])
			speechiness.append(song.attributes['speechiness'])
			tempo.append(song.attributes['tempo'])
			valence.append(song.attributes['valence'])

	mindanceability = min(danceability)
	maxdanceability = max(danceability)
	minenergy = min(energy)
	maxenergy = max(energy)
	minloudness = min(loudness)
	maxloudness = max(loudness)
	minaccousticness = min(accousticness)
	maxaccousticness = max(accousticness)
	mininstrumentalness = min(instrumentalness)
	maxinstrumentalness = max(instrumentalness)
	minspeechiness = min(speechiness)
	maxspeechiness = max(speechiness)
	mintempo = min(tempo)
	maxtempo = max(tempo)
	minvalence = min(valence)
	maxvalence = max(valence)
	danceability = []
	energy = []
	loudness = []
	accousticness = []
	instrumentalness = []
	speechness = []
	tempo = []
	valence = []
	output = []

	for song in song_list:
		v = (song.attributes['danceability']-mindanceability)/(maxdanceability-mindanceability)
		if(v == 0):
			song.attributes['danceability'] = 0.0000001 
		else:
			song.attributes['danceability'] = v

		v = (song.attributes['energy']-minenergy)/(maxenergy-minenergy)
		if(v == 0):
			song.attributes['energy'] = 0.0000001 
		else:
			song.attributes['energy'] = v

		v = (song.attributes['loudness']-minloudness)/(maxloudness-minloudness)
		if(v == 0):
			song.attributes['loudness'] = 0.0000001 
		else:
			song.attributes['loudness'] = v

		v = (song.attributes['accousticness']-minaccousticness)/(maxaccousticness-minaccousticness)
		if(v == 0):
			song.attributes['accousticness'] = 0.0000001 
		else:
			song.attributes['accousticness'] = v

		v = (song.attributes['instrumentalness']-mininstrumentalness)/(maxinstrumentalness-mininstrumentalness)
		if(v == 0):
			song.attributes['instrumentalness'] = 0.0000001 
		else:
			song.attributes['instrumentalness'] = v

		v = (song.attributes['speechiness']-minspeechiness)/(maxspeechiness-minspeechiness)
		if(v == 0):
			song.attributes['speechiness'] = 0.0000001 
		else:
			song.attributes['speechiness'] = v

		v = (song.attributes['tempo']-mintempo)/(maxtempo-mintempo)
		if(v == 0):
			song.attributes['tempo'] = 0.0000001 
		else:
			song.attributes['tempo'] = v

		v = (song.attributes['valence']-minvalence)/(maxvalence-minvalence)
		if(v == 0):
			song.attributes['valence'] = 0.0000001 
		else:
			song.attributes['valence'] = v
	return song_list

def findAverage(song_list):
	danceability = []
	energy = []
	loudness = []
	accousticness = []
	instrumentalness = []
	speechiness = []
	tempo = []
	valence = []

	playlistname = ""
	for song in song_list:
		playlistname = song.attributes['from_playlist']
		danceability.append(song.attributes['danceability'])
		energy.append(song.attributes['energy'])
		loudness.append(song.attributes['loudness'])
		accousticness.append(song.attributes['accousticness'])
		instrumentalness.append(song.attributes['instrumentalness'])
		speechiness.append(song.attributes['speechiness'])
		tempo.append(song.attributes['tempo'])
		valence.append(song.attributes['valence'])

	playlist_compare_dictionary = {
		"playlist_type_1" : playlistname,
		"playlist_type_2" : None,
		"accousticness" : np.mean(accousticness),
		"danceability" : np.mean(danceability),
		"energy" : np.mean(energy),
		"instrumentalness" : np.mean(instrumentalness),
		"loudness" : np.mean(loudness),
		"speechiness" : np.mean(speechiness),
		"tempo" : np.mean(tempo),
		"valence" : np.mean(valence)
		}

	return playlist_compare_dictionary


def findDistance(aggregate_song_list1, list1_name, aggregate_song_list2, list2_name):
	distance = {
		"playlist_type_1" : list1_name,
		"playlist_type_2" : list2_name,
		"accousticness" : abs(aggregate_song_list1['accousticness'] - aggregate_song_list2['accousticness']),
		"danceability" :  abs(aggregate_song_list1['danceability'] - aggregate_song_list2['danceability']),
		"energy" :  abs(aggregate_song_list1['energy'] - aggregate_song_list2['energy']),
		"instrumentalness" :  abs(aggregate_song_list1['instrumentalness'] - aggregate_song_list2['instrumentalness']),
		"loudness" :  abs(aggregate_song_list1['loudness'] - aggregate_song_list2['loudness']),
		"speechiness" :  abs(aggregate_song_list1['speechiness'] - aggregate_song_list2['speechiness']),
		"tempo" :  abs(aggregate_song_list1['tempo'] - aggregate_song_list2['tempo']),
		"valence" :  abs(aggregate_song_list1['valence'] - aggregate_song_list2['valence'])
		}
	return distance


# normalize_from_pickle('/Users/Yash/Desktop/playlist_recommender/song_list_pickles/Country.txt')
# findAverage_from_pickle('/Users/Yash/Desktop/playlist_recommender/normalized_song_list_pickles/normalized_Country.txt')
# findDistance_from_pickle('/Users/Yash/Desktop/playlist_recommender/findAverage_song_list_pickles/agg_normalized_Country.txt')




	
