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
    testing_dataset = [song for song in playlist.groundtruth_combined]
    print testing_dataset

    # settings = {
    #     "n_inputs" : 8,
    #     "layers"   : [(2, sigmoid_function), (1, sigmoid_function)]
    # }
    #
    # network        = NeuralNet(settings)
    # training_set   = dataset
    # test_set       = dataset
    # cost_function  = cross_entropy_cost
    #
    # RMSprop(network, training_set, test_set, cost_function)


main()
