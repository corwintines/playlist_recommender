import requests

class Playlist: 
    def __init__(self, username, playlistname):
        # Spotify username
        self.playlist_username = username
        # Spotify playlist name
        self.playlist_playlistname = playlistname
        # Cluster that this playlist would be found in 
        self.playlist_cluster_index = None
        # Average attribute vector for playlist used to find its cluster
        self.playlist_attribute_vector = None
        '''
        Arrays for the attribute values for every song in the playlist
        '''
        self.playlist_song_names = None
        self.playlist_song_artists = None
        # A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
        self.playlist_accousticness = None
        # Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
        self.playlist_dancibility = None
        # Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
        self.playlist_energy = None
        # Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
        self.playlist_instrumentalness = None
        # The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
        self.playlist_loudness = None
        # Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
        self.playlist_speechness = None
        # The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
        self.playlist_tempo = None
        # A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
        self.playlist_valence = None
        
        
    def get_playlist(self):
        # Request to heroku server to get spotify playlist info
        data = {'username':self.playlist_username, 'playlist':self.playlist_playlistname}
        #playlist = requests.get('https://playlist-recommender.herokuapp.com/get_playlist')
        playlist = requests.get('http://localhost:3003/get_playlist', data)
        playlist = playlist.json()
        
        self.playlist_song_names = playlist[0]
        self.playlist_song_artists = playlist[1]
        
        song_uris = []
        for song in playlist[2]:
            song_uris.append(song.split(':')[2])
            
        song_uris = ','.join(song_uris)
            
        data = {'song_uri': song_uris}
        attributes = requests.get('http://localhost:3003/song_attributes', data);
        attributes = attributes.json()
        
        self.playlist_accousticness = attributes[0]
        self.playlist_dancibility = attributes[1]
        self.playlist_energy = attributes[2]
        self.playlist_loudness = attributes[3]
        self.playlist_instrumentalness = attributes[4]
        self.playlist_speechness = attributes[5]
        self.playlist_tempo = attributes[6]
        self.playlist_valence = attributes[7]        
    
    
    def generate_playlist_vector(self):
        for element in range(0, len(self.playlist_song_names)):
            accousticness += self.playlist_accousticness[element]
            dancibility += self.playlist_dancibility[element]
            energy += self.playlist_energy[element]
            instrumentalness += self.playlist_instrumentalness[element]
            loudness += self.playlist_loudness[element]
            speechiness += self.playlist_speechness[element]
            tempo += self.playlist_tempo[element]
            valence += self.playlist_valence[element]
    
        self.playlist_attribute_vector = [accousticness/len(self.playlist_accousticness), dancibility/len(self.playlist_dancibility), energy/len(self.playlist_energy), instrumentalness/len(self.playlist_instrumentalness), loudness/len(self.playlist_loudness), speechiness/len(self.playlist_speechiness), tempo/len(self.playlist_tempo), valence/len(self.playlist_valnce)]
        
        
    def find_cluster(self):
        print(self.playlist_cluster_index)
        
        
    def trim_outliers(self):
        print("Trim")
    