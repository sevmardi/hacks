import itertools, os

class TestingThings():
    def __construct__(self):
        pass
    def save_to_file(self):
        file = open('bcon.txt', 'w')
        file.write('hello world')
        file.close()
        
    def mydec(function):
        def _mydec(* args, **kw):
            #do soome stuff 
            #function gets called. 
            res = function(*args, **kw)
            return res;
        return _mydec

    
if __name__ == '__main__':
    main = TestingThings()
    main.save_to_file()
    
