import random

print("Welcome to LS Casino, roulette")
money = int(input("How much money do you want to bet? "))


if money < 100:
    print("Okay noob")
elif money > 100000:
    print("Daaamn okay")
else:
    print("Confirmed")
bet = input("Do you want to bet on red, black or green? ")

number = random.randint(1, 19)

if bet == "green":
    if number == 1:
        print("Risky, but you won! You got:", money*17, "dollars!")
    else: 
        print("Stupid risk, you lost", money, "dollars idiot")
else:
    if number < 10 > 1:
        print ("You lost", money, "dollars")
    else:
        print("You won", money*2, "dollars!")
    


input()