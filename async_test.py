import asyncio, time

# def run(coros):
#     try:
#         coros.send(None)
#         print('try: finished')
#     except StopIteration as e:
#         print(e.value)
#         print('except: finished')

def run(coros):
    yield from coros


async def sleep(n):
    start=time.time()
    while True:
        # yield
        if time.time()-start > n:
            print('done:', n)
            return


async def waiting(n):
    await sleep(2)
    # sleep(1)
    return n
    
async def main(loop):
    coros=[]
    for i in reversed(range(10)):
        print('reversed:', i)
        if i % 2 == 0:
            coros.append(loop.create_task(waiting(i)))
            
    await asyncio.sleep(5)
    print('sleep stopped')
    await asyncio.gather(*coros)


# def test():
#     loop = asyncio.get_event_loop()
#     results = loop.run_until_complete(main(loop))
    

# test()

# test = waiting(2)
# print(test)

run(waiting(2))


# test.send(None)
# try:
#     test.send(None)
#     print('try: finished')
# except StopIteration as e:
#     print(e.value)
#     print('except: finished')
# print(test.send(None))











# class Count():

#     """Iterator that counts upward forever."""

#     def __init__(self, start=0):
#         self.num = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         print('running __next__')
#         num = self.num
#         self.num += 1
#         return num

#     def __iter__(self):
#         while True:
#             print('running __iter__')
#             num = self.num
#             self.num += 1
#             yield self.num
            
#     def send(self, arg):
        

# count = Count()

# print(count)
    
# print(next(count))
# print(next(count))

# for x in count:
#     if x > 10: break
#     print(x)



# def Test(x):
#     count=0
#     while True:
#         input_arg = yield
#         print(count)
#         count+=1
#         if x in input_arg:
#             yield True
#         else:
#             yield False

# test = Test('test')
# print(test.send(None))
# print('this is a test', test.send('this is a test'))
# print('this is a another test', test.send('this is a another test'))
# print('this is test number 3', test.send('this is test number 3'))
# print('this is test number 4', test.send('this is test number 4'))