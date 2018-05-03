# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import random
# from collections import Counter, defaultdict
# import math
# import datetime
# import subprocess

# import tensorflow as tf
# print(tf.get_default_graph())

# g = tf.Graph()
# print(g)

class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self, arg):
		super(MyObject, self).__init__()
		self.arg = arg
		self.__private_filed= 0
		self.public_filed = 1

	def get_private_field(self):
		return self.__private_filed
		



