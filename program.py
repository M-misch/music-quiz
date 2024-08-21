def badrange_check(to_check):
    if len(to_check) > 15 or len(to_check) < 5 or to_check == None:
        return True

def user_is_authenticated(username,password):
    if username == 'Mischa123' and password == 'Password123':
        return True
    else:
        print ('unknown username or password')

def ask_music_question(artist,initials,answer):
    score=0
    answer1=False
    questionattempts=0
    while answer1==False and questionattempts <2:
        print('the artist for this round is ' + artist)
        song=input('the song initials are ' + initials)

        if song.lower() == answer :
            print('correct')
            answer1=True
            score=score + 3 if questionattempts == 0 else 1
        else:    
            print('incorrect')
            questionattempts = questionattempts + 1
            if questionattempts == 2:
                print('no more attempts')
                exit()
    return score


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
    print('Here\'s how to play ')
    score=0
    score = score + ask_music_question('taylor swift','s---- i- o--','shake it off')
    score = score + ask_music_question('justin bieber','b---','baby')
    #score = score + ask_music_question('adele','s--- f--','set fire to the rain')
    #score = score + ask_music_question('rihanna','u---- a---','umbrella')
    #score = score + ask_music_question('katy perry','r---','roar')
    print('your score is ' + str(score))

    