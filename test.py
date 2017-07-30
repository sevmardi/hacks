import itertools, os

class TestingThings():
    def __construct__(self):
        pass
    def save_to_file(self):
        file = open('bcon.txt', 'w')
        file.write('hello world')
        file.close()
        
    def test(self, cls):
    	print('work with %s' % cls)
    	it = classmethod(it)
    	def uncommon():
    		print('I could be a global function')
    	uncommon = statismethod(uncommon)

    def decorator(self, cls):
    	print('work with %s', % cls)
    
    @staicmethod
    def uncommon(self):
    	print('I could be a global function')

    
if __name__ == '__main__':
    main = TestingThings()
    main.save_to_file()
    
