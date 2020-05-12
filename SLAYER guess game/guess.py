# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:53:03 2020

@author: Adnan Hashem Mohamed

PROGRAM TASK:
    This program prompts the user to guess a siz-digit number for
    a variable called SLAYER. Where each letter corresponds to the
    digit in the guessed number. Correct guess which satisfies the 
    equation: SLAYER + SLAYER + SLAYER = LAYERS
"""

def correct(guess):
    '''
    Precondition: guess is a six-digit integer
    Postconition: returns true if guess satisfies the equation:
    SLAYER + SLAYER + SLAYER = LAYERS
    '''
    the_sum = str(guess * 3)
    LAYERS = str(guess)[1::] + str(guess)[0]
    return the_sum == LAYERS

def play():
    guess = 0
    while(not(99999 < guess < 1000000)):
        try:
            guess = int(input("Enter guess: "))
            if(not(99999 < guess < 1000000)):
                print("guess should be 6 digit long!")
        except(ValueError):
            guess = 0
            print("Your guess should be of integer type!")
        
    if(correct(guess)):
        print("CORRECT!!!")
    else:
        print("INCORRECT!!!:(")
        
def answers():
    '''
    returns the list of possible answers
    '''
    answers = []
    for guess in range(100000, 1000000):
        if(correct(guess)):
            answers.append(guess)
    return answers

def show_answers(answers):
    '''
    precondition: answers is a list of integers
    Postcondition: prints the elements of answers
    '''
    print("*** Answers ***")
    for element in answers:
        print(element)
    print("------------")
        


if(__name__ == "__main__"):
    print("Youe six-digit guess should satisfy the equation SLAYER + SLAYER + SLAYER = LAYERS\n")
    replay = 'Yes'
    give_up = 'no'
    while('yes' in replay.lower()):
        play()
        give_up = input("Whould you like to view the possible answers (yes/no): ")
        if('yes' in give_up.lower()):
            show_answers(answers())
            print("Thanks for playing :)")
            break
        replay = input("Whould you like to replay? (yes/no): ")
        print("-------------\n")

