"""
    In this game, two numbers are taken from you,
    one number is randomly selected from among the numbers,
    and then you will have 5 chances to find the chosen number.
"""
from random import randint 
try:
    one_number = int(input("enter your [one] number: "))
    end_number = int(input("enter your [end] number: "))
    
    if one_number >= end_number :
        number_random = randint(end_number, one_number)
    else:
        number_random = randint(one_number, end_number)
        
except:
    print("please enter your number!")

guess_number = 5

while guess_number > 0:
    print(f"your suess is => {guess_number}")
    try:
        guess_user = int(input("enter your suess: "))
    except:
        print("please enter your number!")
        break
    guess_number -= 1
    if guess_user > number_random:
        print("Your guess is greater than the number!")

    elif guess_user == number_random:
        print("Your guess is correct")
        break
    else :
        print("Your guess is smaller than the number!")
