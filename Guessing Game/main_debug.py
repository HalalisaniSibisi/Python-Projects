import random

print('Welcome to the guessing game!')

def guess_number(): 
    random_number = random.randint(1, 100)
    print(f"DEBUG - The secret number is: {random_number}")  # This line for debugging
    
    while True:
        try:
            player_guess = int(input('Enter your guess: '))

            if player_guess < random_number:
                print(f'Your guess ({player_guess}) is TOO LOW. The secret number is higher.')
            elif player_guess > random_number:
                print(f'Your guess ({player_guess}) is TOO HIGH. The secret number is lower.')
            else:
                print('Congratulations! You guessed the number correctly.')
                break
        except ValueError:
            print('Invalid input please enter the number!')
            
guess_number()