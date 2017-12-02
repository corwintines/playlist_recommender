'''
This script selects only the relevant attributes for each song in the Million Song Dataset HDF5
files and stores them as a pickle text file as a list of Song objects in:
	'.../playlist_recommender/training_data/pickle/songs_msd/song_list_mined_from_hdf5.txt'
'''

import os
import Song
import hdf5_access_Luke
import pickle_tools_Luke


# get your current path to our repository
dir_path = os.path.dirname(os.path.realpath(__file__))

# the path to the Million Song Datases 'data' folder
msd_original_data_folder = os.path.join(dir_path,'MillionSongSubset/data')

# the folder where the pickle will be dumped
output_folder = os.path.join(dir_path,'training_data/pickle/songs_msd')

# the name of the pickle txt file
pickle_file_name = 'song_list_mined_from_hdf5.txt'

out_path = os.path.join(output_folder,pickle_file_name)
if not os.path.isdir(output_folder):
	os.mkdir(output_folder)

if os.path.isdir(msd_original_data_folder):
	song_list = hdf5_access_Luke.getSongs_MSD(msd_original_data_folder)
	pickle_tools_Luke.writeToPickle(song_list, out_path)
else:
	print "Error: check file paths."