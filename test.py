import time

def main(n):
    start = time.time()

    the_sum  = 0
    for i in range(1, n+1):
        the_sum+=i
    end = time.time()
    return the_sum,end-start

def sum_of_n(n):
    return (n * (n +1) ) / 2       
    
if __name__ == '__main__':
   
    print(sum_of_n(50))   
