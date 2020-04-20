#This is a guess the number game

import random #Here I import the random functions to use for the secretNumber variable.

print ('What is your name?')
name = input()

print('Well ' + name + ', I am thinking of a number between 1 and 30. Take a guess! But remember - you only get 8 turns to get the right number!')

secretNumber = random.randint(1, 30) # Here I get a random integer between 1 and 30

#Here is the loop that gives them 8 chances to geuss the right number
for guessTaken in range(1, 9): 
    print('Take a guess...')

    #Here I use the try except method so that if the user inputs something other than an integer an error message will appear.
    try: 
        # In order to compare the inputs I need to convert the input to an integer
        guess = int(input()) 
        if guess > secretNumber:
            print('You guessed too high!')
        elif guess < secretNumber:
            print('You guessed too low!')
        else:
            break #This is for the correct guess
    except:
        print('Error: Please input a number.')
    
if guess == secretNumber:
    print('You have guessed correctly! Well done ' + name + '! You only took ' + str(guessTaken) + ' turns to guess the number!')
else:
    print('You have not guessed the number correctly, better luck next time ' + name + '. I was thinking of ' + str(secretNumber) + '!')



