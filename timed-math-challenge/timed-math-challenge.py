import random
import time

max_operator = 15
min_operator = 2
operators = ['+', '-', '*']
total_problems = 10

def output(count):
    end = time.time()
    seconds = round(end - start, 2)
    statement = f'''
    
    \033[93m Your Score :- {count}
    You finished in {seconds} seconds.
                      '''
    return statement

def generate_problem():
    left = random.randint(min_operator, max_operator)
    right = random.randint(min_operator, max_operator)
    random_operator = operators[random.randint(0, 2)]
    expression = str(left) + " " + random_operator + " " + str(right)
    answer = eval(expression)
    return expression, answer

count = 0
print("\033[92m press 'q' to quit \033[0m")
for i in range(total_problems):
    start = time.time()
    expression, answer = generate_problem()
    try:
        guess = int(input(f"\u001b[1m Problem {i + 1} : \u001b[0m {expression} = "))
        if guess == answer:
            count += 1
    except:
        break
print(output(count))

