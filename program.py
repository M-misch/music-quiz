def badrange_check(to_check):
    if len(to_check) > 15 or len(to_check) < 5 or  to_check == '':
        return True

def user_is_authenticated(username,password):
    if username == 'Mischa123' and password == 'Password123':
        return True
    else:
        print ('unknown username or password')

username=input('input the username')
password=input('input the password')
    
if badrange_check(username) or badrange_check(password):
    print('username and password must be at least 5 characters and at most 15 characters')
elif user_is_authenticated(username,password):
    print('login successful')

