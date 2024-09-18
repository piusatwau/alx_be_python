#If the guess is correct, display a message like “Congratulations, you guessed it!”
#If the guess is too high, display a message like “Oops, your guess is a bit high. Try again!”
#If the guess is too low, display a message like “Nope, your guess is a bit low. Give it another shot!”


'''
first the random function will generate a random number
after compare the generated number to the user's guess
then display the answer

'''

import random
def play_game():
    
    secret_number = random.randint(5, 10)
    guess_count = 0
    
    while True:
        guess = int(input("I am thinking of a number between 5 and 10, guess which number it is: "))
        guess_count += 1
             
        match guess:
            case _ if guess == secret_number:
                print("Congratulations, you guessed it!")
                print(f"It took you {guess_count} attempt(s) to get the correct answer")
                break
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

    play_again = input("would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing")
play_game()
