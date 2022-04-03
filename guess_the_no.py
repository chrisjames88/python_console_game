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
     system will give you the clue if you guess wrong no. 
                  see carefully 
     pico: if one digit is correct but in wrong position
     fermi: one digit is correct and correct position
     bagel: no digit is correct''')
    while True:
        secretnum = getsecretnum()
        print("i have a no.")
        print(f"you have {no_of_guess} guess to get it.")

        numguesses = 1
        while numguesses <= no_of_guess:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print(f"guess {numguesses}:")
                guess = input('>')
                clues = getclue(guess,secretnum)
                print(clues)
                numguesses += 1

                if guess == secretnum:
                    break
                if numguesses > no_of_guess:
                    print("you run out of guesses")
                    print(f"the ans was{secretnum}")
            print("do yoi want play again?(yes/no)")
            if not input('.').lower().startswith("y"):
                break
        print("Thanks for play")
def getsecretnum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretnum = ''
    for i in range(num_digits):
        secretnum += str(numbers[i])
    return secretnum
def getclue(guess, secretnum):
    if guess == secretnum:
        return "you got it"
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            clues.append("fermi")
        elif guess[i] in secretnum:
            clues.append("pico")
    if len(clues) == 0:
        return "bagels"
    else:
        clues.sort()
        return ' '.join(clues)
main()
