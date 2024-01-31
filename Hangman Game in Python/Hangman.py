import random
from collections import Counter

someWords = '''apple banana mango strawberry orange grape pineapple
apricot lemon coconut watermelon cherry papaya berry peach
lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords) 

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        # for printing the empty spaces for letters of the word
        print('_', end='')
    print()

    playing = True
    #List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word)+2
    correct = 0
    flag = 0
    try:
        while (chances != 0 ) and flag == 0 :
            print()
            chances -=1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print ('Enter ony a letter!')
                continue
            #validation of the guess
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed:
                print ('You have already guessed that letter')
                continue
            #If letter isguessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs iin the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess #the guess letter is added as many tmes

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char,end='')
                    correct += 1
                #If user has guessed all the letters
                #Once the correct word is guessed fully

                elif (Counter(letterGuessed) == Counter(word)):
                    #the game ends, even if chances remain
                    print ("the word is: ", end='')     
                    print(word)
                    flag = 1
                    print ("Congratulations you won!")
                    break # to break for loop
                    break # to break while loop
                else:
                    print('_', end='')
        # If user has used all of hs chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print( )
            print('You lost Try Again!')
            print ('the word was {}' .format(word))
    except KeyboardInterrupt:
        print()
        print('Bye Try Again!')
        exit()
          