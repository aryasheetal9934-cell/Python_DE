import time

def start_counter(second,delay=1):
    for i in range (1,second+1):  #(10,0,-1) for reverse 
        print ("counter is at:",i)
        time.sleep(delay)
    print("counter finished!")
start_counter(5,delay=1)
