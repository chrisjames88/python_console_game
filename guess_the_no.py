import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Welcome.
    This is a number guessing game where the system is thinking of a {}-digit number without repeating digits.
    The system will give you hints if you guess the wrong number. 
    *******See carefully, you need this while playing*******
    Hint1: one digit is correct but in the wrong position
    Hint2: one digit is correct and in the correct position
    Rethink: no digit is correct'''.format(NUM_DIGITS))

    while True:
        secret_num = get_secret_num()
        print("I have thought of a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdigit():
                print("Guess {}:".format(num_guesses))
                guess = input('> ')
            
            hints = get_hint(guess, secret_num)
            print(hints)
            num_guesses += 1
            
            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("You've run out of guesses.")
                print("The answer was {}".format(secret_num))

        print("Do you want to play again? (yes/no)")
        if not input('> ').lower().startswith("y"):
            break

    print("Well played! Thanks for playing.")

def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''.join(numbers[:NUM_DIGITS])
    return secret_num

def get_hint(guess, secret_num):
    if guess == secret_num:
        return "You got it!"

    hints = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            hints.append("Hint2")
        elif guess[i] in secret_num:
            hints.append("Hint1")

    if len(hints) == 0:
        return "Rethink"
    else:
        hints.sort()
        return ' '.join(hints)

if __name__ == "__main__":
    main()
