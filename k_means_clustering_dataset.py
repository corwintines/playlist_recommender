from sklearn.cluster import KMeans
import numpy as np

def cluster_data(data):
    attribute_data = extract_attribute_data(data)
    # Takes the array of attributes for songs and clusters them
    attributes = np.array(attribute_data)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(attributes)
    labels = kmeans.predict(attributes)
    centroids = kmeans.cluster_centers_
    centroids_order = [
    centroids[5],
    centroids[0],
    centroids[1],
    centroids[6],
    centroids[2],
    centroids[3],
    centroids[7],
    centroids[8],
    centroids[9],
    centroids[10],
    centroids[4],
    centroids[11],
    centroids[12]
    ]
    return labels, centroids_order

def extract_attribute_data(data):
    attribute_data = []
    for element in range(0, len(data)):
        data_element = [
        data[element][2],
        data[element][3],
        data[element][4],
        data[element][5],
        data[element][6],
        data[element][7],
        data[element][8],
        data[element][9],
        data[element][10],
        data[element][11],
        data[element][12],
        data[element][13],
        data[element][14]
        ]
        attribute_data.append(data_element)
    return attribute_data
