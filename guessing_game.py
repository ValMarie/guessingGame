import random


#g Guessing the secret number of the Computer
def guess(number):
    player_guess = 0
    random_number = random.randint(1, number)
    while player_guess != random_number:
        player_guess = int (input ("Guess a number between 1 and {}: ".format(number))) # f-str literals not available on this py version
        print(player_guess)
        if player_guess > random_number:
            print("Too high! Sorry, guess again.")
        elif player_guess < random_number:
            print("Too low! Sorry, guess again.")
    
    print("Good job! You guess the number {} correctly".format(random_number))


# Letting the Computer guess your secret number
def  computer_guess(number):
    lower_bound = 1
    upper_bound = number
    feedback = ""
    
    while feedback != "c":
        if upper_bound != lower_bound:
            guess = random.randint(lower_bound, upper_bound)
        else:
            guess = upper_bound # or lower_bound b/c lower_bound = Upper_bound
        feedback = input("Is the number {} too high (H), too low (L) or correct (C)? ".format(guess).lower())
        if feedback == "h":
            upper_bound = guess - 1
        elif feedback == "l":
            lower_bound = guess + 1

    print("Wow! Computer guessed your number {} correctly.".format(guess))


invitation = input("Are you ready to play (y/n) ")
while True:
    if invitation == "y":
        print("OK, then let's play...")
        guess(100)
        print("Now your turn...")
        computer_guess(100)
    elif invitation == "n":
        print("Alright, Thanks for stopping by")
        break
    
