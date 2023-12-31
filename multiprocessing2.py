import multiprocessing
def test():
    print("this is my multiprocessing program")

def producer(q):
    for i in range(10):
        q.put(i)
    
def consumer(q):
    while True:
        item=q.get()
        if item ==None:
            break
        print(item)

if __name__=='__main__':
    queue=multiprocessing.Queue()
    m1=multiprocessing.Process(target=producer,args=(queue,))
    m2=multiprocessing.Process(target=consumer,args=(queue,))
    m1.start()
    m2.start()
    #queue.put("asif")
    m1.join()
    m2.join()


   
   