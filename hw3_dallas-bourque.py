%matplotlib inline
# %matplotlib widget
# All imports

from random import choice
import numpy as np
import matplotlib.pyplot as plt
from copy import copy
import time
from IPython import display


Class NeuralNetwork:

    Class Layer:
        #layer[x] = individual layers ([0] = bias = 1)
        #layer[][x] = 
        def __init__(self, num):

    def __init__(self, layers, activation='sigmoid'):
        self.layers = []
        for i in range(1, len(layers) - 1):
            self.layers.append(np.ones(layers[i], layers[i-1])
        self.activation_type = 0 if self.activation == 'sigmoid' else 1
    
    def fit(self, X, y, learning_rate=0.2, steps=100000, tol=1e-2):
        #docstring
        
        
    def find_RMS_error(self, X, y):
        #docstring

        return RMS_err
        
    def predict(self, x):
        #docstring
        return prediction
    
    def visual_NN_boundaries(self, Nsamp=2000):
        #docstring