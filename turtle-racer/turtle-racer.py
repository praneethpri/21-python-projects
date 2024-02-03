import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_turtles():
    races = 0
    while True:
        races = input('Enter how many turtles would you like to race? (2 - 10)')
        if races.isdigit():
            if int(races) >= 2 and int(races) < 10:
                break
            else:
                print('Enter a digit between 2 and 10.')
        else:
            print('Enter a digit between 2 and 10.')
    return races

def get_turtle_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racer')

x = get_number_of_turtles()
get_turtle_screen()
racer = turtle.Turtle()
random_colors = random.shuffle(COLORS)
random_colors_array = []
random_colors_array.append(random_colors)
racer.shape('turtle')
racer.color('cyan')
racer.forward(100)
print(random_colors_array)
time.sleep(20)
