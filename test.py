import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import random
from collections import Counter, defaultdict
import math, datetime





def log(message, when=None):
	when = datetime.datetime.now() if when is None else when
	print("%s: %s" % (when, message))


log('hie there')





