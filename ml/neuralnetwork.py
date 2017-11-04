import numpy as np
# import tensorflow as tf
import glob
import codecs
import pickle
import PyPDF2

#based on below
# https://github.com/zackthoutt/got-book-6/blob/master/got-book-generator.ipynb

mmds_chaps = sorted(glob.glob("data/*.txt"))
print("Found {} books".format(len(mmds_chaps)))



