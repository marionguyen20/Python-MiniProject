import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low, ")
        elif guess > random_number:
            print("Sorry, guess again. Too high. ")
    print(f'Yay, congrast. You have guessed the number {random_number} correctly')


def computer_guess (x):
    low = 1
    high = x 
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high) #If low = high => error
        else:
            guess = low
        feedback = input(f"Is {guess} correct or higher, lower than your number: (c/l/h) ")
        if feedback == 'l':
            low = guess + 1
            print(f"{guess} is lower than your number")
        elif feedback == 'h':
            high = guess - 1
            print(f"{guess} is higher than your number")
    print(f"Yay. Congrast. Your computer have gueesed the number {guess} correctly ")

#640
computer_guess(1000)
