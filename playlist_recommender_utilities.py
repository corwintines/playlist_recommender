from nimblenet.data_structures import Instance


def create_processing_data(song_list):
    prediction_set = []
    for song in song_list:
        prediction_set.append(Instance([song.attributes['accousticness'],
                                        song.attributes['danceability'],
                                        song.attributes['energy'],
                                        song.attributes['instrumentalness'],
                                        song.attributes['loudness'],
                                        song.attributes['speechiness'],
                                        song.attributes['tempo'],
                                        song.attributes['valence']]))

    return prediction_set


def generate_top_twentyfive(recommended_values, hundred_song_set):
    print True
