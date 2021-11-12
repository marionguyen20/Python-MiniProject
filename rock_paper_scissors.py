import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    print(f"Computer choice: {computer}")
    print(f"Your choice: {user}")

    if user == computer:
        return "It is a tie!"
    elif is_win (user, computer):
        return "You won!"
    else:
        return "You lost!"


def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True

print(play())