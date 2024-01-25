import random

name = input ("What is your name ? ")

print ( " Goodluck !", name)

# The function is to choose a random name 
# from this list

words = ['rainbow', 'computer', 'science', 'programming', 'python',
         'mathematics', 'player', 'condition', 'reverse', 'water',
         'board','geeks']

word = random.choice(words)
print ("Guess the characters!")
guesses = ''

# Any number of turns can be used here

turns = 12

while turns > 0:
    # count  the number of fails

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end="")
        else:
            print("_")
            
            failed += 1
    
    if failed == 0:
        # user will win the game if failure is 0

        print ("You Win!")
        print ("The word is : ", word)
        break
    
    print()
    guess = input("Guess a character:")

    guesses += guess

    if guess not in word:
        turns -= 1

        print ("Wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print(" You Loose!")
