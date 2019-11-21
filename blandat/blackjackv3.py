import random
import time

suit = ("Hjärter", "Spader", "Ruter", "Klöver")
cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, "knekt", "dam", "kung", "ess")

user_points = 0
dealer_points = 0
keep_playing = True
dealer_keep_playing = True

def dealer_card():
    global user_points, dealer_points

    s = random.randint(0, 3)
    c = random.randint(0, 12)
    card_suit = suit[s]
    card_value = cards[c]

    if c > 8 and c < 12:
        dealer_points += 10
    elif c == 12:
        if dealer_points < 11:
            dealer_points += 11
        elif dealer_points > 10:
            dealer_points += 1
    else:
        dealer_points += c + 2

    return card_suit + " " + str(card_value)

def card():
    global user_points, dealer_points

    s = random.randint(0, 3)
    c = random.randint(0, 12)
    card_suit = suit[s]
    card_value = cards[c]

    if c > 8 and c < 12:
        user_points += 10
    elif c == 12:
        if user_points < 11:
            user_points += 11
        elif user_points > 10:
            user_points += 1
    else:
        user_points += c + 2

    return card_suit + " " + str(card_value)

print()
print("Välkommen till blackjack")
time.sleep(1)

tutorial = input("Vet du hur man spelar? (Ja / Nej) ").lower()
if tutorial == "nej":
    print()
    print("Det är ett spel mot dig och datorn")
    print("Du drar 2 kort och får sen välja om du vill dra fler eller passa")
    print("Man vill så så nära 21 poäng som möjligt men går man över 21 är det game over")
    print("Alla numrerade kort har sina egna värden")
    print("Knekt, dam och kung har värdet 10")
    print("Ess har värdet 11 om det inte överksider 21, isåfall får den värdet 1")
    print("Lycka till")
    time.sleep(5)

time.sleep(1)
print()
print("Dina kort är", card(), "och", card())

while keep_playing == True:
    choice = input("Vill du dra ett kort eller passa? (Dra / Passa) ").lower()
    if choice == "dra":
        print("Du drog", card())
        if user_points > 21:
            keep_playing = False
            print("Du drog över 21, game over")
            dealer_keep_playing = False
    elif choice == "passa":
        keep_playing = False
    else:
        print("Välj ett av alternativen")

if user_points < 22:
    time.sleep(1)
    print()
    print("Dealern drog", dealer_card(), "och", dealer_card())

while dealer_keep_playing == True:
    if dealer_points < 12:
        time.sleep(1)
        print("Dealern drog igen och fick", dealer_card())
    elif dealer_points < 17 and dealer_points > 11:
        dealer_chance = random.randint(0, 1)
        if dealer_chance == 0:
            time.sleep(1)
            print("Dealern drog igen och fick", dealer_card())
    elif dealer_points > 21:
        print("Dealern drog över 21, grattis")
        dealer_keep_playing = False
    else:
        print("Dealern passade")
        dealer_keep_playing = False

if user_points < 22 and user_points > dealer_points:
    time.sleep(1)
    print("Grattis, du fick", user_points, "poäng och dealern fick bara", dealer_points, "poäng")
elif user_points < 22 and dealer_points < 22 and user_points <= dealer_points:
    time.sleep(1)
    print("Synd, du fick", user_points, "men dealern fick", dealer_points, "poäng")