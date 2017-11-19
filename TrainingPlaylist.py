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

        
