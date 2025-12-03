import random
target = random.randint(1, 100)
while True:
    q = input('insert your guess: ')
    if not q.isdigit():
        print('it is not valid, insert only a number')
        continue

    q = int(q)
    if q > target:
        print('go down')
    elif q < target:
        print('go up')
    else:
        print('right answer: ', target)
        break
        

