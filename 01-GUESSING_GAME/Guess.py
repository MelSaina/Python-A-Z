import random
import math

# input

lower = int(input("Enter the lower boundary value:~ "))
upper = int(input("Enter the highest boundary value:~ "))

# Let's generate the random number

x = random.randint(lower,upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)),
        "chances to guess the integer!\n")

# Initialize the number of guesses

count = 0

# Calculatiion of minimum number of guesses is dependant on the range 

while count < math.log(upper - lower + 1,2):
    count += 1

# Taking guessing number as the input
    
    guess = int(input("Guess a number:- "))

    if x == guess:
        print( " Congratulations you did it in ",count, "try")
        break
    elif x > guess:
        print( "You guessed too small!")
    elif x < guess:
        print(" You guessed too high!")

# If guessing is more than required 

if count >= math.log(upper - lower + 1,2):
    print("\nThe number is %d" % x )
    print ("\tBetter Luck Next time!")