import os
import json
from time import sleep
import sys
import pythonwhois
import string
from multiprocessing.pool import ThreadPool
# from multiprocessing import Pool
import psutil
import signal
import argparse
from functools import partial


domains = []
available = []
unavailable = []


class DomainChecker():
	"""docstring for DomainChecker"""

	def __init__(self, arg):
		super(DomainChecker, self).__init__()
		self.arg = arg

	def send_email(self, msg):
		"""
		If the domain requested if available, prepare a message and send this to the user.
		"""
		pass

	def check_domain(self):
		for dom in domains:
			if dom is not None and dom != '':
				details = pythonwhois.get_whois(dom)
				if details['contacts']['registrant'] is not None:
					unavailable.append(dom)
				else:
					available.append(dom)

	def domain_generator(self):
		"""
		Function to generate domain names
		"""
		pass

	def check_file(self):
		"""
		Get the file for all the domain names willing to check and check those calling the check_domain function

		"""
		pass

	def random_search(self, size):
		pass

	def bulk_check(self):
		"""
		Bulk of domain names to check, report to a file and send this file to the user.
		:return:
		"""
		pass

	def check_ping(self):
		pass

	def get_domain_names_from_file(self):
		"""
		Get the domain names from a file.
		:return:
		"""
		with open('domains.txt', 'r+') as f:
			for domainName in f.read().splitlines():
				    domains.append(domainName)


	def three_letters_domain_checker(self):
		"""Check domain of three letters"""
		char_set = string.ascii_lowercase
		string_list = []
		for h in char_set:
			for u in char_set:
				string_list.append(h+u)

		return string_list
	

    # def printAvailability():
    #     print("-----------------------------")
    #     print("Unavailable Domains: ")
    #     print("-----------------------------")
    #     for un in unavailable:
    #         print(un)
    #     print("\n")
    #     print("-----------------------------")
    #     print("Available Domains: ")
    #     print("-----------------------------")
    #     for av in available:
    #         print(av)


