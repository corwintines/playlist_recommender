# 4310/4660 Group Project - Playlist Continuation Recommender
# November 20, 2017
# Lucas Jakober
# Accessing Million Song Dataset HDF5 files

import os
import h5py as h5
import matplotlib.pyplot as plt
import numpy as np
import time

# Functions for ALL HDF5 objects (File, Group and Dataset)
def isFile(item):
	return isinstance(item, h5.File)
def isGroup(item):
	return isinstance(item, h5.Group)
def isDataset(item):
	return isinstance(item, h5.Dataset)
def getInfo(item):
	info = {
		'id'		: item.id,
		'ref' 		: item.ref,
		'parent' 	: item.parent,
		'file' 		: item.file,
		'name' 		: item.name,
	}
	return info

# Functions for Dataset HDF5 objects only
def getType(dataset):
	return dataset.dtype
def getShape(dataset):
	return dataset.shape
def getValue(dataset):
	return dataset.value

# Functions for File or Group HDF5 objects
def getAttributes(item):
	return item.attrs
def getAttributeKeys(item):
	return item.attrs.keys()
def getAttributeValues(item):
	return item.attrs.values()
def getNumAttributes(item):
	return len(item.attrs)


# Pass the path to your 'data' folder inside the MillionSongSubset on your computer
def getSongs_MSD(MSD_data_folder_path):
	rootdir	= MSD_data_folder_path
	songList = []
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			filepath = subdir + os.sep + file
			if filepath.endswith(".h5"):
				f = h5.File(filepath,"r")
				songDict = getSongAttributes_MSD(f)
				song = convertSongDictToTup(songDict)
				songList.append(song)
				# print song
	return songList

def getSongAttributes_MSD(h5file):
	f = h5file
	song_tup = ()
	f_items = f.items()
	songAttribtes = {
		'artist' : None,
		'artist_familiarity' : None,
		'artist_hotness' : None,
		'duration' : None,
		'endOfFadeIn' : None,
		'startOfFadeOut' : None,
		'title' : None }
	for item in f_items:
		if isGroup(item[1]):
			group_items = item[1].items()
			for group_item in group_items:
				if isDataset(group_item[1]):
					dataset_key = group_item[0]
					dataset_value = group_item[1]
					if item[0] == 'metadata' and dataset_key == 'songs':
						valueTup = getValue(dataset_value)[0]
						songAttribtes['artist'] = valueTup[9]
						songAttribtes['artist_familiarity'] = valueTup[2]
						songAttribtes['artist_hotness'] = valueTup[3]
						songAttribtes['title'] = valueTup[18]
					if item[0] == 'analysis' and dataset_key == 'songs':
						valueTup = getValue(dataset_value)[0]
						songAttribtes['duration'] = valueTup[3]
						songAttribtes['endOfFadeIn'] = valueTup[4]
						songAttribtes['startOfFadeOut'] = valueTup[26]						
	return songAttribtes

def convertSongDictToTup(songDict):
	songTup = (songDict['title'], songDict['artist'], songDict['artist_familiarity'], songDict['artist_hotness'], songDict['duration'], songDict['endOfFadeIn'], songDict['startOfFadeOut'])
	return songTup




### Garbage below only for testing purposes ###
def test_level1():
	eff = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/MillionSongSubset/data/A/G/A/TRAGAAF128F9338911.h5'
	f = h5.File(eff,"r")
	f_items = f.items()
	for item in f_items:
		print ("item: ", item)

def test_level2():
	eff = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/MillionSongSubset/data/A/G/A/TRAGAAF128F9338911.h5'
	f = h5.File(eff,"r")
	f_items = f.items()
	for item in f_items:
		if isGroup(item[1]):
			group_items = item[1].items()
			for group_item in group_items:
				print ("group_item: ", group_item)

def test_level3():
	eff = '/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/MillionSongSubset/data/A/G/A/TRAGAAF128F9338911.h5'
	f = h5.File(eff,"r")
	f_items = f.items()
	for item in f_items:
		if isGroup(item[1]):
			group_items = item[1].items()
			for group_item in group_items:
				if isDataset(group_item[1]):
					dataset_key = group_item[0]
					print ("item: ", item)
					print ("group_item: ", group_item)
					print ("dataset_key: ", dataset_key)
					dataset_value = group_item[1]
					print ("dataset_value: ", dataset_value,"\n\n")
					# valueTup = getValue(dataset_value)[0]
					valueTup = getValue(dataset_value)
					print ("valueTup:\n",valueTup)
					print ("\n\n\n\n")

# level1()
# level2()
# level3()
songs = getSongs_MSD('/Users/lucasjakober/Documents/Semester 9/Combined Course Project/Code/playlist_recommender/MillionSongSubset/data')

'''
****** Analysis tuple structure ******
	analysis dictionary object:
		(u'analysis', <HDF5 group "/analysis" (16 members)>)

		1 		('analysis_sample_rate', '<i4'),
		2 		('audio_md5', 'S32'),
		3 		('danceability', '<f8'),							*Spotify
		4 		('duration', '<f8'),
		5 		('end_of_fade_in', '<f8'),
		6 		('energy', '<f8'),									*Spotify
		7 		('idx_bars_confidence', '<i4'),
		8 		('idx_bars_start', '<i4'),
		9 		('idx_beats_confidence', '<i4'),
		10		('idx_beats_start', '<i4'),
		11		('idx_sections_confidence', '<i4'),
		12		('idx_sections_start', '<i4'),
		13		('idx_segments_confidence', '<i4'),
		14		('idx_segments_loudness_max', '<i4'),
		15		('idx_segments_loudness_max_time', '<i4'),
		16		('idx_segments_loudness_start', '<i4'),
		17		('idx_segments_pitches', '<i4'),
		18		('idx_segments_start', '<i4'),
		19		('idx_segments_timbre', '<i4'),
		20		('idx_tatums_confidence', '<i4'),
		21		('idx_tatums_start', '<i4'),
		22		('key', '<i4'),
		23		('key_confidence', '<f8'),
		24		('loudness', '<f8'),								*Spotify
		25		('mode', '<i4'),
		26		('mode_confidence', '<f8'),
		27		('start_of_fade_out', '<f8'),
		28		('tempo', '<f8'),									*Spotify
		29		('time_signature', '<i4'),
		30		('time_signature_confidence', '<f8'),
		31		('track_id', 'S32')

	Sample metadata returned for one song (ie. one h5 file) using utility function above getValue(dataset_item)
		- it returns a list containing one tuple with 20 elements

		[
			(
		1		22050,
		2		'a1f5526c64f7ce9c46b28eee26867dcd',
		3		0.0,
		4		195.52608,
		5		0.205,
		6		0.0,
		7		0,
		8		0,
		9		0,
		10		0,
		11		0,
		12		0,
		13		0,
		14		0,
		15		0,
		16		0,
		17		0,
		18		0,
		19		0,
		20		0,
		21		0,
		22		2,
		23		0.467,
		24		-8.775,
		25		0,
		26		0.59,
		27		184.918,
		28		146.484,
		29		1,
		30		0.0,
		31		'TRADDBK128F1483FF8'
			)
		]

****** Metadata tuple structure ******
	metadata dictionary object:
		(u'metadata', <HDF5 group "/metadata" (5 members)>)

		1		('analyzer_version', 'S32'),
		2		('artist_7digitalid', '<i4'),
		3		('artist_familiarity', '<f8'),
		4		('artist_hotttnesss', '<f8'),
		5		('artist_id', 'S32'),
		6		('artist_latitude', '<f8'),
		7		('artist_location', 'S1024'),
		8		('artist_longitude', '<f8'),
		9		('artist_mbid', 'S40'),
		10		('artist_name', 'S1024'),
		11		('artist_playmeid', '<i4'),
		12		('genre', 'S1024'),
		13		('idx_artist_terms', '<i4'),
		14		('idx_similar_artists', '<i4'),
		15		('release', 'S1024'),
		16		('release_7digitalid', '<i4'),
		17		('song_hotttnesss', '<f8'),
		18		('song_id', 'S32'),
		19		('title', 'S1024'),
		20		('track_7digitalid', '<i4')

	Sample metadata returned for one song (ie. one h5 file) using utility function above 'getValue(dataset_item)'
		- it returns a list containing one tuple with 20 elements

			[
				(
		1			'',
		2			590,
		3			0.7306695019354311,
		4			0.6238352009226658,
		5			'ARR6LWJ1187FB44C8B',
		6			nan,
		7			'Athens, GA',
		8			nan,
		9			'ea4dfa26-f633-4da6-a52a-f49ea4897b58',
		10			'R.E.M.',
		11			1324,
		12			'',
		13			0,
		14			0,
		15			'And I Feel Fine.....The Best Of The IRS Years 82-87',
		16			43154,
		17			nan,
		18			'SOLUGTX12A6D4FAC08',
		19			'So. Central Rain (2006 Digital Remaster)',
		20			460648
				)
			]

'''
