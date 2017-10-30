import random
from utils import sign
class Perceptron(object):
    def __init__(self, weights_len):
        self.weights = []
        self.lr = 0.1
        for i in range(weights_len):
            self.weights.append(random.uniform(-1,1))
    def guess(self, inputs):
        soma = 0
        for i in range(len(inputs)):
            soma += inputs[i]*self.weights[i]
        return sign(soma)
    def guessF(self, x):
        return -(self.weights[2]/self.weights[1])*1 - (self.weights[0]/self.weights[1])*x
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)):
            self.weights[i] += inputs[i]*error*self.lr
