def banner(message1, message2, message3, border='*'):
    line = border * len(message2)
    print(line)
    print(message1)
    print(message2)
    print(message3)
    print(line)

def bannershort(messageshort1, messageshort2, border='*'):
    lineshort = border * len(messageshort1)
    print(lineshort)
    print(messageshort1)
    print(messageshort2)
    print(lineshort)

banner(' ',
       'WELCOME TO THE GUESSING GAME',
       ' ')

name = str(input('Hi there, my name is Computer.  What is yours: '))

banner('Nice to meet you {n}.  Let us play THE guessing game'.format(n=name),
       'The objective is to guess the right number I am "thinking" between 1 and 100 with the least attempts',
       'Let us see how many guesses you need to get it right')

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
    print('This is your attempt #{g}'.format(g=str(guesses)))
    print(' ')
    if (stranswer.isdigit()):
        print('Ok, lets check it')
    else:
        print('{n}, it needs to be a number!  Do not try tricking me!'.format(n=name))
        continue
    answer = int(stranswer)
    if answer > 100:
        bannershort('Pay attention to the instructions {n}! Super Salame!'.format(n=name),
                    'Number is under 101')
    elif answer < 1:
        bannershort('You clearly can’t follow instructions {n}!'.format(n=name),
                    'Number has to be greater than zero')
    elif answer > mysterynumber:
        bannershort('*** Good guess, getting warmer but it’s LOWER than {a}'.format(a=str(answer)), ' ')
    elif answer < mysterynumber:
        bannershort('*** Almost there, but Mystery Number is HIGHER than {a}'.format(a=str(answer)), ' ')
    else:
        banner('GREAT JOB {n}!'.format(n=name),
               'You guessed it.  Mystery number is {m}'.format(m=mysterynumber),
               'It took you {g} attempts this time'.format(g=guesses))
        break

print(' ')

if guesses > 30:
    print('*** You were really bad!  Try getting better')
elif guesses < 5:
    print('*** You are AWESOME!  Top of your class') 
else:
    print('*** Getting better, but still average.  You Do NOT want to be average, do you?')

bannershort(' ', 'End of Program', ' ')
