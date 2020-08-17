import random, time

def sleep(n):
    start=time.time()
    while True:
        yield
        if time.time()-start > n:
            return
    
    
def rand_sleeps(id, n):
    rand = random.randint(0, n)
    print(id, 'sleep:', rand)
    yield from sleep(rand)
    print('done:', id)
    

def rand_sleeps_wrapper(loop, x, n):
    for i in range(x):
        loop.add_event(rand_sleeps(i, n))
        yield
        
    
    
class custom_event_loop:
    
    def __init__(self):
        self.event_loop = []
        self.new_events = []
        
    def add_event(self, e):
        self.new_events.append(e)
        
    def merge(self):
        self.event_loop+=self.new_events
        self.new_events=[]
    
    def run(self, *args):
        self.event_loop+=args
        while self.event_loop:
            self.merge()
            for i, e in enumerate(self.event_loop):
                try:
                    e.send(None)
                except StopIteration as e:
                    self.event_loop.pop(i)
                    
        
    
loop = custom_event_loop()
    
test1 = rand_sleeps_wrapper(loop, 3, 5)

loop.run(test1)