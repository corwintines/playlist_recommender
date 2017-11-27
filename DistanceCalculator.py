import numpy as np
from operator import itemgetter
from sklearn.cluster import KMeans
import scipy
from scipy.stats.stats import pearsonr
from Playlist import Playlist



aggregateVector = [0]
listOfCentroids = ([1],
				   [2],
				   [3],
				   [4],
				   [5],
				   [5],
				   [4],
				   [3],
				   [2],
				   [1])

song_attributes = []
p = Playlist('spotify', '37i9dQZF1DX76Wlfdnj7AP')
p.get_playlist()
for song in range(0, len(p.playlist_song_names)):
	song_attributes.append((p.playlist_dancibility[song], p.playlist_energy[song], p.playlist_loudness[song], p.playlist_accousticness[song], p.playlist_instrumentalness[song], p.playlist_speechness[song], p.playlist_tempo[song], p.playlist_valence[song]))


songAttributes = [(0,1,2,3,4),
				  (1,2,4,3,5),
				  (1,2,5,6,4),
				  (1,2,4,5,8),
				  (6,5,1,2,5),
				  (4,3,2,4,5),
				  (9,8,6,3,7)]

x = (1,2,3,4,5,6,7,8)
y = (1,2,3,4,5,6,7,8)

def closestCentroid(aggregateVector, listOfCentroids):
	closestIndex = []
	for x in range(0,len(listOfCentroids)):
		length = len(listOfCentroids[x])
		count = 0

		for y in range(0, length):
			count = count  + (abs(aggregateVector[y] - listOfCentroids[x].__getitem__(y))**2)

		if x == 0:
				closestIndex.append([x, count**(1/2.0)])
				lowestdistance = count**(1/2.0)

		Dist = count**(1/2.0)
		if Dist < lowestdistance :
			closestIndex.pop(0)
			closestIndex.append([x, Dist])
			lowestdistance = Dist

	return closestIndex[0].__getitem__(0)


def closestSongs(aggregateVector, listOfSongs, n):
	closestIndex = []
	for x in range(0,len(listOfSongs)):
		length = len(listOfSongs[x])
		count = 0
		Dist = 0

		for y in range(0, length):
			count = count  + (abs(aggregateVector[y] - listOfSongs[x].__getitem__(y))**2)
			Dist = count**(1/2.0)

		if(x < n):
			closestIndex.append((x, Dist))

		closestIndex.sort(key=itemgetter(1))

		if (x >= n):
			if Dist < (closestIndex[n-1].__getitem__(1)) :
				closestIndex.pop(n-1)
				closestIndex.append((x, Dist))
				closestIndex.sort(key=itemgetter(1))

	return [x[0] for x in closestIndex]





closestCentroid(aggregateVector, listOfCentroids)

closestSongs(aggregateVector, listOfCentroids, 3)


def cluster_data(data):
    attributes = data
    kmeans = KMeans(n_clusters=2, random_state=0).fit(attributes)
    labels = kmeans.predict(attributes)
    centroids = kmeans.cluster_centers_
    return labels, centroids

def pearsonCorrelation(songAttributes):
	numOfElements = (len(songAttributes))
	sizeOfElement = (len(songAttributes[0]))
	print 'Num of Elements ', numOfElements
	print 'Values inside the Element ', sizeOfElement
	correlationMatrix = []
	temp = []
	l = 1
	for i in range(0, sizeOfElement):
		locals()["group"+str(i)] = []
		for j in range(0, numOfElements):
			locals()["group"+str(i)].append(songAttributes[j].__getitem__(i))

		print str(i), locals()["group"+str(i)]
		if (i == 14):
			for k in range(0, sizeOfElement):
				l = k+1
				while(l < sizeOfElement):
					tuple1 = tuple(locals()["group"+str(k)])
					tuple2 = tuple(locals()["group"+str(l)])
					temp = scipy.stats.pearsonr(tuple1,tuple2)
					correlationMatrix.append(temp[0])
					l = l+1
	return correlationMatrix

def pearsonCorrelationDict(p):
	numOfElements = (len(songAttributes))
	sizeOfElement = (len(songAttributes[0]))
	'''
	Danceability = []
	Energy = []
	Loudness = []
	Accousticness = []
	Instrumentalness = []
	Speechness = []
	Tempo = []
	Valence = []

	for i in range(0, (len(song_attributes[0]))):
		for j in range(0, (len(song_attributes))):
			if i == 0:
				Danceability.append(song_attributes[j].__getitem__(i))
			if i == 1:
				Energy.append(song_attributes[j].__getitem__(i))
			if i == 2:
				Loudness.append(song_attributes[j].__getitem__(i))
			if i == 3:
				Accousticness.append(song_attributes[j].__getitem__(i))
			if i == 4:
				Instrumentalness.append(song_attributes[j].__getitem__(i))
			if i == 5:
				Instrumentalness.append(song_attributes[j].__getitem__(i))
			if i == 6;
				Instrumentalness.append(song_attributes[j].__getitem__(i))
			if i == 7:
				Instrumentalness.append(song_attributes[j].__getitem__(i))

	'''
	dict = {'Dancibility' : {'Energy':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_energy)[0]), 'Loudness':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_loudness)[0]), 'Accousticness' :(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_valence)[0])},
			'Energy' : {'Danceability':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_dancibility)[0]), 'Loudness':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_loudness)[0]), 'Accousticness' :(scipy.stats.pearsonr(p.playlist_energy,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_valence)[0])},
			'Loudness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_energy)[0]), 'Accousticness' :(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_valence)[0])},
			'Accousticness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_loudness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_valence)[0])},
			'Instrumentalness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_accousticness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_valence)[0])},
			'Speechness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_instrumentalness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_valence)[0])},
			'Tempo' : {'Danceability':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_speechness)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_valence)[0])},
			'Valence' : {'Danceability':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_valence,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_tempo)[0])}}

	return dict


def outputCorrelation(p):
	playlistname = p.playlist_playlistname + ".txt"
	openfile = open(str(playlistname), "w+")
	openfile.write("Dancibility :")
	openfile.write(str(pearsonCorrelationDict(p)['Dancibility']))
	openfile.write("\n\n")
	openfile.write("Energy :")
	openfile.write(str(pearsonCorrelationDict(p)['Energy']))
	openfile.write("\n\n")
	openfile.write("Loudness :")
	openfile.write(str(pearsonCorrelationDict(p)['Loudness']))
	openfile.write("\n\n")
	openfile.write("Accousticness :")
	openfile.write(str(pearsonCorrelationDict(p)['Accousticness']))
	openfile.write("\n\n")
	openfile.write("Instrumentalness :")
	openfile.write(str(pearsonCorrelationDict(p)['Instrumentalness']))
	openfile.write("\n\n")
	openfile.write("Speechness :")
	openfile.write(str(pearsonCorrelationDict(p)['Speechness']))
	openfile.write("\n\n")
	openfile.write("Tempo :")
	openfile.write(str(pearsonCorrelationDict(p)['Tempo']))
	openfile.write("\n\n")
	openfile.write("Valence :")
	openfile.write(str(pearsonCorrelationDict(p)['Valence']))
	openfile.write("\n\n")
	openfile.close()

outputCorrelation(p)
