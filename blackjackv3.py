import random
import time
suit = ("Hjärter", "Spader", "Ruter", "Klöver")
cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, "knekt", "dam", "kung", "ess")

userpoints = 0
dealerpoints = 0
loop = 0
keepplaying = True
dealerkeepplaying = True

def dealercard():
    global userpoints, dealerpoints
    s = random.randint(0, 3)
    c = random.randint(0, 12)
    cardsuit = suit[s]
    cardvalue = cards[c]
    if c > 8 and c < 12:
        dealerpoints += 10
    elif c == 12:
        if dealerpoints < 11:
            dealerpoints += 11
        elif dealerpoints > 10:
            dealerpoints += 1
    else:
        dealerpoints += c + 2
    return cardsuit + " " + str(cardvalue)

def card():
    global userpoints, dealerpoints
    s = random.randint(0, 3)
    c = random.randint(0, 12)
    cardsuit = suit[s]
    cardvalue = cards[c]
    if c > 8 and c < 12:
        userpoints += 10
    elif c == 12:
        if userpoints < 11:
            userpoints += 11
        elif userpoints > 10:
            userpoints += 1
    else:
        userpoints += c + 2
    return cardsuit + " " + str(cardvalue)

print()
print("Välkommen till blackjack")
time.sleep(1)

tutorial = input("Vet du hur man spelar? ")
if tutorial == "Nej" or tutorial == "nej":
    print()
    print("Det är ett spel mot dig och datorn")
    print("Du drar 2 kort och får sen välja om du vill dra fler eller passa")
    print("Man vill så så nära 21 poäng som möjligt men går man över 21 är det game over")
    print("Alla numrerade kort har sina egna värden")
    print("Knekt, dam och kung har värdet 10")
    print("Ess har värdet 11 om det inte överksider 21, isåfall får den värdet 1")
    print("Lycka till")
    print()
    time.sleep(5)

time.sleep(1)
print()
print("Dina kort är", card(), "och", card())

while keepplaying == True:
    choice = input("Vill du dra ett kort eller passa? ")
    if choice == "Dra" or choice == "dra":
        print("Du drog", card())
        if userpoints > 21:
            keepplaying = False
            print("Du drog över 21, game over")
            dealerkeepplaying = False
    elif choice == "Passa" or choice == "passa" or choice == "pass":
        keepplaying = False
    else:
        print("Välj ett av alternativen")

if userpoints < 22:
    time.sleep(1)
    print()
    print("Dealern drog", dealercard(), "och", dealercard())

while dealerkeepplaying == True:
    if dealerpoints < 12:
        time.sleep(1)
        print("Dealern drog igen och fick", dealercard())
    elif dealerpoints < 17 and dealerpoints > 11:
        dealerchance = random.randint(0, 1)
        if dealerchance == 0:
            time.sleep(1)
            print("Dealern drog igen och fick", dealercard())
    elif dealerpoints > 21:
        print("Dealern drog över 21, grattis")
        dealerkeepplaying = False
    else:
        print("Dealern passade")
        dealerkeepplaying = False

if userpoints < 22 and userpoints > dealerpoints:
    time.sleep(1)
    print("Grattis, du fick", userpoints, "poäng och dealern fick bara", dealerpoints, "poäng")
elif userpoints < 22 and dealerpoints < 22 and userpoints <= dealerpoints:
    time.sleep(1)
    print("Synd, du fick", userpoints, "men dealern fick", dealerpoints, "poäng")