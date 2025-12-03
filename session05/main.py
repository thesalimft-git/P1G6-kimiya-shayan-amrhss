import random

pc_win = 0
h_win = 0

while True:
    pc_choice = random.choice(['r', 'p', 's'])
    h_choice = input('select from r/p/s or end: ')
    print('pc:', pc_choice, ', h:', h_choice)

    if h_choice not in ['r', 'p', 's', 'end']:
        print('invalid input')
    elif h_choice == 'end':
        break
    elif h_choice == pc_choice:
        print('same, try again')
    elif pc_choice == 'r':
        if h_choice == 'p':
            print('win')
            h_win += 1
        else:
            print('loss')
            pc_win += 1
            
    elif pc_choice == 'p':
        if h_choice == 's':
            print('win')
            h_win += 1
        else:
            print('loss')
            pc_win += 1
            
    elif pc_choice == 's':
        if h_choice == 'r':
            print('win')
            h_win += 1
        else:
            print('loss')
            pc_win += 1
            

print('pc: ', pc_win)
print('h: ', h_win)