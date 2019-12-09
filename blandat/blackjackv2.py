import random
suit = ("Hjärter", "Spader", "Ruter", "Klöver")
cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, "knekt", "dam", "kung", "ess")

userpoints = 0
dealerpoints = 0
keepplaying = True

print("Välkommen till blackjack")
c1s = random.randint(0, 3)
c1c = random.randint(0, 12)
c1suit = suit[c1s] 
c1value = cards[c1c]
c2s = random.randint(0, 3)
c2c = random.randint(0, 12)
c2suit = suit[c2s] 
c2value = cards[c2c]
print("Dina kort är", c1suit, c1value, "och", c2suit, c2value )
userpoints +=