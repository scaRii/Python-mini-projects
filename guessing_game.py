print("GUESSING GAME")
import random
top_limit = input("Please type an upper limit: ")
if top_limit.isdigit():
    top_limit = int(top_limit)
    if int(top_limit) <= 0:
        print("Enter number greater than 0")
        quit()
else:
    print("Enter a number!!")
    quit()
random_num = random.randint(1,int(top_limit))
guesses = 0
while True:
    user_guess = input("Make a guess: ")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue
    if user_guess == random_num:
        print("You got it right")
        break
    else:
        if user_guess > random_num:
            print("You were above the number")
        if user_guess < random_num:
            print("You were below the number")
        continue
print("You got got in", guesses, "guesses")