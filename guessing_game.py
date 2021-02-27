# -*- coding: utf-8 -*-
"""
Guessing Game

Created on Sat Feb 27 12:10:43 2021

@author: Lini Benson
"""

import random

secret_num = random.randint(1, 30)
name = input('What\'s your name? ')


for trial in range(1,7):
    print(secret_num)
    guess = int(input('Hello, %s Enter a number: (remember you have %s guesses left: ' %(name, 6-trial)))
    if (guess > secret_num):
        print('The number is too large, try another')
        
    elif (guess < secret_num):
        print('The number is too small, try another')
    
    else:
        break
    
if guess == secret_num:
    print('Well done %s you complete guessing after %s guesses' %(name ,trial))
else:
    print('You ran out of guesses, the number I was thinking of is', secret_num)
    
    