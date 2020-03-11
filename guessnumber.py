print(' ')
print('***********************************************')
print(' ')
name = str(input('Hi there, my name is Computer.  What is yours: '))
print(' ')
print('***********************************************')
print(' ')
print('Nice to meet you ' + name + '.  Let us play a guessing game')
print('The objective is to guess the right number I am "thinking" between 1 and 100 with the least attempts')
print(' ')
print('Let us see how many guesses you need to get it right')

import time
t = time.localtime()
strHour = time.strftime("%H", t)
intHour = int(strHour)
#print(intHour)
strMin = time.strftime("%M", t)
intMin = int(strMin)
#print(intMin)
strSec = time.strftime("%S", t)
intSec = int(strSec)
#print(intSec)

guesses = 0
stranswer = 0
answer = 0
mysterynumber = intHour + intMin + intSec
#print(mysterynumber)

while mysterynumber > 100:
    mysterynumber -= intSec

while answer != mysterynumber:
    print(' ')
    stranswer = (input('What number between 1 and 100 am I "thinking" of: '))
    guesses += 1
    print('This is your attempt #' + str(guesses))
    print(' ')
    if (stranswer.isdigit()):
        print('Ok, lets check it')
    else:
        print(name + ', it needs to be a number!  Do not try tricking me!')
        continue
    answer = int(stranswer)
    if answer > 100:
        print('***********************************************')
        print('Pay attention to the instructions ' + name + '!  Salame')
        print('Number is under 101')
        print('***********************************************')
    elif answer < 1:
        print('***********************************************')
        print('You clearly can’t follow instructions ' + name + '!')
        print('Number has to be greater than zero')
        print('***********************************************')
    elif answer > mysterynumber:
        print('*** Good guess, getting warmer but it’s LOWER than ' + str(answer))
    elif answer < mysterynumber:
        print('*** Almost there, but Mystery Number is HIGHER than ' + str(answer))
    else:
        print('***********************************************')
        print('GREAT JOB ' + name + '!  You guessed it')
        print('Mystery number is ' + str(mysterynumber))
        print('It took you ' + str(guesses) + ' attempts this time')
        print('***********************************************')
        break
print(' ')
if guesses > 30:
    print('*** You were really bad!  Try getting better')
elif guesses < 5:
    print('*** You are AWESOME!  Top of your class') 
else:
    print('*** Getting better, but still average.  You Do NOT want to be average, do you?')
print(' ')
print('End of Program')
print(' ')
