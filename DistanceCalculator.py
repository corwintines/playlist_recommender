import numpy as np
from operator import itemgetter
from sklearn.cluster import KMeans
import scipy
from scipy.stats.stats import pearsonr



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
			locals()["group"+str(i)].append(songAttributes[j].__getitem__(i))#correlationMatrix.append(songAttributes[j].__getitem__(i))
		
		print str(i), locals()["group"+str(i)]
		if (i == 4):
			for k in range(0, sizeOfElement-1):
				l = k+1
				while(l < sizeOfElement):
					tuple1 = tuple(locals()["group"+str(k)])
					tuple2 = tuple(locals()["group"+str(l)])
					temp = scipy.stats.pearsonr(tuple1,tuple2)
					correlationMatrix.append(temp[0])
					l = l+1
	return correlationMatrix

def pearsonCorrelationDict(songAttributes):
	numOfElements = (len(songAttributes))
	sizeOfElement = (len(songAttributes[0]))

	Danceability = []
	Energy = []
	Loudness = []
	Tone = []
	Beats = []

	for i in range(0, (len(songAttributes[0]))):
		for j in range(0, (len(songAttributes))):
			if i == 0:
				Danceability.append(songAttributes[j].__getitem__(i))
			if i == 1:
				Energy.append(songAttributes[j].__getitem__(i))
			if i == 2:
				Loudness.append(songAttributes[j].__getitem__(i))
			if i == 3:
				Tone.append(songAttributes[j].__getitem__(i))
			if i ==4:
				Beats.append(songAttributes[j].__getitem__(i))

	print "Danceability: ", Danceability
	print "Energy: ", Energy
	print "Loudness: ", Loudness
	print "Tone: ", Tone
	print "Beats: ", Beats

	dict = {'Danceability' : {'Energy':(scipy.stats.pearsonr(Danceability,Energy)[0]), 'Loudness':(scipy.stats.pearsonr(Danceability,Loudness)[0]), 'Tone':(scipy.stats.pearsonr(Danceability,Tone)[0]), 'Beats':(scipy.stats.pearsonr(Danceability,Beats)[0])},
			'Energy' : {'Danceability':(scipy.stats.pearsonr(Danceability,Energy)[0]), 'Loudness':(scipy.stats.pearsonr(Energy,Loudness)[0]), 'Tone':(scipy.stats.pearsonr(Energy,Tone)[0]), 'Beats':(scipy.stats.pearsonr(Energy,Beats[0]))},
			'Loudness' : {'Danceability': (scipy.stats.pearsonr(Loudness,Danceability)[0]), 'Energy':(scipy.stats.pearsonr(Loudness,Energy)[0]), 'Tone':(scipy.stats.pearsonr(Loudness,Tone)[0]), 'Beats':(scipy.stats.pearsonr(Loudness,Beats)[0])},
			'Tone' : {'Danceability':(scipy.stats.pearsonr(Tone,Danceability)[0]), 'Energy':(scipy.stats.pearsonr(Tone,Energy)[0]), 'Loudness':(scipy.stats.pearsonr(Tone,Loudness)[0]), 'Beats':(scipy.stats.pearsonr(Tone,Beats)[0])},
			'Beats' : {'Danceability':(scipy.stats.pearsonr(Beats, Danceability)[0]), 'Energy':(scipy.stats.pearsonr(Beats,Energy[0]), 'Loudness':(scipy.stats.pearsonr(Beats,Loudness)[0]), 'Tone':(scipy.stats.pearsonr(Beats,Tone)[0])
	print 'Danceability :', dict['Danceability']
	print 'Energy :', dict['Energy']
	print 'Loudness :', dict['Loudness']
	print 'Tone :', dict['Tone']
	print 'Beats :', dict['Beats']

	#print str(i), locals()["group" + str(i)]
	#return scipy.stats.pearsonr(listOfSongs, aggregateVector)


cluster_data(listOfCentroids)
print pearsonCorrelationDict(songAttributes)
