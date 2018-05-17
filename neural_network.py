import os

class NeuralNetwork:
	def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
		self.inodes = input_nodes
		self.hnodes = hidden_nodes
		self.onodes = output_nodes

		self.lr = learning_rate 

		pass

	def train(self):
		pass

	def query(self):
		pass


if __name__ == '__main__':
	nn = NeuralNetwork()
	nn.learning_rate = 0.03
	

