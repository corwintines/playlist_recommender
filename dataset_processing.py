from hdf5_access_Luke import *
# from k_means_clustering_dataset import *
import os
import requests

def query_spotify_for_attributes():
    MSD = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'MillionSongSubset', 'data')
    MSD_song_list = getMSDSongTitleAndArtistList(MSD)
    MSD_song_attributes = []
    print(len(MSD_song_list))

    for song in range(0, 100):
        data = {'artist': MSD_song_list[song][1], 'songname': MSD_song_list[song][0]}
        attributes = requests.get('https://playlist-recommender.herokuapp.com/spotify_tracks', data)
        uri = attributes.text
        if uri is 'oops':
            MSD_song_list.pop(song)
        else:
            uri = attributes.text.split(':')[2]
            data = {'song_uri': uri}
            attributes = requests.get('https://playlist-recommender.herokuapp.com/get_track_attributes', data)
            attributes = attributes.json()
            MSD_song_attributes.append(attributes)

    print(len(MSD_song_attributes))
