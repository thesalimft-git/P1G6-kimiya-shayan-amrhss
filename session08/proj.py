import random

win_card = {
    'p': 's',
    'r': 'p',
    's': 'r'
}

while True:
    p_choice = random.choice(list(win_card.keys()))
    h_choice = input('select from p/r/s: ')
    print('pc:', p_choice, 'you: ', h_choice)
    
    if h_choice in ['r', 'p', 's', 'end']:
        print('error: input is not valid')
        continue
    if h_choice == 'end':
        break
    elif h_choice == p_choice:
        print('try again')
        continue
    elif win_card.get(p_choice) == h_choice:
        print('win')
    else:
        print('loss')