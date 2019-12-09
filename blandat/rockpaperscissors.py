import random

again = "true"
while again == "true":
 hand = random.randint(1, 3)

 hand2 = input("Rock, Paper or Scissors? ")

 if hand2 == ("Rock"):
    hand2 = 1
 elif hand2 == ("Paper"):
    hand2 = 2
 elif hand2 == ("Scissors"):
    hand2 = 3
 else:
    print("Bruh you gotta choose")

 if hand + hand2 == 2:
    print("You both chose Rock")
 if hand + hand2 == 3:
    if hand == 1:
        print("You chose Paper and the computer chose Rock, ")
        print("You won")
        again = "false"
    else:
        print("You chose Rock but the computer chose Paper, ")
        print("You lost")
 if hand + hand2 == 4:
    if hand == 2:
        print("You both chose Paper")
    elif hand2 == 1:
        print("You chose Rock and the computer chose Scissors, ")
        print("You won")
        again = "false"
    else:
        print("You chose Scissors but the computer chose Rock, ")
        print("You lost")
 if hand + hand2 == 5:
    if hand == 2:
        print("You chose Scissors and the computer chose Paper, ")
        print("You won")
        again = "false"
    else:
        print("You chose Paper but the computer chose Scissors, ")
        print("You lost")
 if hand + hand2 == 6:
    print("You both chose scissors")