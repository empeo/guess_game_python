import random
import time

def display_message():
    print("""
    Welcome to the Guessing Game!
    You need to guess a number between 1 and 100.
    You have 5 attempts. Good luck!
    """)

def generate_secret_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input! Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_guessing_game():
    secret = generate_secret_number()
    attempts = 5
    print(secret)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = get_user_guess()

        if guess == secret:
            print("Congratulations! You guessed the correct number!")
            return
        elif guess < secret:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        attempts -= 1
    
    print("Sorry, you've run out of attempts!")
    print(f"The correct number was {secret}.")

def main():
    display_message()
    play_guessing_game()

main()
