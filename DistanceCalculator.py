import numpy as np
from operator import itemgetter
from sklearn.cluster import KMeans
import scipy
from scipy.stats.stats import pearsonr
from Playlist import Playlist
from dataset_processing import *
import pickle

# FITNESS
with open('Fitness.txt') as f:
    Fitness = f.readlines()
Fitness_Playlist_Object = []
Fitness_attributes = []
for x in range(0, len(Fitness)-1):
	Fitness1 = Playlist('spotify', Fitness[x][:-1])
	Fitness1.get_playlist()
	Fitness_Playlist_Object.append(Fitness1)
	for song in range(0, (len(Fitness1.playlist_song_names))-1):
		Fitness_attributes.append((Fitness1.playlist_dancibility[song], Fitness1.playlist_energy[song], Fitness1.playlist_loudness[song], Fitness1.playlist_accousticness[song], Fitness1.playlist_instrumentalness[song], Fitness1.playlist_speechness[song], Fitness1.playlist_tempo[song], Fitness1.playlist_valence[song]))
f.close()

openfile = open("Fitness_Playlist_Object.txt", "wb")
pickle.dump(Fitness_Playlist_Object, openfile)
openfile.close()


# ELECTRONIC
Electronic = []
Electronic_Playlist_Object = []
Electronic_attributes = []
with open('Electronic.txt') as f:
    Electronic = f.readlines()
for x in range(0, len(Electronic)-1):
	print "Electronic : ", x, " ", Electronic[x]
	Electronic1 = Playlist('spotify', Electronic[x][:-1])
	Electronic1.get_playlist()
	for song in range(0, (len(Electronic1.playlist_song_names))-1):
		Electronic_attributes.append((Electronic1.playlist_dancibility[song], Electronic1.playlist_energy[song], Electronic1.playlist_loudness[song], Electronic1.playlist_accousticness[song], Electronic1.playlist_instrumentalness[song], Electronic1.playlist_speechness[song], Electronic1.playlist_tempo[song], Electronic1.playlist_valence[song]))
	Electronic_Playlist_Object.append(Electronic1)
	print "Done"
f.close()

openfile = open("Electronic_Playlist_Object.txt", "wb")
pickle.dump(Electronic_Playlist_Object, openfile)
openfile.close()

# HIPHOP
with open('HipHop.txt') as f:
    HipHop = f.readlines()
HipHop_Playlist_Object = []
for x in range(0, len(HipHop)):
	HipHop1 = Playlist('spotify', HipHop[x][:-1])
	HipHop1.get_playlist()
	HipHop_Playlist_Object.append(HipHop1)
f.close()

openfile = open("HipHop_Playlist_Object.txt", "wb")
pickle.dump(HipHop_Playlist_Object, openfile)
openfile.close()

# POP
with open('Pop.txt') as f:
    Pop = f.readlines()
Pop_Playlist_Object = []
for x in range(0, len(Pop)):
	globals()['Pop%s' % x] = Playlist('spotify', Pop[x][:-1])
	globals()['Pop%s' % x].get_playlist()
	Pop_Playlist_Object.append(globals()['Pop%s' % x])
f.close()

openfile = open("Pop_Playlist_Object.txt", "wb")
pickle.dump(Pop_Playlist_Object, openfile)
openfile.close()

# MOOD
with open('Mood.txt') as f:
    Mood = f.readlines()
Mood_Playlist_Object = []
for x in range(0, len(Mood)):
	globals()['Mood%s' % x] = Playlist('spotify', Mood[x][:-1])
	globals()['Mood%s' % x].get_playlist()
	Mood_Playlist_Object.append(globals()['Mood%s' % x])
f.close()

openfile = open("Mood_Playlist_Object.txt", "wb")
pickle.dump(Mood_Playlist_Object, openfile)
openfile.close()

# CHILL
with open('Chill.txt') as f:
    Chill = f.readlines()
Chill_Playlist_Object = []
for x in range(0, len(Chill)):
	globals()['Chill%s' % x] = Playlist('spotify', Chill[x][:-1])
	globals()['Chill%s' % x].get_playlist()
	Chill_Playlist_Object.append(globals()['Chill%s' % x])
f.close()

openfile = open("Chill_Playlist_Object.txt", "wb")
pickle.dump(Chill_Playlist_Object, openfile)
openfile.close()

# COUNTRY
with open('Country.txt') as f:
    Country = f.readlines()
Country_Playlist_Object = []
for x in range(0, len(Country)):
	globals()['Country%s' % x] = Playlist('spotify', Country[x][:-1])
	globals()['Country%s' % x].get_playlist()
	Country_Playlist_Object.append(globals()['Country%s' % x])
f.close()

openfile = open("Country_Playlist_Object.txt", "wb")
pickle.dump(Country_Playlist_Object, openfile)
openfile.close()

# R&B
with open('R_B.txt') as f:
    R_B = f.readlines()
R_B_Playlist_Object = []
for x in range(0, len(R_B)):
	globals()['R_B%s' % x] = Playlist('spotify', R_B[x][:-1])
	globals()['R_B%s' % x].get_playlist()
	R_B_Playlist_Object.append(globals()['R_B%s' % x])
f.close()

openfile = open("R_B_Playlist_Object.txt", "wb")
pickle.dump(R_B_Playlist_Object, openfile)
openfile.close()

# FOCUS
with open('Focus.txt') as f:
    Focus = f.readlines()
Focus_Playlist_Object = []
for x in range(0, len(Focus)):
	globals()['Focus%s' % x] = Playlist('spotify', Focus[x][:-1])
	globals()['Focus%s' % x].get_playlist()
	Focus_Playlist_Object.append(globals()['Focus%s' % x])
f.close()

openfile = open("Focus_Playlist_Object.txt", "wb")
pickle.dump(Focus_Playlist_Object, openfile)
openfile.close()

# PARTY
with open('Party.txt') as f:
    Party = f.readlines()
Party_Playlist_Object = []
for x in range(0, len(Party)):
	globals()['Party%s' % x] = Playlist('spotify', Party[x][:-1])
	globals()['Party%s' % x].get_playlist()
	Party_Playlist_Object.append(globals()['Party%s' % x])
f.close()

openfile = open("Party_Playlist_Object.txt", "wb")
pickle.dump(Party_Playlist_Object, openfile)
openfile.close()

# ROCK
with open('Rock.txt') as f:
    Rock = f.readlines()
Rock_Playlist_Object = []
for x in range(0, len(Rock)):
	globals()['Rock%s' % x] = Playlist('spotify', Rock[x][:-1])
	globals()['Rock%s' % x].get_playlist()
	Rock_Playlist_Object.append(globals()['Rock%s' % x])
f.close()

openfile = open("Rock_Playlist_Object.txt", "wb")
pickle.dump(Rock_Playlist_Object, openfile)
openfile.close()

# INDIE
with open('Indie.txt') as f:
    Indie = f.readlines()
Indie_Playlist_Object = []
for x in range(0, len(Indie)):
	globals()['Indie%s' % x] = Playlist('spotify', Indie[x][:-1])
	globals()['Indie%s' % x].get_playlist()
	Indie_Playlist_Object.append(globals()['Indie%s' % x])
f.close()

openfile = open("Indie_Playlist_Object.txt", "wb")
pickle.dump(Indie_Playlist_Object, openfile)
openfile.close()

# SLEEP
with open('Sleep.txt') as f:
    Sleep = f.readlines()
Sleep_Playlist_Object = []
for x in range(0, len(Sleep)):
	globals()['Sleep%s' % x] = Playlist('spotify', Sleep[x][:-1])
	globals()['Sleep%s' % x].get_playlist()
	Sleep_Playlist_Object.append(globals()['Sleep%s' % x])
f.close()

openfile = open("Sleep_Playlist_Object.txt", "wb")
pickle.dump(Sleep_Playlist_Object, openfile)
openfile.close()

# JAZZ
with open('Jazz.txt') as f:
    Jazz = f.readlines()
Jazz_Playlist_Object = []
for x in range(0, len(Jazz)):
	globals()['Jazz%s' % x] = Playlist('spotify', Jazz[x][:-1])
	globals()['Jazz%s' % x].get_playlist()
	Jazz_Playlist_Object.append(globals()['Jazz%s' % x])
f.close()

openfile = open("Jazz_Playlist_Object.txt", "wb")
pickle.dump(Jazz_Playlist_Object, openfile)
openfile.close()

# CLASSICAL
with open('Classical.txt') as f:
    Classical = f.readlines()
Classical_Playlist_Object = []
for x in range(0, len(Classical)):
	globals()['Classical%s' % x] = Playlist('spotify', Classical[x][:-1])
	globals()['Classical%s' % x].get_playlist()
	Classical_Playlist_Object.append(globals()['Classical%s' % x])
f.close()

openfile = open("Classical_Playlist_Object.txt", "wb")
pickle.dump(Classical_Playlist_Object, openfile)
openfile.close()

# ROMANCE
with open('Romance.txt') as f:
    Romance = f.readlines()
Romance_Playlist_Object = []
for x in range(0, len(Romance)):
	globals()['Romance%s' % x] = Playlist('spotify', Romance[x][:-1])
	globals()['Romance%s' % x].get_playlist()
	Romance_Playlist_Object.append(globals()['Romance%s' % x])
f.close()

openfile = open("Romance_Playlist_Object.txt", "wb")
pickle.dump(Romance_Playlist_Object, openfile)
openfile.close()

# METAL
with open('Metal.txt') as f:
    Metal = f.readlines()
Metal_Playlist_Object = []
for x in range(0, len(Metal)):
	globals()['Metal%s' % x] = Playlist('spotify', Metal[x][:-1])
	globals()['Metal%s' % x].get_playlist()
	Metal_Playlist_Object.append(globals()['Metal%s' % x])
f.close()

openfile = open("Metal_Playlist_Object.txt", "wb")
pickle.dump(Metal_Playlist_Object, openfile)
openfile.close()

# RAGGAE
with open('Raggae.txt') as f:
    Raggae = f.readlines()
Raggae_Playlist_Object = []
for x in range(0, len(Raggae)):
	globals()['Raggae%s' % x] = Playlist('spotify', Raggae[x][:-1])
	globals()['Raggae%s' % x].get_playlist()
	Raggae_Playlist_Object.append(globals()['Raggae%s' % x])
f.close()

openfile = open("Raggae_Playlist_Object.txt", "wb")
pickle.dump(Raggae_Playlist_Object, openfile)
openfile.close()

# DINNER
with open('Dinner.txt') as f:
    Dinner = f.readlines()
Dinner_Playlist_Object = []
for x in range(0, len(Dinner)):
	globals()['Dinner%s' % x] = Playlist('spotify', Dinner[x][:-1])
	globals()['Dinner%s' % x].get_playlist()
	Dinner_Playlist_Object.append(globals()['Dinner%s' % x])
f.close()

openfile = open("Dinner_Playlist_Object.txt", "wb")
pickle.dump(Dinner_Playlist_Object, openfile)
openfile.close()

# SOUL
with open('Soul.txt') as f:
    Soul = f.readlines()
Soul_Playlist_Object = []
for x in range(0, len(Soul)):
	globals()['Soul%s' % x] = Playlist('spotify', Soul[x][:-1])
	globals()['Soul%s' % x].get_playlist()
	Soul_Playlist_Object.append(globals()['Soul%s' % x])
f.close()

openfile = open("Soul_Playlist_Object.txt", "wb")
pickle.dump(Soul_Playlist_Object, openfile)
openfile.close()

# BLUES
with open('Blues.txt') as f:
    Blues = f.readlines()
Blues_Playlist_Object = []
for x in range(0, len(Blues)):
	globals()['Blues%s' % x] = Playlist('spotify', Blues[x][:-1])
	globals()['Blues%s' % x].get_playlist()
	Blues_Playlist_Object.append(globals()['Blues%s' % x])
f.close()

openfile = open("Blues_Playlist_Object.txt", "wb")
pickle.dump(Blues_Playlist_Object, openfile)
openfile.close()

# PUNK
with open('Punk.txt') as f:
    Punk = f.readlines()
Punk_Playlist_Object = []
for x in range(0, len(Punk)):
	globals()['Punk%s' % x] = Playlist('spotify', Punk[x][:-1])
	globals()['Punk%s' % x].get_playlist()
	Punk_Playlist_Object.append(globals()['Punk%s' % x])
f.close()

openfile = open("Punk_Playlist_Object.txt", "wb")
pickle.dump(Punk_Playlist_Object, openfile)
openfile.close()

# FAMILY
with open('Family.txt') as f:
    Family = f.readlines()
Family_Playlist_Object = []
for x in range(0, len(Family)):
	globals()['Family%s' % x] = Playlist('spotify', Family[x][:-1])
	globals()['Family%s' % x].get_playlist()
	Family_Playlist_Object.append(globals()['Family%s' % x])
f.close()

openfile = open("Family_Playlist_Object.txt", "wb")
pickle.dump(Family_Playlist_Object, openfile)
openfile.close()

# GAMING
with open('Gaming.txt') as f:
    Gaming = f.readlines()
Gaming_Playlist_Object = []
for x in range(0, len(Gaming)):
	globals()['Gaming%s' % x] = Playlist('spotify', Gaming[x][:-1])
	globals()['Gaming%s' % x].get_playlist()
	Gaming_Playlist_Object.append(globals()['Gaming%s' % x])
f.close()

openfile = open("Gaming_Playlist_Object.txt", "wb")
pickle.dump(Gaming_Playlist_Object, openfile)
openfile.close()
'''


# Takes in a list of one tuple containing average/aggregate song attributes 
# and a list of tupples containing centroids
# the ouptut is a list of one list containing the index of the closest centroid
# from the input file and the eucledian distance
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

# Takes in a list of one tuple containing average/aggregate song attributes 
# and a list of tuples containing song attributes and n for n number of closest songs
# the ouptut is a list of one tuple containing the index of the closest n songs
# based on eucledean distance
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

# USE ONLY FOR 8 attributes - USE next function below for 13 attributes
# Takes in a list of tuples containing song attributes
# and calculates the pearson r correlation for each attribute
# outputs a dictionary for each attribute containing the correlation
# for every other attribute 
def pearsonCorrelationDict(p):
	numOfElements = (len(songAttributes))
	sizeOfElement = (len(songAttributes[0]))
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
				Speechness.append(song_attributes[j].__getitem__(i))
			if i == 6:
				Tempo.append(song_attributes[j].__getitem__(i))
			if i == 7:
				Valence.append(song_attributes[j].__getitem__(i))

	dict = {'Dancibility' : {'Energy':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_energy)[0]), 'Loudness':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_loudness)[0]), 'Accousticness' :(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_dancibility,p.playlist_valence)[0])},
			'Energy' : {'Danceability':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_dancibility)[0]), 'Loudness':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_loudness)[0]), 'Accousticness' :(scipy.stats.pearsonr(p.playlist_energy,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_energy,p.playlist_valence)[0])},
			'Loudness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_energy)[0]), 'Accousticness' :(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_loudness,p.playlist_valence)[0])},
			'Accousticness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_loudness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_accousticness,p.playlist_valence)[0])},
			'Instrumentalness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_accousticness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_instrumentalness,p.playlist_valence)[0])},
			'Speechness' : {'Danceability':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_instrumentalness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_tempo)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_speechness,p.playlist_valence)[0])},
			'Tempo' : {'Danceability':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_speechness)[0]), 'Valence':(scipy.stats.pearsonr(p.playlist_tempo,p.playlist_valence)[0])},
			'Valence' : {'Danceability':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_dancibility)[0]), 'Energy':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_energy)[0]), 'Loudness' :(scipy.stats.pearsonr(p.playlist_valence,p.playlist_loudness)[0]), 'Accousticness':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_accousticness)[0]), 'Instrumentalness':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_instrumentalness)[0]), 'Speechness':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_speechness)[0]), 'Tempo':(scipy.stats.pearsonr(p.playlist_valence,p.playlist_tempo)[0])}}

	return dict

# same things as the above function but for 13 attributes
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

# calculates the correlation using the 8 attributes
# and write the outputs to a local directory
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

# Extra function that calculates variation between two lists of tuples
def variation(attributes1, attributes2):
	output = []
	i = 0

	for j in range(0, (len(attributes1[0]))):
		v0 = abs((attributes1[0].__getitem__(j) - attributes2[0].__getitem__(j)))
		v0 = v0/abs((attributes1[0].__getitem__(j)))
		output.append(v0)

	return output

# Calculates the difference between two lists of one tuple containing the aggregate vector
def difference(attributes, attributes2, Genre):
	output = []

	for j in range(0, (len(attributes[0]))):
		v = abs((attributes[0].__getitem__(j) - attributes2[0].__getitem__(j)))
		output.append(v)

	for x in range(0,(len(output))):
		if x == 0:
			dancibility = output[x]
		if x == 1:
			energy = output[x]
		if x == 2:
			loudness = output[x]
		if x == 3:
			accousticness = output[x]
		if x == 4:
			instrumentalness = output[x]
		if x == 5:
			speechness = output[x]
		if x == 6:
			tempo = output[x]
		if x == 7:
			valence = output[x]

	dict = { Genre : {'dancibility': dancibility, 'energy': energy, 'loudness': loudness, 'accousticness': accousticness, 'instrumentalness': instrumentalness, 'speechness': speechness, 'tempo': tempo, 'valence': valence}}

	return dict

# Finds the aggregate vector by taking in a list of tuples containing song attributes
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
				if((playlist[j].__getitem__(i)) != 0):
					dancibility.append(playlist[j].__getitem__(i))
			if i == 1:
				if((playlist[j].__getitem__(i)) != 0):
					energy.append(playlist[j].__getitem__(i))
			if i == 2:
				if((playlist[j].__getitem__(i)) != 0):
					loudness.append(playlist[j].__getitem__(i))
			if i == 3:
				if((playlist[j].__getitem__(i)) != 0):
					accousticness.append(playlist[j].__getitem__(i))
			if i == 4:
				if((playlist[j].__getitem__(i)) != 0):
					instrumentalness.append(playlist[j].__getitem__(i))
			if i == 5:
				if((playlist[j].__getitem__(i)) != 0):
					speechness.append(playlist[j].__getitem__(i))
			if i == 6:
				if((playlist[j].__getitem__(i)) != 0):
					tempo.append(playlist[j].__getitem__(i))
			if i == 7:
				if((playlist[j].__getitem__(i)) != 0):
					valence.append(playlist[j].__getitem__(i))

	output = []
	output.append((np.mean(dancibility), np.mean(energy), np.mean(loudness), np.mean(accousticness), np.mean(instrumentalness), np.mean(speechness), np.mean(tempo), np.mean(valence)))
	return output

# Normalizes a list of tuples containing playlist songs attributes
def normalize(playlist):
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

	mindanceability = min(dancibility)
	maxdanceability = max(dancibility)
	minenergy = min(energy)
	maxenergy = max(energy)
	minloudness = min(loudness)
	maxloudness = max(loudness)
	minaccousticness = min(accousticness)
	maxaccousticness = max(accousticness)
	mininstrumentalness = min(instrumentalness)
	maxinstrumentalness = max(instrumentalness)
	minspeechness = min(speechness)
	maxspeechness = max(speechness)
	mintempo = min(tempo)
	maxtempo = max(tempo)
	minvalence = min(valence)
	maxvalence = max(valence)
	dancibility = []
	energy = []
	loudness = []
	accousticness = []
	instrumentalness = []
	speechness = []
	tempo = []
	valence = []
	output = []
	for i in range(0, (len(playlist[0]))):
		for j in range(0, (len(playlist))):
			if i == 0:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-mindanceability)/(maxdanceability-mindanceability)
					if(v == 0):
						dancibility.append(0.00001)
					else:
						dancibility.append(v)
				else:
					dancibility.append(0)
			if i == 1:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-minenergy)/(maxenergy-minenergy)
					if(v == 0):
						energy.append(0.00001)
					else:
						energy.append(v)
				else:
					energy.append(0)
			if i == 2:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-minloudness)/(maxloudness-minloudness)
					if(v == 0):
						loudness.append(0.00001)
					else:
						loudness.append(v)
				else:
					loudness.append(0)
			if i == 3:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-minaccousticness)/(maxaccousticness-minaccousticness)
					if(v == 0):
						accousticness.append(0.00001)
					else:
						accousticness.append(v)
				else:
					accousticness.append(0)
			if i == 4:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-mininstrumentalness)/(maxinstrumentalness-mininstrumentalness)
					if(v == 0):
						instrumentalness.append(0.00001)
					else:
						instrumentalness.append(v)
				else:
					instrumentalness.append(0)
			if i == 5:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-minspeechness)/(maxspeechness-minspeechness)
					if(v == 0):
						speechness.append(0.00001)
					else:
						speechness.append(v)
				else:
					speechness.append(0)
			if i == 6:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-mintempo)/(maxtempo-mintempo)
					if(v == 0):
						tempo.append(0.00001)
					else:
						tempo.append(v)
				else:
					tempo.append(0)
			if i == 7:
				if ((playlist[j].__getitem__(i)) != 0):
					v = ((playlist[j].__getitem__(i))-minvalence)/(maxvalence-minvalence)
					if(v == 0):
						valence.append(0.00001)
					else:
						valence.append(v)
				else:
					valence.append(0)

	output = []
	for i in range(0,(len(dancibility))):
		output.append((dancibility[i], energy[i], loudness[i], accousticness[i], instrumentalness[i], speechness[i], tempo[i], valence[i]))

	return output

'''
Fitness_attributes = []
for playlist in Fitness_Playlist_Object:
	currentplaylist = playlist.get_playlist()
	for song in range(0,(len(playlist.playlist_song_names))-1):
		Fitness_attributes.append((currentplaylist.playlist_dancibility[song], currentplaylist.playlist_energy[song], currentplaylist.playlist_loudness[song], currentplaylist.playlist_accousticness[song], currentplaylist.playlist_instrumentalness[song], currentplaylist.playlist_speechness[song], currentplaylist.playlist_tempo[song], currentplaylist.playlist_valence[song]))

print Fitness_attributes


Fitness_attributes = []
for playlist in range(0, len(Fitness_Playlist_Object)-1):
	print "Playlist : ", playlist
	for song in range(0, len(Fitness_Playlist_Object[playlist].playlist_song_names)):
		if Fitness_Playlist_Object[playlist].playlist_song_names is not None:
			Fitness_attributes.append((Fitness_Playlist_Object[playlist].playlist_dancibility[song], Fitness_Playlist_Object[playlist].playlist_energy[song], Fitness_Playlist_Object[playlist].playlist_loudness[song], Fitness_Playlist_Object[playlist].playlist_accousticness[song], Fitness_Playlist_Object[playlist].playlist_instrumentalness[song], Fitness_Playlist_Object[playlist].playlist_speechness[song], Fitness_Playlist_Object[playlist].playlist_tempo[song], Fitness_Playlist_Object[playlist].playlist_valence[song]))

print Fitness_attributes

Electronic_attributes = []
for playlist in range(0, len(Electronic_Playlist_Object)-1):
	for song in range(0, len(Electronic_Playlist_Object[playlist].playlist_song_names)):
		Electronic_attributes.append((Electronic_Playlist_Object[playlist].playlist_dancibility[song], Electronic_Playlist_Object[playlist].playlist_energy[song], Electronic_Playlist_Object[playlist].playlist_loudness[song], Electronic_Playlist_Object[playlist].playlist_accousticness[song], Electronic_Playlist_Object[playlist].playlist_instrumentalness[song], Electronic_Playlist_Object[playlist].playlist_speechness[song], Electronic_Playlist_Object[playlist].playlist_tempo[song], Electronic_Playlist_Object[playlist].playlist_valence[song]))

print Fitness_attributes





Electronic_attributes = []
for playlist in Electronic_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(0, len(playlist.playlist_song_names)):
			print song
			Electronic_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

HipHop_attributes = []
for playlist in HipHop_Playlist_Object-1:
	if playlist.playlist_song_names is not None:
		print "LENGTH", len(playlist.playlist_song_names)-1
		for song in range(0, len(playlist.playlist_song_names)-1):
			print "SONG", song
			HipHop_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

HipHop_attributes = []
for playlist in range(0,HipHop_Playlist_Object):
	currentplaylist = HipHop_Playlist_Object[playlist]
	for song in range(0,currentplaylist.playlist_song_names-1):
		print "Song :", song




Pop_attributes = []
for playlist in Pop_Playlist_Object-1:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-4):
			Pop_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Mood_attributes = []
for playlist in Mood_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Mood_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Chill_attributes = []
for playlist in Chill_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Chill_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Country_attributes = []
for playlist in Country_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Country_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

R_B_attributes = []
for playlist in R_B_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			R_B_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Focus_attributes = []
for playlist in Focus_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Focus_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Party_attributes = []
for playlist in Party_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Party_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Rock_attributes = []
for playlist in Rock_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Rock_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Indie_attributes = []
for playlist in Indie_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Indie_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Sleep_attributes = []
for playlist in Sleep_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Sleep_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Jazz_attributes = []
for playlist in Jazz_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Jazz_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Classical_attributes = []
for playlist in Classical_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Classical_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Romance_attributes = []
for playlist in Romance_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Romance_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Metal_attributes = []
for playlist in Metal_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Metal_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Raggae_attributes = []
for playlist in Raggae_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Raggae_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Dinner_attributes = []
for playlist in Dinner_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Dinner_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Soul_attributes = []
for playlist in Soul_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Soul_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Blues_attributes = []
for playlist in Blues_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Blues_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Punk_attributes = []
for playlist in Punk_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Punk_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Family_attributes = []
for playlist in Family_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Family_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))

Gaming_attributes = []
for playlist in Gaming_Playlist_Object:
	if playlist.playlist_song_names is not None:
		print len(playlist.playlist_song_names)
		for song in range(len(playlist.playlist_song_names)-1):
			Gaming_attributes.append((playlist.playlist_dancibility[song], playlist.playlist_energy[song], playlist.playlist_loudness[song], playlist.playlist_accousticness[song], playlist.playlist_instrumentalness[song], playlist.playlist_speechness[song], playlist.playlist_tempo[song], playlist.playlist_valence[song]))


'''
normalized_Fitness = normalize(Fitness_attributes)
Fitness_aggregate = findAverage(normalized_Fitness)

normalized_Electronic = normalize(Electronic_attributes)
Electronic_aggregate = findAverage(normalized_Electronic)
'''
normalized_HipHop = normalize(HipHop_attributes)
HipHop_aggregate = findAverage(normalized_HipHop)

normalized_Pop = normalize(Pop_attributes)
Pop_aggregate = findAverage(normalized_Pop)

normalized_Mood = normalize(Mood_attributes)
Mood_aggregate = findAverage(normalized_Mood)

normalized_Chill = normalize(Chill_attributes)
Chill_aggregate = findAverage(normalized_Chill)

normalized_Country = normalize(Country_attributes)
Country_aggregate = findAverage(normalized_Country)

normalized_R_B = normalize(R_B_attributes)
R_B_aggregate = findAverage(normalized_R_B)

normalized_Focus = normalize(Focus_attributes)
Focus_aggregate = findAverage(normalized_Focus)

normalized_Party = normalize(Party_attributes)
Party_aggregate = findAverage(normalized_Party)

normalized_Rock = normalize(Rock_attributes)
Rock_aggregate = findAverage(normalized_Rock)

normalized_Indie = normalize(Indie_attributes)
Indie_aggregate = findAverage(normalized_Indie)

normalized_Sleep = normalize(Sleep_attributes)
Sleep_aggregate = findAverage(normalized_Sleep)

normalized_Jazz = normalize(Jazz_attributes)
Jazz_aggregate = findAverage(normalized_Jazz)

normalized_Classical = normalize(Classical_attributes)
Classical_aggregate = findAverage(normalized_Classical)

normalized_Romance = normalize(Romance_attributes)
Romance_aggregate = findAverage(normalized_Romance)

normalized_Metal = normalize(Metal_attributes)
Metal_aggregate = findAverage(normalized_Metal)

normalized_Raggae = normalize(Raggae_attributes)
Raggae_aggregate = findAverage(normalized_Raggae)

normalized_Dinner = normalize(Dinner_attributes)
Dinner_aggregate = findAverage(normalized_Dinner)

normalized_Soul = normalize(Soul_attributes)
Soul_aggregate = findAverage(normalized_Soul)

normalized_Blues = normalize(Blues_attributes)
Blues_aggregate = findAverage(normalized_Blues)

normalized_Punk = normalize(Punk_attributes)
Punk_aggregate = findAverage(normalized_Punk)

normalized_Family = normalize(Family_attributes)
Family_aggregate = findAverage(normalized_Family)

normalized_Gaming = normalize(Gaming_attributes)
Gaming_aggregate = findAverage(normalized_Gaming)

'''
print difference(Fitness_aggregate, Electronic_aggregate, 'Electronic')
print "\n"
'''
print difference(Fitness_aggregate, HipHop_aggregate, 'HipHop')
print "\n"
print difference(Fitness_aggregate, Pop_aggregate, 'Pop')
print "\n"
print difference(Fitness_aggregate, Mood_aggregate, 'Mood')
print "\n"
print difference(Fitness_aggregate, Chill_aggregate, 'Chill')
print "\n"
print difference(Fitness_aggregate, Country_aggregate, 'Country')
print "\n"
print difference(Fitness_aggregate, R_B_aggregate, 'R_B')
print "\n"
print difference(Fitness_aggregate, Focus_aggregate, 'Focus')
print "\n"
print difference(Fitness_aggregate, Party_aggregate, 'Party')
print "\n"
print difference(Fitness_aggregate, Rock_aggregate, 'Rock')
print "\n"
print difference(Fitness_aggregate, Indie_aggregate, 'Indie')
print "\n"
print difference(Fitness_aggregate, Sleep_aggregate, 'Sleep')
print "\n"
print difference(Fitness_aggregate, Jazz_aggregate, 'Jazz')
print "\n"
print difference(Fitness_aggregate, Classical_aggregate, 'Classical')
print "\n"
print difference(Fitness_aggregate, Romance_aggregate, 'Romance')
print "\n"
print difference(Fitness_aggregate, Metal_aggregate, 'Metal')
print "\n"
print difference(Fitness_aggregate, Raggae_aggregate, 'Raggae')
print "\n"
print difference(Fitness_aggregate, Dinner_aggregate, 'Dinner')
print "\n"
print difference(Fitness_aggregate, Soul_aggregate, 'Soul')
print "\n"
print difference(Fitness_aggregate, Blues_aggregate, 'Blues')
print "\n"
print difference(Fitness_aggregate, Punk_aggregate, 'Punk')
print "\n"
print difference(Fitness_aggregate, Family_aggregate, 'Family')
print "\n"
print difference(Fitness_aggregate, Gaming_aggregate, 'Gaming')
print "\n"

'''
