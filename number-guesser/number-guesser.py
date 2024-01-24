import random

top_of_range = input('Enter a Number : ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    guess = random.randint(0, top_of_range)

else:
    print('Only Numbers are allowed')
    quit()

count = 0
while True:
    question = input('Type your Guess: ')
    if guess < int(question):
        print('You are above the Number')
        count += 1
    elif guess > int(question):
        print('You are below the Number')
        count += 1
    elif guess == int(question):
        print(f'You\'ve guessed the correct Number in {count} times.')
        break
    else:
        print('Only numbers are allowed')
        break
