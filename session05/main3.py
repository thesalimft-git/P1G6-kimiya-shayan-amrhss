print('select a number between 1, 100')

u = 100
l = 1

while True:
    q = (u + l) // 2
    answer = input(f'is it {q} (u/d/c): ')
    if answer == 'u':
        l = q
    elif answer == 'd':
        u = q
    elif answer == 'c':
        print('hoora')
        break
    else:
        print('only u/d/c')
    