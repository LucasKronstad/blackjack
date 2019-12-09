score = 0
print()
print("Welcome to my padel quiz")
print ()

print("What country is padel most popular in? ")
q1 = int(input("1: Spain. 2: USA. 3: Sweden "))
if q1 == 1:
    print("Good job")
    score = score + 1
elif q1 == 2:
    print("That's the wrong answer")
elif q1 == 3:
    print("That's the wrong answer")
else:
    print("Please choose an answer next time")
print()

q2 = input("What sport is padel most similar to? ")
if q2 == "Tennis":
    print("Good job")
    score = score + 1
elif q2 == "tennis":
    print("Good job")
    score = score + 1
else:
    print("That's the wrong answer")
print()

print("The score system in padel is the same as tennis, ")
q3 = int(input("How many points do you get if you win a ball? Answer in numbers "))
if q3 == 15:
    print("Good job")
    score = score + 1
else:
    print("That's the wrong answer")
print()

print("Which of the following is not the name of a shot? ")
q4 = input("A: Smash. B: Slice. C: Spin ")
if q4 == "C":
    print("Good job")
    score = score + 1
elif q4 == "B":
    print("That's the wrong answer")
elif q4 == "A":
    print("That's the wrong answer")
elif q4 == "c":
    print("Good job")
    score = score + 1
elif q4 == "b":
    print("That's the wrong answer")
elif q4 == "a":
    print("That's the wrong answer")
else:
    print("Please choose an answer next time")
print()

q5 = input("Generally, how many players are on the court? Answer in letters or numbers ")
if q5 == "four":
    print("Good job")
    score = score + 1
elif q5 == "Four":
    print("Good job")
    score = score + 1
elif int(q5) == 4:
    print("Good job")
    score = score + 1
else:
    print("That's the wrong answer")
print()

scorep = score / 5 * 100
if score == 1:
    print("You got", score, "question right")
else:
    print("You got", score, "questions right")
print("That's", int(scorep), "percent correct!")