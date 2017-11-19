from sklearn.cluster import KMeans
import numpy as np
import h5py

test = h5py.File('/Users/corwinsmith/Documents/Database_DataMining_GroupProject/playlist_recommender/MillionSongSubset/data/A/A/A/TRAAABD128F429CF47.h5', 'r')
thing = test['analysis']['songs'].attrs.items()[6]
print test['analysis']['songs'].attrs.__dict__[0]
