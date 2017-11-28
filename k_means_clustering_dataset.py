from sklearn.cluster import KMeans
import numpy as np

def cluster_data(data):
    attribute_data = extract_attribute_data(data)
    # Takes the array of attributes for songs and clusters them
    attributes = np.array(attribute_data)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(attributes)
    labels = kmeans.predict(attributes)
    centroids = kmeans.cluster_centers_
    print centroids
    centroids_order = [
    centroids[0],
    centroids[1],
    centroids[2],
    centroids[3],
    centroids[4],
    centroids[5],
    centroids[6],
    centroids[7],
    centroids[8],
    centroids[9]
    ]
    return labels, centroids_order

def extract_attribute_data(data):
    attribute_data = []
    for element in range(0, len(data)):
        data_element = [
        data[element][7],
        data[element][9],
        data[element][10],
        data[element][11],
        data[element][12]
        ]
        attribute_data.append(data_element)
    return attribute_data
