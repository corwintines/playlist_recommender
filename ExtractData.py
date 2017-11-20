import os
import glob
import hdf5_getters
import h5py

f = h5py.File("MillionSongSubset/data/A/A/A/TRAAAAW128F429D538.h5",'r')

#h5 = hdf5_getters.open_h5_file_read('TRAAAAW128F429D538.h5')

basedir = "MillionSongSubset/data"
ext = ".h5"
for root, dirs, files in os.walk(basedir):
    files = glob.glob(os.path.join(root,'*'+ext))
    for f in files:
        h5 = hdf5_getters.open_h5_file_read(f)
        print('Song Name :', hdf5_getters.get_title(h5), 
        	'Danceability: ',hdf5_getters.get_danceability(h5), 
        	'Energy: ',hdf5_getters.get_energy(h5), 
        	'Loudness: ',hdf5_getters.get_loudness(h5),
            'Tempo: ', hdf5_getters.get_tempo(h5))
        h5.close()

h5.close()