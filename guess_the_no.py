'''
This is no guessing console game please see the code and
give me feedback for improvement.
I have used a random module to generating the no,I hope you will like it.
'''
import random
num_digits = 3
no_of_guess = 10
def main() :
    print(f'''I am Rakesh Soni, Welcome to the game.
     This is a no guessing game, system is thinking {num_digits} digits no without repeating.
     system will give you the hints if you guess wrong no. 
     *******see carefully you need this while playing*******
     Hint1: if one digit is correct but in wrong position
     Hint2: one digit is correct and correct position
     Rethink: no digit is correct''')
    while True:
        secretnum = getsecretnum()
        print("i have a no.")
        print(f"you have {no_of_guess} guess to get it.")

        numguesses = 1
        while numguesses <= no_of_guess:
            guess = ''
            print(f"guess {numguesses}:")
            guess = input('>')
            numguesses += 1
            if guess == secretnum:
                break
            if numguesses > no_of_guess:
                print("you run out of guesses")
                print(f"the ans was{secretnum}")
        print("do yoi want play again?(yes/no)")
        if not input('.').lower().startswith("y"):
            break
    print("Well played! Thanks for play")

# Refactoring
def getsecretnum():
    secretnum = random.randint(1, 10000)    
    return secretnum
def get_hint(guess, secretnum):
    if guess == secretnum:
        return "you got it"
    hints = []

    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            hints.append("Hint1")
        elif guess[i] in secretnum:
            hints.append("Hint2")
    if len(hints) == 0:
        return "Rethink"
    else:
        hints.sort()
        return ' '.join(hints)
main()
