import pickle
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'song_lists', 'Blues.txt')) as f:
    songs = pickle.load(f)
    print songs[0].attributes
