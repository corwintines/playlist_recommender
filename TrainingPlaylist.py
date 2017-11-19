import requests

class TrainingPlaylist:
    def __init__(self, username, playlistname):
        # Spotify username
        self.playlist_username = username
        # Spotify playlist name
        self.playlist_playlistname = playlistname

        self.playlist_song_names = None
        self.playlist_song_artists = None
        self.playlist_accousticness = None
        self.playlist_dancibility = None
        self.playlist_energy = None
        self.playlist_instrumentalness = None
        self.playlist_loudness = None
        self.playlist_speechness = None
        self.playlist_tempo = None
        self.playlist_valence = None

        self.training_song_names = None
        self.training_song_artists = None
        self.training_accousticness = None
        self.training_dancibility = None
        self.training_energy = None
        self.training_instrumentalness = None
        self.training_loudness = None
        self.training_speechiness = None
        self.training_tempo = None
        self.training_valence = None

        self.groundtruth_song_names = None
        self.groundtruth_song_artists = None
        self.groundtruth_accousticness = None
        self.groundtruth_dancibility = None
        self.groundtruth_energy = None
        self.groundtruth_instrumentalness = None
        self.groundtruth_loudness = None
        self.groundtruth_speechness = None
        self.groundtruth_tempo = None
        self.groundtruth_valence = None


    def get_playlist(self):
        # Request to heroku server to get spotify playlist info
        data = {'username':self.playlist_username, 'playlist':self.playlist_playlistname}
        playlist = requests.get('https://playlist-recommender.herokuapp.com/get_playlist', data)
        playlist = playlist.json()

        self.playlist_song_names = playlist[0]
        self.playlist_song_artists = playlist[1]

        song_uris = []
        for song in playlist[2]:
            song_uris.append(song.split(':')[2])

        song_uris = ','.join(song_uris)

        data = {'song_uri': song_uris}
        attributes = requests.get('https://playlist-recommender.herokuapp.com/song_attributes', data);
        attributes = attributes.json()

        self.playlist_accousticness = attributes[0]
        self.playlist_dancibility = attributes[1]
        self.playlist_energy = attributes[2]
        self.playlist_loudness = attributes[3]
        self.playlist_instrumentalness = attributes[4]
        self.playlist_speechness = attributes[5]
        self.playlist_tempo = attributes[6]
        self.playlist_valence = attributes[7]
