import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number_to_guess = random.randint(1, 20)
    guesses = 0

    while True:
        try:
            guess = int(input("Take a guess.\n"))
            guesses += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()