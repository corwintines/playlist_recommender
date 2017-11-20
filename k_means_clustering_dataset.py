from sklearn.cluster import KMeans
import numpy as np

def cluster_data(data):
    attribute_data = extract_attribute_data(data)
    # Takes the array of attributes for songs and clusters them
    attributes = np.array(attribute_data)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(attributes)
    labels = kmeans.predict(attributes)
    centroids = kmeans.cluster_centers_
    return labels, centroids

def extract_attribute_data(data):
    attribute_data = []
    for element in range(0, len(data)):
        data_element = [
        data[element][2],
        data[element][3],
        data[element][4],
        data[element][5]
        ]
        attribute_data.append(data_element)
    return attribute_data
