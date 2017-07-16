import itertools, os
from itertools import groupby

class ExperInPython():

    def __construct__(self):
        pass

    def starting_at_five():
        value = input().strip()
        while value != '':
            for i in itertools.islice(value.split(), 4 , None):
                yield i
                value = input().strip()

    def with_head(self, iterable, headsize=1):
        """tee the back and forth iterator"""
        a, b = itertools.tee(iterable)
        return list(itertools.islice(a, headsize))


    def group_by_uniq_iter_compress(self, data):
        """This function is able to group the duplicate elements from an iterator, as long as they are adjacent"""
        return ((len((group)), name)
                for name, group in groupby(data))
    
    def decompress(self,data):
        return (car * size for size, car in data)
    

if __name__ == '__main__':
    seq = [1,2,3,4,54]
    
    main = ExperInPython()
    main.group_by_uniq_iter_compress('get upppppppp')
