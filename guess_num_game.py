import random

#setting difficulty level.
print("choose the difficulty level.")
print("1. Easy")
print("2. Medium")
print("3. Hard")

user_choice = input("Enter the number from (1/2/3) for difficulty level:")

if user_choice == "1":
    attempts = 8
    range = 50

elif user_choice == "2":
    attempts = 6
    range = 100
    
elif user_choice == "3":
    attempts = 4
    range = 150

else:
    print("invalide input, defaulting Easy")
    attempts = 10
    range = 50

target = random.randint(1, range)

print("Guess the number between 1 and range according to the difficulty level:" )
print("Attempts:", attempts)

#including numbers of attempts.
while attempts>0:
    user_choice = input("guess the number or quit(Q):")

# if user wants to quit the game.
    if user_choice == "Q":
        break

    user_choice = int(user_choice)

    if user_choice == target:
        print("Congratulations, You won...")
        break

    elif user_choice < target:
        print("Your guessed number is too low from the target.") 

    else:
        print("Your guessed number is too high from target, try again")

    attempts -=1
    print("attempts left", attempts)

if attempts == 0:
    print("GAME OVER, Target was:", target ,"begain from start.")