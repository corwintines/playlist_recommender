from sklearn.cluster import KMeans
import numpy as np
import h5py


attributes = np.array()
kmeans = KMeans(n_clusters=2, random_state=0).fit(attributes)
labels = kmeans.predict(attributes)
centroids = kmeans.cluster_centers_
