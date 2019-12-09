import random
kortlek = ["hjärter 2", "spader 2", "ruter 2", "klöver 2", "hjärter 3", "spader 3", "ruter 3", "klöver 3", "hjärter 4", "spader 4", "ruter 4", "klöver 4", "hjärter 5", "spader 5", "ruter 5", "klöver 5", "hjärter 6", "spader 6", "ruter 6", "klöver 6", "hjärter 7", "spader 7", "ruter 7", "klöver 7", "hjärter 8", "spader 8", "ruter 8", "klöver 8", "hjärter 9", "spader 9", "ruter 9", "klöver 9", "hjärter 10", "spader 10", "ruter 10", "klöver 10", "hjärter knekt", "spader knekt", "ruter knekt", "klöver knekt", "hjärter dam", "spader dam", "ruter dam", "klöver dam", "hjärter kung", "spader kung", "ruter kung", "klöver kung", "hjärter ess", "spader ess", "ruter ess", "klöver ess"]

keepplaying = True

userpoint = 0

print("Välkommen till blackjack")
cc1 = random.randint(0, 51)
c1 = kortlek[cc1]
cc2 = random.randint(0, 51)
c2 = kortlek[cc2]
print("Första kortet är", c1, "och andra är", c2)
loop = 0
    
while keepplaying == True:
    choice = input("Vill du dra eller passa? ")
    if choice == "dra" and loop == 0:
        cc3 = random.randint(0, 51)
        c3 = kortlek[cc3]
        loop = 1
        print("Du drog", c3)
    elif choice == "dra" and loop == 1:
        cc4 = random.randint(0, 51)
        c4 = kortlek[cc4]
        loop = 2
        print("Du drog", c4)
    elif choice == "dra" and loop == 2:
        cc5 = random.randint(0, 51)
        c5 = kortlek[cc5]
        loop = 3
        print("Du drog", c5)
    elif choice == "passa":
        keepplaying = False
    elif choice == "dra" and loop == 3:
        keepplaying = False

bb1 = random.randint(0, 51)
b1 = kortlek[bb1]
bb2 = random.randint(0, 51)
b2 = kortlek[bb2]

print("Dealern fick", b1, "och", b2)