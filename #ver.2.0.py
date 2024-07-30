#ver.2.0
#guess number2.0
import random


RNGB = input('enter the smallest number you want: ')
RNGT = input('enter the biggest number you want: ')
RNGB = int(RNGB)
RNGT = int(RNGT)
r = random.randint(RNGB, RNGT)
x = 0
while True:
    
    x = x+1


    num = input('guess a number: ')
    
    num = int(num)

    if num < r:
        print('bigger')
        print('you have tested ', x , 'times')
    elif num > r:
        print('smaller')    
        print('you have tested ', x , 'times')




	
    else:
        if x <= 1:
            print('you are a guessing God!')
        elif x <= 5 and x > 1:
        	print('you are a guessing master')
        elif x <=10 and x > 5:
        	print('you are a little lucky')
        else:
        	print('you are pretty unlucky!')
        break

		
