# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import random
# from collections import Counter, defaultdict
# import math
# import datetime
# import subprocess
from collections.abc import Sequence 
# import tensorflow as tf
# print(tf.get_default_graph())

# g = tf.Graph()
# print(g)


class OldRegsiter(object):
	def __init__(self, ohms):
		
		self._ohms = ohms
	
	def get_ohms(self):
		return self._ohms

	def set_ohms(self, ohms):
		self._ohms = ohms

	@property
	def voltage(self):
		return self._voltage
	
	@voltage.setter
	def voltage(self, voltage):
		self._voltage = voltage
		self.current = self._voltage / self.ohms

	