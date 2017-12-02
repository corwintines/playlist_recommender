from sklearn.cluster import KMeans
import numpy as np

def cluster_data(song_list):
    attribute_data = extract_attribute_data(song_list)
    # Takes the array of attributes for songs and clusters them
    attributes = np.array(attribute_data)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(attributes)
    labels = kmeans.predict(attributes)
    centroids = kmeans.cluster_centers_
    print centroids
    centroids_order = [
    centroids[0].tolist(),
    centroids[1].tolist(),
    centroids[2].tolist(),
    centroids[3].tolist(),
    centroids[4].tolist(),
    centroids[5].tolist(),
    centroids[6].tolist(),
    centroids[7].tolist(),
    centroids[8].tolist(),
    centroids[9].tolist()
    ]
    return labels, centroids_order

energy               17
accousticness        16
danceability         5
instrumentalness     4
valence              4

def extract_attribute_data(song_list):
    attribute_data = []
    for song in song_list:
        accousticness = song.attributes['accousticness']
        danceability = song.attributes['danceability']
        instrumentalness = song.attributes['instrumentalness']
        valence = []
        ]
        data_element = [
        song.attributes[]]
    for element in range(0, len(song_list)):
        data_element = [
        data[element][7],
        data[element][9],
        data[element][10],
        data[element][11],
        data[element][12]
        ]
        attribute_data.append(data_element)
    return attribute_data
