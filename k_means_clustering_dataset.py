from sklearn.cluster import KMeans
import numpy as np

def cluster_data(data):
    # Takes the array of attributes for songs and clusters them
    attributes = np.array(data)
    kmeans = KMeans(n_clusters=1, random_state=0).fit(attributes)
    labels = kmeans.predict(attributes)
    centroids = kmeans.cluster_centers_
    return labels, centroids
