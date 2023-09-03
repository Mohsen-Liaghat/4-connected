from strategicalALG import *
from connected4 import ENV4C as ENV 
import tracemalloc as tmem
import time  

def main() :
    env = ENV()
    
    print("alpha beta search : ")
    tmem.start()
    t1 = time.time()
    print( abs(env) )
    print( "time usage =" , time.time() - t1 , "s" )
    print( "space usage =" , tmem.get_traced_memory() , "B" )
    tmem.stop() 

    print("min-max : ")
    tmem.start()
    t1 = time.time()
    print( min_max(env) )
    print( "time usage =" , time.time() - t1 , "s" )
    print( "space usage =" , tmem.get_traced_memory() , "B" )
    tmem.stop() 



if  __name__ == "__main__" :
    main() 