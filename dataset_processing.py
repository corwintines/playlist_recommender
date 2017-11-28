from hdf5_access_Luke import *
import os
import requests

def query_spotify_for_attributes():
    MSD = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'MillionSongSubset', 'data')
    # (title, artist, artist_familiarity, artist_hotness,duration,endOfFadeIn, startOfFadeOut)
    MSD_song_list = getSongs_MSD(MSD)
    for song in MSD_song_list:
        if song[0] == None or song[1] == None or song[2] == None or song[3] == None or song[4] == None or song[5] == None or song[6] == None:
            MSD_song_list.remove(song)
    print MSD_song_list[9852]
    MSD_song_attributes = []
    MSD_song_final = []

    for song in range(9854, len(MSD_song_list)):
        print song
        data = {'artist': MSD_song_list[song][1], 'songname': MSD_song_list[song][0]}
        attributes = requests.get('https://playlist-recommender.herokuapp.com/spotify_tracks', data)
        uri = attributes.text
        if uri == 'oops':
            MSD_song_attributes.append(None)
        else:
            uri = uri.split(':')[2]
            data = {'song_uri': uri}
            attributes = requests.get('https://playlist-recommender.herokuapp.com/get_track_attributes', data)
            print attributes
            print attributes.text
            if attributes.status_code == 503:
                break
            try:
                attributes = attributes.json()
                MSD_song_attributes.append(attributes)
            except:
                MSD_song_attributes.append(None)

    # (title, artist, artist_familiarity, artist_hotness,duration,endOfFadeIn, startOfFadeOut, acousticness, dancability, energy, intrumentalness, loudness, speechiness, tempo, valence)
    for data in range(0, len(MSD_song_attributes)):
        if MSD_song_attributes[data] != None:
            MSD_song_final.append([
            MSD_song_list[9854+data][0],
            MSD_song_list[9854+data][1],
            MSD_song_list[9854+data][2],
            MSD_song_list[9854+data][3],
            MSD_song_list[9854+data][4],
            MSD_song_list[9854+data][5],
            MSD_song_list[9854+data][6],
            MSD_song_attributes[data][0],
            MSD_song_attributes[data][1],
            MSD_song_attributes[data][2],
            MSD_song_attributes[data][3],
            MSD_song_attributes[data][4],
            MSD_song_attributes[data][5],
            MSD_song_attributes[data][6],
            MSD_song_attributes[data][7]
            ])

    return MSD_song_final

def combine_cluster_song_data(song_data, label_data):
    combined_data = []
    for elem in range(0, len(song_data)):
        data = [
        label_data[elem],
        song_data[elem][0],
        song_data[elem][1],
        song_data[elem][7],
        song_data[elem][2],
        song_data[elem][3],
        song_data[elem][8],
        song_data[elem][4],
        song_data[elem][5],
        song_data[elem][9],
        song_data[elem][10],
        song_data[elem][11],
        song_data[elem][12],
        song_data[elem][6],
        song_data[elem][13],
        song_data[elem][14]
        ]
        combined_data.append(data)

    return combined_data

def pearson_correlation_data(data):
    correlation_data = []
    for item in data:
        correlation_data.append([
        item[2],
        item[3],
        item[4],
        item[5],
        item[6],
        item[7],
        item[8],
        item[9],
        item[10],
        item[11],
        item[12],
        item[13],
        item[14]
        ])

    return correlation_data
