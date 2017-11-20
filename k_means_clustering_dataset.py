from sklearn.cluster import KMeans
import numpy as np

# Takes the array of attributes for songs and clusters them
attributes = np.array(x)
kmeans = KMeans(n_clusters=10, random_state=0).fit(attributes)
labels = kmeans.predict(attributes)
centroids = kmeans.cluster_centers_
