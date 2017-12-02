from nimblenet.activation_functions import sigmoid_function
from nimblenet.cost_functions import cross_entropy_cost
from nimblenet.learning_algorithms import RMSprop
from nimblenet.data_structures import Instance
from nimblenet.neuralnet import NeuralNet
from TrainingPlaylist import TrainingPlaylist
import os
import pickle


def produce_dataset(training_file):
    training_data = []
    with open(training_file) as data:
        dataset = pickle.load(data)
        for song in dataset:
            attributes = [song.attributes['accousticness'],
                          song.attributes['danceability'],
                          song.attributes['energy'],
                          song.attributes['instrumentalness'],
                          song.attributes['loudness'],
                          song.attributes['speechiness'],
                          song.attributes['tempo'],
                          song.attributes['valence']]
            recommended_value = [song.attributes['rec_value']]

            training_data.append(Instance(attributes, recommended_value))

    return training_data


def main():
    training_dataset = produce_dataset(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'training_playlists', 'training_1.txt'))
    test_dataset = produce_dataset(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'test_playlists', 'test_1.txt'))

    settings = {
        # Required settings
        "n_inputs": 8, # Number of input signals
        "layers": [
                    (8, sigmoid_function), # First Hidden Layer (number of nodes, activation function)
                    (1, sigmoid_function)  # Output layer
                ],

        # Optional settings
        "initial_bias_value": 0.0,
        "weights_low": -0.1,
        "weights_high": 0.1
    }

    network = NeuralNet(settings)
    training_set = training_dataset
    test_set = test_dataset
    cost_function = cross_entropy_cost

    RMSprop(network, training_set, test_set, cost_function, ERROR_LIMIT=0.1, max_iterations=100000, batch_size=1800)
    network.save_network_to_file("%s.pkl" % "filename3")


main()
