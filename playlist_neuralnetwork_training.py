from nimblenet.activation_functions import sigmoid_function
from nimblenet.cost_functions import cross_entropy_cost
from nimblenet.learning_algorithms import RMSprop
from nimblenet.data_structures import Instance
from nimblenet.neuralnet import NeuralNet
from TrainingPlaylist import TrainingPlaylist


def main():
    playlist = TrainingPlaylist('spotify', '37i9dQZF1DX76Wlfdnj7AP')
    playlist.get_playlist()
    playlist.construct_training_groundtruths()
    training_dataset = [Instance( [0,0], [0] ), Instance( [1,0], [1] ), Instance( [0,1], [1] ), Instance( [1,1], [0] )]

    settings = {
        # Required settings
        "n_inputs": 8, # Number of input signals
        "layers": [
                    (8, sigmoid_function), # First input layer (number of nodes, activation function)
                    (1, sigmoid_function)  # Output layer
                ],

        # Optional settings
        "initial_bias_value": 0.0,
        "weights_low": -0.1,
        "weights_high": 0.1
    }

    network = NeuralNet(settings)
    training_set   = dataset
    test_set       = dataset

    RMSprop(network, training_set, test_set, cost_function, ERROR_LIMIT=0.1)
    network.save_network_to_file("%s.pkl" % "filename")


main()
