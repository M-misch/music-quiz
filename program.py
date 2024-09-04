def badrange_check(to_check):
    if len(to_check) > 15 or len(to_check) < 5 or to_check == None:
        return True

def checkUserInFile(username,password):
    f = open('users.txt','r')
    line = f.readline()
    userinfomatch = False
    while line:
        userinfo = line.split()
        if username == userinfo[0] and password == userinfo[1]:
            userinfomatch=True
            print(userinfo[0]+ ', you have a score of ' + userinfo[2])
        line = f.readline()
    f.close()

    return userinfomatch


def ask_music_question(artist,initials,answer):
    score=0
    answer1=False
    questionattempts=0
    while answer1==False and questionattempts <2:
        print('the artist for this round is ' + artist)
        song=input('the song initials are ' + initials + ' enter your guess here ')

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
    elif checkUserInFile(username,password):
        print('login successful')
        authenticated=True
    else:
        print('login failed')
        attempts = attempts + 1

if authenticated:
    print('Welcome to the Music Quiz!')
    print('Here\'s how to play the quiz an artist and song initials will be displayed on the screen, guess the song to collect point ')
    score=0
    score = score + ask_music_question('taylor swift','s---- i- o--','shake it off')
    score = score + ask_music_question('Kanye west','r------','runaway')
    score = score + ask_music_question('rihanna','u-------','umbrella')
    score = score + ask_music_question('katy perry','r---','roar')
    print('your score is ' + str(score))
    #savescore(username,score)

    

# def savescore (username, score):
#     f = open('users.txt','r')
#     line = f.readline()
#     newfilecontent = ''
#     while line and len(line) > 0:
#         userinfo = line.split()
#         if username == userinfo[0]:
#             newfilecontent = newfilecontent + userinfo[0] + ' ' + userinfo[1] + ' ' + str(score) + '\n'
#         else:
#             newfilecontent = newfilecontent + line + '\n' 
            
#         line = f.readline()
#     f.close()
#     f = open('users.txt','w')
#     f.write(newfilecontent)
#     f.close()

# savescore('Anouk',1)