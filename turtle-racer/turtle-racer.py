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

def get_turtle_screen(x):
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racer')
    racer = turtle.Turtle()
    racer2 = turtle.Turtle()
    racer.shape('turtle')
    racer2.shape('turtle')
    racer2.setpos(-250, -250)
    turtle.mainloop()
    
get_turtle_screen(get_number_of_turtles())
