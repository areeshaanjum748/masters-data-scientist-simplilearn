# User credentials
users = {
    'user1':'password1',
    'user2':'password2',
    'user3':'password3'
}

# Admin credentials
admins = {
    'admin':'adminpass'
}
# Session - Simulate a login session
session = {
    'user' : None,
    'admin': None
}

# Login mechanism
def login(username, password, is_admin = False):
    if is_admin:
        if username in admins:
            if(admins[username] == password):
                session['admin'] = username
                print('Admin logged in successfully')
        else:
            print('Admin does not exist in the system')
    else:
        if username in users:
            if(users[username] == password):
                session['user'] = username
                print('User logged in successfully')
            else:
                print('Invalid credentials')
            print()
        else:
            print('User does not exist in the system')
