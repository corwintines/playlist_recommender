import numpy as np
from operator import itemgetter
from sklearn.cluster import KMeans
import scipy
from scipy.stats.stats import pearsonr
from Playlist import Playlist
from dataset_processing import *



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
smoothjazz_attributes = []
p = Playlist('spotify', '37i9dQZF1DX76Wlfdnj7AP')
p.get_playlist()
for song in range(0, (len(p.playlist_song_names)-1)):
	song_attributes.append((p.playlist_dancibility[song], p.playlist_energy[song], p.playlist_loudness[song], p.playlist_accousticness[song], p.playlist_instrumentalness[song], p.playlist_speechness[song], p.playlist_tempo[song], p.playlist_valence[song]))
p2 = Playlist('spotify', '37i9dQZF1DXdxcBWuJkbcy')
p2.get_playlist()

p3 = Playlist('spotify', '37i9dQZF1DX8CwbNGNKurt')
p3.get_playlist()

p4 = Playlist('spotify', '37i9dQZF1DX35oM5SPECmN')
p4.get_playlist()


p5 = Playlist('spotify', '37i9dQZF1DWSJHnPb1f0X3')
p5.get_playlist()

p6 = Playlist('spotify', '37i9dQZF1DX6hvx9KDaW4s')
p6.get_playlist()

p7 = Playlist('spotify', '37i9dQZF1DWZYWNM3NfvzJ')
p7.get_playlist()

p8 = Playlist('spotify', '37i9dQZF1DX4eRPd9frC1m')
p8.get_playlist()

p9 = Playlist('spotify', '37i9dQZF1DX70RN3TfWWJh')
p9.get_playlist()

p10 = Playlist('spotify', '37i9dQZF1DX21UfQ8M3LWJ')
p10.get_playlist()

smoothjazz = Playlist('spotify', '37i9dQZF1DX0SM0LYsmbMT')
smoothjazz.get_playlist()

country = Playlist('spotify', '37i9dQZF1DWSK8os4XIQBk')
country.get_playlist()

sleep = Playlist('spotify', '37i9dQZF1DWZd79rJ6a7lp')
sleep.get_playlist()

coffee = Playlist('spotify', '37i9dQZF1DX6ziVCJnEm59')
coffee.get_playlist()

sleep2 = Playlist('spotify', '37i9dQZF1DX4sWSpwq3LiO')
sleep2.get_playlist()

lastfitness = Playlist('spotify', '37i9dQZF1DX0HRj9P7NxeE')
lastfitness.get_playlist()

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


def pearsonCorrelation2(songAttributes):
	numOfElements = (len(songAttributes))
	sizeOfElement = (len(songAttributes[0]))

	artist_familiarity = []
	artist_hotness = []
	duration = []
	endoffadein = []
	startoffadeout = []
	accousticness = []
	dancibility = []
	energy = []
	loudness = []
	instrumentalness = []
	speechness = []
	tempo = []
	valence = []

	for i in range(0, (len(songAttributes[0]))):
		for j in range(0, (len(songAttributes))):
			if i == 0:
				artist_familiarity.append(songAttributes[j].__getitem__(i))
			if i == 1:
				artist_hotness.append(songAttributes[j].__getitem__(i))
			if i == 2:
				duration.append(songAttributes[j].__getitem__(i))
			if i == 3:
				endoffadein.append(songAttributes[j].__getitem__(i))
			if i == 4:
				startoffadeout.append(songAttributes[j].__getitem__(i))
			if i == 5:
				accousticness.append(songAttributes[j].__getitem__(i))
			if i == 6:
				dancibility.append(songAttributes[j].__getitem__(i))
			if i == 7:
				energy.append(songAttributes[j].__getitem__(i))
			if i == 8:
				loudness.append(songAttributes[j].__getitem__(i))
			if i == 9:
				instrumentalness.append(songAttributes[j].__getitem__(i))
			if i == 10:
				speechness.append(songAttributes[j].__getitem__(i))
			if i == 11:
				tempo.append(songAttributes[j].__getitem__(i))
			if i == 12:
				valence.append(songAttributes[j].__getitem__(i))
	'''
	print "artist_familiarity : ", artist_familiarity
	print "artist_hotness : ", artist_hotness
	print "duration : ", duration
	print "endoffadein : ", endoffadein
	print "startoffadeout : ", startoffadeout
	print "accousticness : ", accousticness
	print "dancibility : ", dancibility
	print "energy : ", energy
	print "loudness : ", loudness
	print "instrumentalness : ", instrumentalness
	print "speechness : ", speechness
	print "tempo : ", tempo
	print "valence : ", valence

	'''

	dict = {'artist_familiarity' : {'artist_familiarity':(scipy.stats.pearsonr(artist_familiarity,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(artist_familiarity,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(artist_familiarity,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(artist_familiarity,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(artist_familiarity,startoffadeout)[0]),
									'accousticness':(scipy.stats.pearsonr(artist_familiarity,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(artist_familiarity,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(artist_familiarity,energy)[0]),
									'loudness':(scipy.stats.pearsonr(artist_familiarity,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(artist_familiarity,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(artist_familiarity,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(artist_familiarity,tempo)[0]),
									'valence':(scipy.stats.pearsonr(artist_familiarity,valence)[0])},
			'artist_hotness' : {'artist_familiarity':(scipy.stats.pearsonr(artist_hotness,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(artist_hotness,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(artist_hotness,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(artist_hotness,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(artist_hotness,startoffadeout)[0]),
									'accousticness':(scipy.stats.pearsonr(artist_hotness,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(artist_hotness,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(artist_hotness,energy)[0]),
									'loudness':(scipy.stats.pearsonr(artist_hotness,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(artist_hotness,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(artist_hotness,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(artist_hotness,tempo)[0]),
									'valence':(scipy.stats.pearsonr(artist_hotness,valence)[0])},
			'duration' : {'artist_familiarity':(scipy.stats.pearsonr(duration,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(duration,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(duration,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(duration,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(duration,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(duration,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(duration,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(duration,energy)[0]),
									'loudness':(scipy.stats.pearsonr(duration,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(duration,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(duration,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(duration,tempo)[0]),
									'valence':(scipy.stats.pearsonr(duration,valence)[0])},
			'endoffadein' : {'artist_familiarity':(scipy.stats.pearsonr(endoffadein,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(endoffadein,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(endoffadein,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(endoffadein,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(endoffadein,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(endoffadein,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(endoffadein,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(endoffadein,energy)[0]),
									'loudness':(scipy.stats.pearsonr(endoffadein,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(endoffadein,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(endoffadein,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(endoffadein,tempo)[0]),
									'valence':(scipy.stats.pearsonr(endoffadein,valence)[0])},
			'startoffadeout' : {'artist_familiarity':(scipy.stats.pearsonr(startoffadeout,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(startoffadeout,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(startoffadeout,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(startoffadeout,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(startoffadeout,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(startoffadeout,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(startoffadeout,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(startoffadeout,energy)[0]),
									'loudness':(scipy.stats.pearsonr(startoffadeout,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(startoffadeout,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(startoffadeout,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(startoffadeout,tempo)[0]),
									'valence':(scipy.stats.pearsonr(startoffadeout,valence)[0])},
			'accousticness' : {'artist_familiarity':(scipy.stats.pearsonr(accousticness,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(accousticness,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(accousticness,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(accousticness,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(accousticness,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(accousticness,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(accousticness,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(accousticness,energy)[0]),
									'loudness':(scipy.stats.pearsonr(accousticness,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(accousticness,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(accousticness,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(accousticness,tempo)[0]),
									'valence':(scipy.stats.pearsonr(accousticness,valence)[0])},
			'dancibility' : {'artist_familiarity':(scipy.stats.pearsonr(dancibility,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(dancibility,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(dancibility,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(dancibility,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(dancibility,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(dancibility,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(dancibility,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(dancibility,energy)[0]),
									'loudness':(scipy.stats.pearsonr(dancibility,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(dancibility,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(dancibility,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(dancibility,tempo)[0]),
									'valence':(scipy.stats.pearsonr(dancibility,valence)[0])},
			'energy' : {'artist_familiarity':(scipy.stats.pearsonr(energy,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(energy,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(energy,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(energy,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(energy,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(energy,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(energy,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(energy,energy)[0]),
									'loudness':(scipy.stats.pearsonr(energy,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(energy,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(energy,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(energy,tempo)[0]),
									'valence':(scipy.stats.pearsonr(energy,valence)[0])},
			'loudness' : {'artist_familiarity':(scipy.stats.pearsonr(loudness,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(loudness,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(loudness,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(loudness,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(loudness,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(loudness,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(loudness,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(loudness,energy)[0]),
									'loudness':(scipy.stats.pearsonr(loudness,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(loudness,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(loudness,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(loudness,tempo)[0]),
									'valence':(scipy.stats.pearsonr(loudness,valence)[0])},
			'instrumentalness' : {'artist_familiarity':(scipy.stats.pearsonr(instrumentalness,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(instrumentalness,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(instrumentalness,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(instrumentalness,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(instrumentalness,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(instrumentalness,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(instrumentalness,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(instrumentalness,energy)[0]),
									'loudness':(scipy.stats.pearsonr(instrumentalness,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(instrumentalness,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(instrumentalness,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(instrumentalness,tempo)[0]),
									'valence':(scipy.stats.pearsonr(instrumentalness,valence)[0])},
			'speechness' : {'artist_familiarity':(scipy.stats.pearsonr(speechness,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(speechness,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(speechness,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(speechness,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(speechness,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(speechness,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(speechness,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(speechness,energy)[0]),
									'loudness':(scipy.stats.pearsonr(speechness,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(speechness,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(speechness,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(speechness,tempo)[0]),
									'valence':(scipy.stats.pearsonr(speechness,valence)[0])},
			'tempo' : {'artist_familiarity':(scipy.stats.pearsonr(tempo,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(tempo,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(tempo,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(tempo,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(tempo,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(tempo,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(tempo,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(tempo,energy)[0]),
									'loudness':(scipy.stats.pearsonr(tempo,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(tempo,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(tempo,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(tempo,tempo)[0]),
									'valence':(scipy.stats.pearsonr(tempo,valence)[0])},
			'valence' : {'artist_familiarity':(scipy.stats.pearsonr(valence,artist_familiarity)[0]),
									'artist_hotness':(scipy.stats.pearsonr(valence,artist_hotness)[0]),
									'duration':(scipy.stats.pearsonr(valence,duration)[0]),
									'endoffadein':(scipy.stats.pearsonr(valence,endoffadein)[0]),
									'startoffadeout':(scipy.stats.pearsonr(valence,startoffadeout)[0]),
									'accousticness' :(scipy.stats.pearsonr(valence,accousticness)[0]),
									'dancibility':(scipy.stats.pearsonr(valence,dancibility)[0]),
									'energy':(scipy.stats.pearsonr(valence,energy)[0]),
									'loudness':(scipy.stats.pearsonr(valence,loudness)[0]),
									'instrumentalness':(scipy.stats.pearsonr(valence,instrumentalness)[0]),
									'speechness':(scipy.stats.pearsonr(valence,speechness)[0]),
									'tempo':(scipy.stats.pearsonr(valence,tempo)[0]),
									'valence':(scipy.stats.pearsonr(valence,valence)[0])}}
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

def variation(attributes1, attributes2):
	output = []
	i = 0

	for j in range(0, (len(attributes1[0]))):
		v0 = abs((attributes1[0].__getitem__(j) - attributes2[0].__getitem__(j)))
		v0 = v0/abs((attributes1[0].__getitem__(j)))
		output.append(v0)

	return output
	
def difference(attributes, attributes2):
	output = []

	for j in range(0, (len(attributes[0]))):
		v = abs((attributes[0].__getitem__(j) - attributes2[0].__getitem__(j)))
		output.append(v)

	return output
def findAverage(playlist):
	
	dancibility = []
	energy = []
	loudness = []
	accousticness = []
	instrumentalness = []
	speechness = []
	tempo = []
	valence = []

	for i in range(0, (len(playlist[0]))):
		for j in range(0, (len(playlist))):
			if i == 0:
				dancibility.append(playlist[j].__getitem__(i))
			if i == 1:
				energy.append(playlist[j].__getitem__(i))
			if i == 2:
				loudness.append(playlist[j].__getitem__(i))
			if i == 3:
				accousticness.append(playlist[j].__getitem__(i))
			if i == 4:
				instrumentalness.append(playlist[j].__getitem__(i))
			if i == 5:
				speechness.append(playlist[j].__getitem__(i))
			if i == 6:
				tempo.append(playlist[j].__getitem__(i))
			if i == 7:
				valence.append(playlist[j].__getitem__(i))
	output = []
	output.append((np.mean(dancibility), np.mean(energy), np.mean(loudness), np.mean(accousticness), np.mean(instrumentalness), np.mean(speechness), np.mean(tempo), np.mean(valence)))
	return output

agg1 = []
agg2 = []
agg3 = []
agg4 = []
agg5 = []
agg6 = []
agg7 = []
agg8 = []
agg9 = []
agg10 = []
country_attributes = []
sleep_attributes = []
coffee_attributes = []
sleep2_attributes = []
lastfitness_attributes = []

for song in range(0, (len(p.playlist_song_names)-1)):
	agg1.append((p.playlist_dancibility[song], p.playlist_energy[song], p.playlist_loudness[song], p.playlist_accousticness[song], p.playlist_instrumentalness[song], p.playlist_speechness[song], p.playlist_tempo[song], p.playlist_valence[song]))
for song in range(0, (len(p2.playlist_song_names)-1)):
	agg2.append((p2.playlist_dancibility[song], p2.playlist_energy[song], p2.playlist_loudness[song], p2.playlist_accousticness[song], p2.playlist_instrumentalness[song], p2.playlist_speechness[song], p2.playlist_tempo[song], p2.playlist_valence[song]))
for song in range(0, (len(p3.playlist_song_names)-1)):
	agg3.append((p3.playlist_dancibility[song], p3.playlist_energy[song], p3.playlist_loudness[song], p3.playlist_accousticness[song], p3.playlist_instrumentalness[song], p3.playlist_speechness[song], p3.playlist_tempo[song], p3.playlist_valence[song]))
for song in range(0, (len(p4.playlist_song_names)-1)):
	agg4.append((p4.playlist_dancibility[song], p4.playlist_energy[song], p4.playlist_loudness[song], p4.playlist_accousticness[song], p4.playlist_instrumentalness[song], p4.playlist_speechness[song], p4.playlist_tempo[song], p4.playlist_valence[song]))
#for song in range(0, (len(p5.playlist_song_names)-1)):
#	agg5.append((p5.playlist_dancibility[song], p5.playlist_energy[song], p5.playlist_loudness[song], p5.playlist_accousticness[song], p5.playlist_instrumentalness[song], p5.playlist_speechness[song], p5.playlist_tempo[song], p5.playlist_valence[song]))
for song in range(0, (len(p6.playlist_song_names)-1)):
	agg6.append((p6.playlist_dancibility[song], p6.playlist_energy[song], p6.playlist_loudness[song], p6.playlist_accousticness[song], p6.playlist_instrumentalness[song], p6.playlist_speechness[song], p6.playlist_tempo[song], p6.playlist_valence[song]))
for song in range(0, (len(p7.playlist_song_names)-1)):
	agg7.append((p7.playlist_dancibility[song], p7.playlist_energy[song], p7.playlist_loudness[song], p7.playlist_accousticness[song], p7.playlist_instrumentalness[song], p7.playlist_speechness[song], p7.playlist_tempo[song], p7.playlist_valence[song]))
for song in range(0, (len(p8.playlist_song_names)-1)):
	agg8.append((p8.playlist_dancibility[song], p8.playlist_energy[song], p8.playlist_loudness[song], p8.playlist_accousticness[song], p8.playlist_instrumentalness[song], p8.playlist_speechness[song], p8.playlist_tempo[song], p8.playlist_valence[song]))
#for song in range(0, (len(p9.playlist_song_names)-1)):
#	agg9.append((p9.playlist_dancibility[song], p9.playlist_energy[song], p9.playlist_loudness[song], p9.playlist_accousticness[song], p9.playlist_instrumentalness[song], p9.playlist_speechness[song], p9.playlist_tempo[song], p9.playlist_valence[song]))
for song in range(0, (len(p10.playlist_song_names)-1)):
	agg10.append((p10.playlist_dancibility[song], p10.playlist_energy[song], p10.playlist_loudness[song], p10.playlist_accousticness[song], p10.playlist_instrumentalness[song], p10.playlist_speechness[song], p10.playlist_tempo[song], p10.playlist_valence[song]))

for song in range(0, (len(smoothjazz.playlist_song_names)-1)):
	smoothjazz_attributes.append((smoothjazz.playlist_dancibility[song], smoothjazz.playlist_energy[song], smoothjazz.playlist_loudness[song], smoothjazz.playlist_accousticness[song], smoothjazz.playlist_instrumentalness[song], smoothjazz.playlist_speechness[song], smoothjazz.playlist_tempo[song], smoothjazz.playlist_valence[song]))


for song in range(0, (len(country.playlist_song_names)-1)):
	country_attributes.append((country.playlist_dancibility[song], country.playlist_energy[song], country.playlist_loudness[song], country.playlist_accousticness[song], country.playlist_instrumentalness[song], country.playlist_speechness[song], country.playlist_tempo[song], country.playlist_valence[song]))


for song in range(0, (len(coffee.playlist_song_names)-1)):
	coffee_attributes.append((coffee.playlist_dancibility[song], coffee.playlist_energy[song], coffee.playlist_loudness[song], coffee.playlist_accousticness[song], coffee.playlist_instrumentalness[song], coffee.playlist_speechness[song], coffee.playlist_tempo[song], coffee.playlist_valence[song]))

for song in range(0, (len(sleep2.playlist_song_names)-1)):
	sleep2_attributes.append((sleep2.playlist_dancibility[song], sleep2.playlist_energy[song], sleep2.playlist_loudness[song], sleep2.playlist_accousticness[song], sleep2.playlist_instrumentalness[song], sleep2.playlist_speechness[song], sleep2.playlist_tempo[song], sleep2.playlist_valence[song]))

for song in range(0, (len(lastfitness.playlist_song_names)-1)):
	lastfitness_attributes.append((lastfitness.playlist_dancibility[song], lastfitness.playlist_energy[song], lastfitness.playlist_loudness[song], lastfitness.playlist_accousticness[song], lastfitness.playlist_instrumentalness[song], lastfitness.playlist_speechness[song], lastfitness.playlist_tempo[song], lastfitness.playlist_valence[song]))


agg = []
agg = agg1 + agg2 + agg3 + agg4 + agg6 + agg7 + agg8 + agg10

'''
print "Fitness Song Average : ", findAverage(agg)
print "\n"
print "Smooth Jazz Average : ", findAverage(smoothjazz_attributes)
print "\n"
print "Country Song Average : ", findAverage(country_attributes)
print "\n"
print "Coffee Song Average : ", findAverage(coffee_attributes)
print "\n"
print "Sleep 2 Song Average : ", findAverage(sleep2_attributes)
print "\n"
'''

averageoffitness = findAverage(agg)
averageofsmoothjazz = findAverage(smoothjazz_attributes)
averageofcountry = findAverage(country_attributes)
averageofcoffee = findAverage(coffee_attributes)
averageofsleep2 = findAverage(sleep2_attributes)
averageoflastfitness = findAverage(lastfitness_attributes)


print "Variation Fitness and Smooth Jazz: ", variation(averageoflastfitness, averageofsmoothjazz)
print "\n"
print "Variation Fitness and Country", variation(averageoflastfitness, averageofcountry)
print "\n"
print "Variation Fitness and Coffee", variation(averageoflastfitness, averageofcoffee)
print "\n"
print "Variation Fitness and Sleep 2", variation(averageoflastfitness, averageofsleep2)


#song_data = query_spotify_for_attributes()
#correlation_data = pearson_correlation_data(song_data)

#openfile = open("correlation2.txt", "w+")
#openfile.write(str(pearsonCorrelation2(correlation_data)))
#openfile = open(str(playlistname), "w+")
#openfile.write(str(pearsonCorrelation2(correlation_data)))
