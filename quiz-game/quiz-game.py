print('Welcome to play-time.')

def main():
    enter = input('would you like to play? [default = \'yes\']')
    if enter.lower() == 'yes' or enter == None or len(enter) == 0:
        enter_game()
    else:
        quit()

def enter_game():
    count = 0
    question1 = input('''
    What is the Capital of Sri Lanka?

    1) Colombo
    2) Nugegoda
    3) Sri Jayawardhanapura
    4) Negombo

    ''')

    if question1 == '3':
        print('Correct!')
        count += 1
    elif question1 == '1' or question1 == '2' or question1 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question2 = input('''
    What is the National Sport in Sri Lanka ?

    1) Volleyball
    2) NetBall
    3) Cricket
    4) Chess

    ''')

    if question2 == '1':
        print('Correct!')
        count += 1
    elif question2 == '3' or question2 == '2' or question2 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question3 = input('''
    What is the most popular sport in Sri Lanka ?

    1) Volleyball
    2) Soccer
    3) Cricket
    4) Swimming

    ''')

    if question3 == '3':
        print('Correct!')
        count += 1
    elif question3 == '1' or question3 == '2' or question3 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question4 = input('''
    Whom is the governing body of Sri Lanka ?

    1) Prime Minister
    2) President
    3) Chancellor
    4) Governer

    ''')

    if question4 == '2':
        print('Correct!')
        count += 1
    elif question4 == '3' or question4 == '1' or question4 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()
                  
    question5 = input('''
    What is the year Sri Lanka gained Independence ?

    1) 1941
    2) 1948
    3) 1945
    4) 1963

    ''')

    if question5 == '2':
        print('Correct!')
        count += 1
    elif question5 == '3' or question5 == '1' or question5 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question6 = input('''
    Who is the first Prime Minister of Sri Lanka ?

    1) D.S. Senanayake
    2) S.W.R.D. Bandaranayake
    3) Jhon Kothalawala
    4) William Gopallawa

    ''')

    if question6 == '1':
        print('Correct!')
        count += 1
    elif question6 == '3' or question6 == '2' or question6 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question7 = input('''
    Which year the Sri Lanka won the Cricket World Cup ?

    1) 1999
    2) 1927
    3) 2007
    4) 1996

    ''')

    if question7 == '4':
        print('Correct!')
        count += 1
    elif question7 == '3' or question7 == '2' or question7 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question8 = input('''
    From Whom the Sri Lanka gained independence from ?

    1) United States of America
    2) Great Britain
    3) Russia
    4) Japan

    ''')

    if question8 == '2':
        print('Correct!')
        count += 1
    elif question8 == '3' or question8 == '1' or question8 == '4':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question9 = input('''
    Who is the first President of Sri Lanka ?

    1) Sirimawo Bandaranayake
    2) Jhon Kothalawala
    3) Mahinda Rajapaksha
    4) J.R. Jayawardhana

    ''')

    if question9 == '4':
        print('Correct!')
        count += 1
    elif question9 == '3' or question9 == '2' or question9 == '1':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    question10 = input('''
    Who is the last king of Sri Lnaka ?

    1) Kawanthissa
    2) Dutugemunu
    3) Sri Weera Parakrama Narendrasinhe
    4) Sri Wickrama Rajasinghe

    ''')

    if question10 == '4':
        print('Correct!')
        count += 1
    elif question10 == '3' or question10 == '2' or question10 == '1':
        print('Incorrect!')
    else:
        print('unrecognized answer')
        quit()

    print(f'your score is {count} ')

main()
