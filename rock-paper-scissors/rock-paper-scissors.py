import random

options = ['rock', 'paper', 'scissors']

your_score = 0
computer_score = 0

while True:
    chosen_element = 0

    user_input = input('Enter rock/paper/scissors or Q to quit : ').lower()

    random_num = random.randint(0, 2)


    if user_input == 'rock' and options[random_num] == 'scissors':
        print('You Won ! Computer Lost !')
        your_score += 1
    elif user_input == 'paper' and options[random_num] == 'scissors':
        print('You Lost ! Computer Won !')
        computer_score += 1
    elif user_input == 'scissors' and options[random_num] == 'paper':
        print('You Won ! Computer Lost !')
        your_score += 1
    elif user_input == 'rock' and options[random_num] == 'paper':
        print('You Lost ! Computer Won !')
        computer_score += 1
    elif user_input == 'scissors' and options[random_num] == 'rock':
        print('You Lost ! Computer Won !')
        computer_score += 1
    elif user_input == 'paper' and options[random_num] == 'rock':
        print('You Won ! Computer Lost !')
        your_score += 1
    elif user_input == 'paper' and options[random_num] == 'paper':
        print('same value, play again !')
    elif user_input == 'scissors' and options[random_num] == 'scissors':
        print('same value, play again !')
    elif user_input == 'rock' and options[random_num] == 'rock':
        print('same value, play again !')
    elif user_input == 'q':
        print(f'''
        your score is {your_score}
        computer\'s score is {computer_score}
        ''')
        break
    else:
        break

