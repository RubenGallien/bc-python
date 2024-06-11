import random

def ft_except(number, turn, rep):
    if not rep.isdigit():
        print("That's not a number")
        return
    rep = int(rep);
    if (rep < number):
        print("Too low!!")
        return
    elif (rep > number):
        print("Too high!!")
        return
    if (number == rep and number == 42):
        print("The answer to the ultimate question of life, the universe and everything is 42.")
    if number == rep and turn == 1:
        print("Congratulations! You got it on your first try!")
    elif number == rep:
        print(f"Congratulations, you've got it!\nYou won in {turn} attempts!")
    if (number == rep):
        exit()



start = "This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!"
# number = random.randint(1, 99)
number = 11
turn = 1

print(start)
while (1):
    print("What's your guess between 1 and 99?")
    rep = input()
    if (rep == "exit"):
        print("GoodBye!")
        exit()
    ft_except(number, turn, rep)
    turn += 1