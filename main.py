import numpy

inputs = [1, 1]

class Neuron:
    def __init__(self, _weight, _bias, inputs_):
        self.weight = _weight
        self.bias = _bias
        self.inputs = inputs_
    def forward(self):
        self.activation = numpy.average(self.inputs) * self.weight + self.bias
        return self.activation

inputNeuron = [Neuron(2, 1, inputs)]

print(inputNeuron[0].forward())
output = [Neuron, Neuron]