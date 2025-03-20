import random

print('Welcome to the guessing game!')

def guess_number(): 
    random_number = random.randint(1, 100)

    
    while True:

        try:
        
            player_guess = int(input('Enter your guess: '))


            if player_guess < random_number:
                print('Your guess is lower than the number try again')
            elif player_guess > random_number:
                print('Your guess is higher than the number. Try again')
            else:
                print('Congratulations! You guessed the number correctly.')
                break
        except ValueError:
            print('Invalid input please enter the number!')

guess_number()