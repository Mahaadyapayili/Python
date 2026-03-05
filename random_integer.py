import random
number=str(random.randint(0,9))
print("I will generate a number from 0 to 9, and you have to guess one at a time")
playing=True
print("The game ends when you guess it correctly.")
while playing:
    guess=input("Give me your best guess\n")
    if number==guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("Your guess was not quite right, try again")