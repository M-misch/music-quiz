def badrange_check(to_check):
    if len(to_check) > 15 or len(to_check) < 5 or to_check == None:
        return True

def user_is_authenticated(username,password):
    if username == 'Mischa123' and password == 'Password123':
        return True
    else:
        print ('unknown username or password')

authenticated=False
attempts=0

while not authenticated and attempts < 3:
    username=input('input the username')
    password=input('input the password')
    
    if badrange_check(username) or badrange_check(password):
        print('username and password must be at least 5 characters and at most 15 characters')
        attempts = attempts + 1
    elif user_is_authenticated(username,password):
        print('login successful')
        authenticated=True
    else:
        print('login failed')
        attempts = attempts + 1

if authenticated:
    print('Welcome to the Music Quiz!')
    print('Here\'s how to play')

    score=0
    answer1=False
    questionattempts=0
    while answer1==False and questionattempts <2:
        print('the artist for round one is taylor swift')
        song=input('the song initials are s---- i- o--')

        if song.lower() == 'shake it off':
            print('correct')
            answer1=True
            score=score + 3 if questionattempts == 0 else 1
        else:    
            print('incorrect')
            questionattempts = questionattempts + 1
            if questionattempts == 2:
                print('no more attempts')
                exit()

