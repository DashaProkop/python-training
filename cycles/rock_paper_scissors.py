import random

should_continue = True
while should_continue:
    player_choice = input('Your choice: [R/S/P]').lower()
    if player_choice not in ['r', 's', 'p']:
        print('Incorrect. Try again')
        continue
    comp_choice = random.choice(['r', 's', 'p'])
    print(f'Computer choise = {comp_choice}')
    winning_combination = [('p', 'r'), ('r', 's'), ('s', 'p')]
    if player_choice == comp_choice:
        print('A draw')
    elif (player_choice, comp_choice) in winning_combination:
        print('Player wins')
    else:
        print('Computer wins')
    should_continue = input('Want to proceed? [y/n]').lower() == 'y'
