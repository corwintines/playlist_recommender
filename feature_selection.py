import deltaVector
import Song
import pickle_tools_Luke
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

distance_dictionaries = []
sorted_lists = []

for subdir, dirs, files in os.walk(os.path.join(dir_path,'training_data/pickle/normalized')):
	for file in files:
		filepath1 = subdir + os.sep + file
		if '.DS_Store' in filepath1:
			continue
		if 'Fitness' in filepath1:
			song_list1 = pickle_tools_Luke.returnObjectFromPickle(filepath1)
			for file in files:
				filepath2 = subdir + os.sep + file
				if '.DS_Store' in filepath2:
					continue
				song_list2 = pickle_tools_Luke.returnObjectFromPickle(filepath2)
				agg_vect1 = deltaVector.findAverage(song_list1)
				agg_vect2 = deltaVector.findAverage(song_list2)
				name1 = os.path.basename(filepath1)
				name2 = os.path.basename(filepath2)
				distance_dict = deltaVector.findDistance(agg_vect1, name1, agg_vect2, name2)
				distance_dictionaries.append(distance_dict)

for dictionary in distance_dictionaries:
	accousticness = ('accousticness',dictionary['accousticness'])
	speechiness = ('speechiness',dictionary['speechiness'])
	compared_to = ('compared_to',dictionary['playlist_type_2'])
	danceability = ('danceability',dictionary['danceability'])
	loudness = ('loudness',dictionary['loudness'])
	energy = ('energy',dictionary['energy'])
	valence = ('valence',dictionary['valence'])
	tempo = ('tempo',dictionary['tempo'])
	instrumentalness = ('instrumentalness',dictionary['instrumentalness'])
	tup_list = []
	tup_list.append(accousticness)
	tup_list.append(speechiness)
	tup_list.append(compared_to)
	tup_list.append(danceability)
	tup_list.append(loudness)
	tup_list.append(energy)
	tup_list.append(valence)
	tup_list.append(tempo)
	tup_list.append(instrumentalness)
	sorted_tup_list = sorted(tup_list, key=lambda x: x[1],reverse=True)
	sorted_lists.append(sorted_tup_list)
	for tup in sorted_tup_list:
		print "{0:20} {1}".format(tup[0],tup[1])
	print "\n"

totals = [
	['accousticness',0],
	['danceability',0],
	['loudness',0],
	['energy',0],
	['instrumentalness',0],
	['speechiness',0],
	['tempo',0],
	['valence',0]
	]

for l in sorted_lists:
	if l[0][0]=='accousticness' or l[1][0]=='accousticness' or l[2][0]=='accousticness':
		totals[0][1]+=1
	if l[0][0]=='danceability' or l[1][0]=='danceability' or l[2][0]=='danceability':
		totals[1][1]+=1
	if l[0][0]=='loudness' or l[1][0]=='loudness' or l[2][0]=='loudness':
		totals[2][1]+=1
	if l[0][0]=='energy' or l[1][0]=='energy' or l[2][0]=='energy':
		totals[3][1]+=1
	if l[0][0]=='instrumentalness' or l[1][0]=='instrumentalness' or l[2][0]=='instrumentalness':
		totals[4][1]+=1
	if l[0][0]=='speechiness' or l[1][0]=='speechiness' or l[2][0]=='speechiness':
		totals[5][1]+=1
	if l[0][0]=='tempo' or l[1][0]=='tempo' or l[2][0]=='tempo':
		totals[6][1]+=1
	if l[0][0]=='valence' or l[1][0]=='valence' or l[2][0]=='valence':
		totals[7][1]+=1

total = sorted(totals, key=lambda x: x[1],reverse=True)
print "TOTALS: "
for row in total:
	print "{0:20} {1}".format(row[0],row[1])








