MAX_LINES = 5

def deposit():
    while True:
        deposit_amount = input('What would you like to deposit? Rs. ')
        if deposit_amount.isdigit():
            if int(deposit_amount) > 0:
                break
            else:
                print('Deposit amount must be over 0.')
        else:
            print('Please enter a number.')
    return deposit_amount

def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on? (1 - {str(MAX_LINES)}) ')
        if lines.isdigit():
            if int(lines) > 0 and int(lines) <= int(MAX_LINES):
                break
            else:
                print('Enter number between the range.')
        else:
            print('Please enter a number.')
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()
