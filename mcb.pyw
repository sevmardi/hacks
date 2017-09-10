import sys, shelve, pyperclip
# 	mcb.pyw - Saves and loads pieces of text to the clipboard.
# 	Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#
#   py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#
# 	py.exe mcb.pyw list - Loads all keywords to clipboard.

class MultiClipBoard():
	"""docstring for MultiClipBoard"""
	def __init__(self, arg):
		super(MultiClipBoard, self).__init__()
		self.arg = arg
		self.read_file()

	def read_file(self):
		mcbShelf = shelve.open('mcb')

		#TODO Save to clipboard
		if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
			mcbShelf[sys.argv[2]] = pyperclip.paste()
		elif len(sys.argv) == 2:
			#TODO list of keywords and load content
			if sys.argv[1].lower() == 'list':
				pyperclip.copy(str(list(mcbShelf.keys())))
		elif sys.argv[1] in mcbShelf:
			pyperclip.copy(mcbShelf[sys.argv[1]])

		mcbShelf.close()

	#TODO
	def delete_keyword(self):
		pass

	def delete_all_list(self):
		pass

if __name__ == '__main__':
	MultiClipBoard()
