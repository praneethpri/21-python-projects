def view():
    with open('passwords.txt', 'r') as t:
        t.read()

def add():
    name = input('Username : ')
    password = input('Password : ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password)
    

while True:
    master_pwd = input('What is the master password :- ')
    if master_pwd == 'praneethp':
        pass
    else:
        quit()
    mode = input('Would like to view or add new ? ')
    if mode == 'view':
        view()
    elif mode == 'new':
        add()
    else:
        print('Invalid Mode')
        continue
